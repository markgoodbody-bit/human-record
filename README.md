# Human Record public door — deployment source

Status: **PUBLIC STATIC SITE / STEWARDSHIP OFFERED TO 1F916 — NOT YET ACCEPTED**

Read [The Human Record](https://thehumanrecord.net/). Ordinary HTTPS access was
verified on 15 September 2026. Publication does not establish provenance claims
or community ownership. See [STEWARDSHIP.md](STEWARDSHIP.md) for the offer and
current custody, [LICENSE.md](LICENSE.md) for the bounded scope of the CC0
dedication, and [CONTINUE.md](CONTINUE.md) for non-founder recovery/serving
instructions.

Related wider project entrance: [Please Start From Here](https://pleasestartfromhere.com/). It is a separate public object and is not part of this record, its evidence, or its stewardship offer.

This directory is intentionally boring. It is the complete first static public-door payload for `thehumanrecord.net`.

Contents:
- `index.html` — human-readable entrance and specimen summary;
- `specimen.md` — exact human-readable specimen copied from COM after PR #328;
- `specimen.json` — exact machine-readable specimen copied from COM after PR #328;
- `llms.txt` — compact machine entrance and boundaries;
- `robots.txt` — explicit public crawler route and sitemap pointer; not a rights grant;
- `sitemap.xml` — first-party public discovery map;
- `STEWARDSHIP.md` — public stewardship offer, current custody and limits;
- `LICENSE` — standard CC0 1.0 legal code;
- `LICENSE.md` — bounded scope notice explaining which rights Mark actually purports to dedicate and third-party boundaries;
- `CONTINUE.md` — operational continuation/recovery note for a future non-founder operator;
- `CNAME` — configured custom domain;
- `.nojekyll` — serve files without Jekyll processing.

Canonical specimen source used for this copy:

`d117594e3718bd3df613f82d53b9dc9971860caf`

The public-door copy must not silently outrun the canonical record. If the canonical specimen is corrected later, publish a dated update and preserve what changed.

## Hosting boundary

Do **not** deploy this directory by replacing COM's existing `gh-pages` branch. That branch serves Please Start From Here and is a separate public object.

Current deployment path:

```text
markgoodbody-bit/human-record repository root
-> GitHub Pages from main/root
-> custom domain thehumanrecord.net
-> Namecheap DNS to the GitHub Pages site
-> HTTPS
-> verify index.html + specimen.md + specimen.json + llms.txt
-> stop and observe
```

An independent operator should follow `CONTINUE.md`; in particular, do not copy or claim the existing `CNAME`/custom-domain association without legitimate control of that domain.

No framework, database, JavaScript, analytics, login, token, CMS or specimen 2 is required for the first public object.

## Ceilings

```text
PROVENANCE != AUTHORSHIP_DETECTOR
SELECTION != SIGNIFICANCE
WORK_RIGHTS != REPRODUCTION_RIGHTS
SOURCE_LINK != SOURCE_PRESERVED
HASH != TRUTH
OFFERED != ACCEPTED
CC0_GRANT != THIRD_PARTY_RIGHTS_GRANT
INDEPENDENT_COPY != INDEPENDENT_GOVERNANCE
PLUMBING_SPECIMEN != SYNTHETIC_ERA_PURPOSE_TEST
PUBLICATION != VALIDATION
```
