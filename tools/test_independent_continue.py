import json
from pathlib import Path
import shutil
import tempfile
import unittest
import independent_continue as kit

ROOT = Path(__file__).resolve().parents[1]


class ContinuationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='thr-copy-test-')
        self.base = Path(self.temp.name)
        self.output = self.base / 'copy'
        kit.build(ROOT, self.output)

    def tearDown(self):
        self.temp.cleanup()

    def test_all_current_records_context_and_actual_loopback_bytes(self):
        manifest, problems = kit.inspect(self.output)
        self.assertEqual(problems, [])
        catalog = json.loads((ROOT / 'records/catalog.json').read_text())
        self.assertEqual([x['id'] for x in manifest['records']], [x['id'] for x in catalog['records']])
        for record in manifest['records']:
            reading = (self.output / record['reading_route']).read_text(encoding='utf-8')
            self.assertIn('Unknown or unexamined', reading)
            self.assertIn('Correction context', reading)
            for route in record['routes'].values():
                self.assertEqual((self.output / 'source' / route).read_bytes(), (ROOT / route).read_bytes())
        receipt = kit.readback(self.output)
        self.assertIn(receipt['status'], ['PASS', 'PARTIAL'])
        self.assertEqual(receipt['records'], len(catalog['records']))
        self.assertEqual(receipt['external_requests'], 0)
        self.assertGreater(receipt['external_link_count'], 0)
        external = json.loads((self.output / 'external-links.json').read_text())['links']
        self.assertTrue(any(x.startswith(kit.ORIGIN) for x in external))
        self.assertIn('NOT YET ACCEPTED', receipt['source_stewardship_declaration'])
        # Generated navigation must work without assuming an HTTP origin root.
        for path in self.output.rglob('*.html'):
            if path.relative_to(self.output).parts[0] == 'source':
                continue
            parser = kit.Links()
            parser.feed(path.read_text(encoding='utf-8'))
            self.assertTrue(all(not url.startswith('/') for url in parser.links))

    def test_deterministic_manifest_for_same_source_and_tool_bytes(self):
        second = kit.build(ROOT, self.base / 'copy-two')
        self.assertEqual((self.output / 'manifest.json').read_bytes(), (second / 'manifest.json').read_bytes())

    def test_missing_record_is_blocked(self):
        (self.output / 'source/specimen.json').unlink()
        self.assertEqual(kit.readback(self.output)['status'], 'BLOCKED')

    def test_corrupted_record_is_not_a_byte_match(self):
        path = self.output / 'source/specimen.json'
        path.write_bytes(path.read_bytes() + b' ')
        _, problems = kit.inspect(self.output)
        self.assertTrue(any('COPY_HASH_MISMATCH' in p for p in problems))

    def test_cname_leak_and_original_domain_claim_are_blocked(self):
        (self.output / 'CNAME').write_text('thehumanrecord.net')
        _, problems = kit.inspect(self.output)
        self.assertIn('CNAME_LEAK', problems)
        (self.output / 'CNAME').unlink()
        index = self.output / 'index.html'
        index.write_text(index.read_text() + '<link rel="canonical" href="https://thehumanrecord.net/">')
        _, problems = kit.inspect(self.output)
        self.assertTrue(any('DOMAIN_IMPERSONATION' in p for p in problems))

    def test_unusable_link_is_blocked_even_if_manifest_hash_relabelled(self):
        index = self.output / 'index.html'
        index.write_text(index.read_text() + '<a href="missing-local-file.html">broken</a>')
        manifest = json.loads((self.output / 'manifest.json').read_text())
        manifest['files']['index.html']['sha256'] = kit.digest(index.read_bytes())
        (self.output / 'manifest.json').write_text(json.dumps(manifest))
        _, problems = kit.inspect(self.output)
        self.assertTrue(any('UNUSABLE_LOCAL_LINK' in p for p in problems))

    def test_no_git_source_keeps_origin_unknown_not_invented(self):
        source = self.base / 'recovered'
        shutil.copytree(self.output / 'source', source)
        (source / 'tools').mkdir()
        for name in (*kit.VALIDATORS, 'independent_continue.py'):
            shutil.copyfile(ROOT / 'tools' / name, source / 'tools' / name)
        recovered = kit.build(source, self.base / 'recovered-copy')
        receipt = kit.readback(recovered)
        self.assertEqual(receipt['status'], 'PARTIAL')
        self.assertIsNone(receipt['source']['commit'])

    def test_valid_files_without_frontdoor_navigation_do_not_pass(self):
        index = self.output / 'index.html'
        index.write_text(index.read_text().replace('href="catalogue.html"', 'href="index.html"'))
        manifest = json.loads((self.output / 'manifest.json').read_text())
        manifest['files']['index.html']['sha256'] = kit.digest(index.read_bytes())
        (self.output / 'manifest.json').write_text(json.dumps(manifest))
        _, problems = kit.inspect(self.output)
        self.assertTrue(any('UNREACHABLE_FROM_ENTRANCE' in p for p in problems))

    def test_no_overwrite_or_source_internal_output(self):
        with self.assertRaises(ValueError):
            kit.build(ROOT, self.output)
        with self.assertRaises(ValueError):
            kit.build(ROOT, ROOT / 'must-not-create')


if __name__ == '__main__':
    unittest.main(verbosity=2)
