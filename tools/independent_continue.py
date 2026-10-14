"""Build/check an independent static THR copy. Standard library, no remote fetches.

Readback uses a disposable server bound ONLY to 127.0.0.1. Hashes identify bytes,
not truth, rights clearance, governance acceptance or permanent preservation.
"""
import argparse
import contextlib
import functools
import hashlib
import html
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import io
import json
import os
from pathlib import Path
import re
import subprocess
import threading
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import build_opener, ProxyHandler

ORIGIN = 'https://thehumanrecord.net'
CONTEXT = ('CONTINUE.md', 'LICENSE', 'LICENSE.md', 'STEWARDSHIP.md',
           'CONTRIBUTE.md', 'CONTRIBUTION_PACKET.md', 'RECORD_CONTRACT.md',
           'SELECTION.md', 'IDENTITY_MODEL.md', 'ASSERTION_MODEL.md', 'SOURCE_MODEL.md')
VALIDATORS = ('validate_all.py', 'validate_integrity.py', 'validate_operational.py',
              'validate_entity_admission.py')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def inside(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError('OUTSIDE_COPY: ' + str(relative))
    return path


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.claims_original_domain = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == 'link' and attrs.get('rel') == 'canonical' and attrs.get('href', '').startswith(ORIGIN):
            self.claims_original_domain = True


def references(path):
    if path.suffix not in ('.html', '.md', '.json', '.css', '.txt'):
        return []
    text = path.read_text(encoding='utf-8')
    if path.suffix == '.html':
        parser = Links()
        parser.feed(text)
        return parser.links
    # Inventory is intentionally bounded: ordinary Markdown links, CSS URLs,
    # and explicit http(s) locators. No execution or downloaded dependencies.
    urls = re.findall(r'https?://[^\s<>"`\)\]]+', text)
    if path.suffix == '.md':
        urls += re.findall(r'\]\(([^\s\)]+)', text)
    if path.suffix == '.css':
        urls += re.findall(r'url\([\s\'"]*([^\)\'"\s]+)', text)
    return sorted(set(urls))


def local_target(relative, url):
    parsed = urlsplit(urljoin(ORIGIN + '/' + relative, url))
    if parsed.scheme not in ('http', 'https') or parsed.hostname != 'thehumanrecord.net':
        return None
    path = unquote(parsed.path).lstrip('/')
    if not path:
        path = 'index.html'
    return path


def validate_source(root):
    # Reuse all three existing validators; do not reimplement record logic.
    import validate_all
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        code = validate_all.run(root)
    return code, output.getvalue()


def provenance(root, paths):
    try:
        head = subprocess.run(['git', '-C', str(root), 'rev-parse', 'HEAD'],
                              capture_output=True, text=True, check=True, timeout=10).stdout.strip()
        for name in paths:
            expected = subprocess.run(['git', '-C', str(root), 'rev-parse', head + ':' + name],
                                      capture_output=True, text=True, check=True, timeout=10).stdout.strip()
            raw = inside(root, name).read_bytes()
            actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
            if actual != expected:
                return {'commit': None, 'status': 'UNKNOWN_WORKTREE_BYTES_NOT_PINNED'}
        return {'commit': head, 'status': 'COPIED_PUBLIC_BYTES_MATCH_LOCAL_GIT_COMMIT'}
    except (OSError, subprocess.SubprocessError):
        return {'commit': None, 'status': 'UNKNOWN_NO_PROVABLE_LOCAL_COMMIT'}


def page(title, body):
    return ('<!doctype html><html lang="en"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta name="robots" content="noindex"><title>' + html.escape(title) + '</title>'
            '<style>body{font:18px/1.6 system-ui;max-width:70rem;margin:2rem auto;padding:0 1rem}'
            'pre{white-space:pre-wrap;overflow-wrap:anywhere}iframe{width:100%;height:60rem;border:1px solid #888}'
            'nav{display:flex;gap:1rem;flex-wrap:wrap}</style><body>'
            '<p><strong>INDEPENDENT COPY — not the original domain or a governance transfer.</strong></p>'
            '<h1>' + html.escape(title) + '</h1>' + body + '</body></html>')


def build(root, output):
    root, output = root.resolve(), output.resolve()
    if output.exists() or output.is_relative_to(root):
        raise ValueError('OUTPUT_MUST_BE_NEW_AND_OUTSIDE_SOURCE')
    code, validation = validate_source(root)
    if code:
        raise ValueError('SOURCE_VALIDATORS_BLOCKED\n' + validation)
    catalog = json.loads((root / 'records/catalog.json').read_text(encoding='utf-8'))
    selected = set(CONTEXT) | {'index.html', 'records/catalog.json', 'records/index.html',
                              'records/about.html', 'records/architecture.html', 'llms.txt'}
    selected.update(p.relative_to(root).as_posix() for p in (root / 'registry').glob('*') if p.is_file())
    selected.update(p.name for p in root.glob('*.md'))
    records = []
    for entry in catalog['records']:
        routes = {key: local_target('index.html', entry[key])
                  for key in ('human_view', 'full_human_record', 'machine_record', 'correction_route')}
        if any(value is None for value in routes.values()):
            raise ValueError('CATALOGUE_RECORD_ROUTE_NOT_LOCAL: ' + entry['id'])
        selected.update(routes.values())
        records.append({'id': entry['id'], 'routes': routes, 'title': entry['title']})
    pending, external = list(selected), set()
    while pending:
        name = pending.pop()
        path = inside(root, name)
        if not path.is_file() or path.is_symlink():
            raise ValueError('REQUIRED_SOURCE_MISSING_OR_SYMLINK: ' + name)
        for url in references(path):
            if urlsplit(url).netloc:
                # Even a copied own-host target retains an absolute original
                # locator in its unchanged evidence bytes; do not hide this.
                external.add(url)
            target = local_target(name, url)
            if target is None:
                external.add(url)
            elif target != 'CNAME' and target not in selected:
                if inside(root, target).is_dir():
                    # A repository folder link remains a local folder link.
                    # Copy public text/static dependencies, not an invented index.
                    directory = inside(root, target)
                    for child in directory.rglob('*'):
                        if child.is_file() and child.suffix in ('.md', '.json', '.html', '.css', '.py', '.png', '.jpg', '.svg') and '__pycache__' not in child.parts:
                            relative = child.relative_to(root).as_posix()
                            if relative not in selected:
                                selected.add(relative)
                                pending.append(relative)
                    continue
                if not inside(root, target).is_file():
                    raise ValueError('UNUSABLE_SOURCE_LINK: ' + name + ' -> ' + url)
                selected.add(target)
                pending.append(target)
    if any(Path(name).name.lower() == 'cname' for name in selected):
        raise ValueError('DOMAIN_ASSOCIATION_FORBIDDEN')
    source = provenance(root, sorted(selected))
    output.mkdir()
    for name in sorted(selected):
        dest = output / 'source' / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(inside(root, name).read_bytes())
    # Copy the existing validators and this executable for checking after source
    # checkout loss. They are tooling, not public record/evidence content.
    for name in (*VALIDATORS, 'independent_continue.py'):
        dest = output / '_kit_tools' / name
        dest.parent.mkdir(exist_ok=True)
        dest.write_bytes((root / 'tools' / name).read_bytes())
    (output / 'reading').mkdir()
    (output / 'context').mkdir()
    for name in sorted(selected):
        if Path(name).suffix == '.md' or name == 'LICENSE':
            dest = output / 'context' / (name + '.html')
            dest.parent.mkdir(parents=True, exist_ok=True)
            raw = inside(root, name).read_text(encoding='utf-8')
            source_link = os.path.relpath(output / 'source' / name, dest.parent).replace('\\', '/')
            dest.write_text(page(name, '<p>Plain-text reading of preserved source; no new evidence. '
                                 '<a href="' + html.escape(source_link) + '">Exact source bytes</a></p>'
                                 '<pre>' + html.escape(raw) + '</pre>'), encoding='utf-8', newline='\n')
    items = []
    for record, entry in zip(records, catalog['records']):
        identifier = record['id']
        if not re.fullmatch(r'[a-zA-Z0-9_-]+', identifier):
            raise ValueError('UNSAFE_RECORD_ID')
        routes = record['routes']
        body = '<nav><a href="../catalogue.html">Catalogue</a><a href="../context/CONTRIBUTE.md.html">Correction context</a></nav>'
        body += '<h2>Known in this record</h2><p>' + html.escape(entry.get('known_summary', 'See source')) + '</p>'
        body += '<h2>Unknown or unexamined</h2><p>' + html.escape(entry.get('unknown_summary', 'See source')) + '</p>'
        body += ('<p><a href="../context/' + routes['full_human_record'] + '.html">Full human record</a> · '
                 '<a href="../source/' + routes['machine_record'] + '">Machine record</a> · '
                 '<a href="../source/' + routes['human_view'] + '">Preserved original human view</a></p>')
        body += '<iframe sandbox title="Preserved original human view" src="../source/' + routes['human_view'] + '"></iframe>'
        (output / 'reading' / (identifier + '.html')).write_text(page(record['title'], body), encoding='utf-8', newline='\n')
        record['reading_route'] = 'reading/' + identifier + '.html'
        items.append('<li><a href="' + record['reading_route'] + '">' + html.escape(record['title']) + '</a></li>')
    nav = '<nav><a href="index.html">Independent entrance</a><a href="source/records/catalog.json">Original machine catalogue</a></nav>'
    (output / 'catalogue.html').write_text(page('Independent reading catalogue', nav + '<ul>' + ''.join(items) + '</ul>'), encoding='utf-8', newline='\n')
    context = ''.join('<li><a href="context/' + name + '.html">' + name + '</a></li>' for name in CONTEXT)
    stewardship = next((line for line in (root / 'STEWARDSHIP.md').read_text(encoding='utf-8').splitlines()
                        if line.startswith('Status:')), 'UNKNOWN_SOURCE_STEWARDSHIP_STATUS')
    body = ('<p>Original public source: https://github.com/markgoodbody-bit/human-record. '
            'Observed local source commit: ' + html.escape(source['commit'] or 'UNKNOWN') + '.</p>'
            '<p>Project rights cover only rights actually held; linked third-party works are not imported. '
            'This copy establishes no governance transfer.</p><p>Preserved source declaration: '
            + html.escape(stewardship) + '</p>'
            '<p><a href="catalogue.html">Browse all current catalogue records</a> · '
            '<a href="source/records/catalog.json">Machine catalogue</a> · '
            '<a href="external-links.json">Links requiring external hosts</a></p>'
            '<h2>Rights, correction and continuation</h2><ul>' + context + '</ul>'
            '<p>The preserved source pages may identify their original canonical domain; that is source metadata, '
            'not a domain claim by this copy. Correction submissions still use the original repository route and may require an account.</p>')
    (output / 'index.html').write_text(page('The Human Record — independent reading copy', body), encoding='utf-8', newline='\n')
    (output / 'external-links.json').write_text(json.dumps({'fetched': False, 'links': sorted(external),
        'scope': 'Bounded HTML/Markdown/CSS/explicit-URL inventory; includes original-host locators and metadata; not live host or rights verification'}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    manifest = {'format': 'thr-independent-copy/0.1', 'source': source, 'records': records,
                'external_link_count': len(external), 'stewardship_notice': stewardship,
                'validator_report': validation.replace(str(root), 'SOURCE_ROOT'),
                'scope': 'LOCAL_STATIC_COPY_ONLY_NOT_TRUTH_RIGHTS_GOVERNANCE_OR_PERMANENCE',
                'files': {p.relative_to(output).as_posix(): {'sha256': digest(p.read_bytes()), 'bytes': p.stat().st_size}
                          for p in sorted(output.rglob('*')) if p.is_file()}}
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    return output


def inspect(copy):
    copy = copy.resolve()
    manifest = json.loads((copy / 'manifest.json').read_text(encoding='utf-8'))
    problems = []
    if any(p.is_symlink() for p in copy.rglob('*')):
        problems.append('SYMLINK_IN_COPY')
    if any(p.name.lower() == 'cname' for p in copy.rglob('*')):
        problems.append('CNAME_LEAK')
    expected = set(manifest['files']) | {'manifest.json'}
    actual = {p.relative_to(copy).as_posix() for p in copy.rglob('*') if p.is_file()
              and '__pycache__' not in p.parts}
    if actual != expected:
        problems.append('FILE_SET_CHANGED')
    for name, entry in manifest['files'].items():
        path = inside(copy, name)
        if not path.is_file() or path.is_symlink() or digest(path.read_bytes()) != entry['sha256']:
            problems.append('COPY_HASH_MISMATCH: ' + name)
    for path in copy.rglob('*.html'):
        if '__pycache__' in path.parts:
            continue
        parser = Links()
        parser.feed(path.read_text(encoding='utf-8'))
        relative = path.relative_to(copy).as_posix()
        if not relative.startswith('source/'):
            if 'INDEPENDENT COPY' not in path.read_text(encoding='utf-8') or parser.claims_original_domain:
                problems.append('DOMAIN_IMPERSONATION: ' + relative)
        for url in parser.links:
            # Historical absolute original-host locators remain external to this
            # independent copy; relative links must genuinely resolve here.
            if urlsplit(url).scheme or url.startswith('//'):
                continue
            target = local_target(relative, url)
            if target and not inside(copy, target).exists():
                problems.append('UNUSABLE_LOCAL_LINK: ' + relative + ' -> ' + url)
    catalog = json.loads((copy / 'source/records/catalog.json').read_text(encoding='utf-8'))
    if [r['id'] for r in catalog['records']] != [r['id'] for r in manifest['records']]:
        problems.append('CATALOGUE_SCOPE_CHANGED')
    for record in manifest['records']:
        for name in (*record['routes'].values(),):
            if not inside(copy / 'source', name).is_file():
                problems.append('MISSING_RECORD_ROUTE: ' + name)
    code, _ = validate_source(copy / 'source')
    if code:
        problems.append('PRESERVED_SOURCE_VALIDATORS_FAILED')
    return manifest, problems


def readback(copy):
    manifest, problems = inspect(copy)
    if problems:
        return {'status': 'BLOCKED', 'problems': problems}
    class Handler(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def end_headers(self):
            self.send_header('X-THR-Copy', 'INDEPENDENT_NOT_ORIGINAL_DOMAIN')
            self.send_header('Content-Security-Policy', "default-src 'none'; style-src 'self' 'unsafe-inline'; img-src 'self'; frame-src 'self'; base-uri 'none'; form-action 'none'")
            super().end_headers()

    server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Handler, directory=str(copy)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    count = 0
    try:
        opener = build_opener(ProxyHandler({}))  # no system proxy or remote host
        for name, entry in manifest['files'].items():
            with opener.open('http://127.0.0.1:%s/%s' % (server.server_port, name), timeout=10) as response:
                if response.status != 200 or digest(response.read()) != entry['sha256']:
                    raise ValueError('HTTP_READBACK_MISMATCH: ' + name)
                count += 1
    finally:
        server.shutdown()
        thread.join(5)
        server.server_close()
    return {'status': 'PASS' if manifest['source']['commit'] else 'PARTIAL',
            'scope': 'LOCAL_STATIC_COPY_READBACK_ONLY', 'source': manifest['source'],
            'records': len(manifest['records']), 'http_files_verified': count,
            'external_link_count': manifest['external_link_count'], 'external_requests': 0,
            'manifest_sha256': digest((copy / 'manifest.json').read_bytes()),
            'source_stewardship_declaration': manifest['stewardship_notice'],
            'governance_acceptance_verified': False, 'rights_adjudicated': False,
            'limits': ['No third-party works fetched', 'No actual non-founder participation',
                       'No historical truth, permanence or browser/assistive-technology proof']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, help='New directory outside source; never overwritten')
    parser.add_argument('--check', type=Path, help='Check an existing copy including disposable loopback readback')
    args = parser.parse_args()
    try:
        target = args.check or build(args.source, args.output) if args.check or args.output else None
        if target is None:
            parser.error('Supply --output or --check')
        receipt = readback(target.resolve())
    except Exception as exc:
        receipt = {'status': 'BLOCKED', 'reason': str(exc), 'external_requests': 0}
    print(json.dumps(receipt, indent=2))
    return 1 if receipt['status'] == 'BLOCKED' else 0


if __name__ == '__main__':
    raise SystemExit(main())
