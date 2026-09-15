# Human Record public door — deployment source

Status: **PUBLIC STATIC SITE / STEWARDSHIP OFFERED TO 1F916 — NOT YET ACCEPTED**

Read [The Human Record](https://thehumanrecord.net/). Ordinary HTTPS access was
verified on 15 September 2026. Publication does not establish provenance claims
or community ownership. See [STEWARDSHIP.md](STEWARDSHIP.md) for the offer and
current custody, [LICENSE.md](LICENSE.md) for the bounded scope of the CC0
dedication, and [CONTINUE.md](CONTINUE.md) for non-founder recovery/serving
instructions.

Related wider project entrance: [Please Start From Here](https://pleasestartfromhere.com/). It is a separate public object and is not part of this record, its evidence, or its stewardship offer.

The public door now carries two deliberately different objects:

- the original human-made artwork provenance specimen;
- a provenance case tracing the viral “80% of German flak crews died” claim without replacing uncertainty with another unsupported number.

Neither is a detector, certification authority, historical oracle or claim of canon.

Contents:
- `index.html` — human-readable entrance and current record routes;
- `specimen.md` — exact human-readable artwork specimen copied from COM after PR #328;
- `specimen.json` — exact machine-readable artwork specimen copied from COM after PR #328;
- `cases/viral-flak-claim.md` — human-readable provenance reconstruction of the viral historical claim;
- `cases/viral-flak-claim.json` — machine-readable provenance reconstruction;
- `llms.txt` — compact machine entrance and boundaries;
- `robots.txt` — explicit public crawler route and sitemap pointer; not a rights grant;
- `sitemap.xml` — first-party public discovery map;
- `STEWARDSHIP.md` — public stewardship offer, current custody and limits;
- `LICENSE` — standard CC0 1.0 legal code;
- `LICENSE.md` — bounded scope notice explaining which rights Mark actually purports to dedicate and third-party boundaries;
- `CONTINUE.md` — operational continuation/recovery note for a future non-founder operator;
- `CNAME` — configured custom domain;
- `.nojekyll` — serve files without Jekyll processing.

Canonical specimen source used for the original artwork copy:

`d117594e3718bd3df613f82d53b9dc9971860caf`

The public-door copy must not silently outrun canonical records. Corrections should be dated and preserve what changed.

## Provenance-case boundary

The viral flak case records a visible source/repetition/correction chain. Its current claim status is:

```text
CLAIM: roughly 80% of German anti-aircraft crew members died during WWII
STATUS: UNSUPPORTED IN SOURCES CHECKED
TRUE AGGREGATE RATE: UNKNOWN
```

`UNSUPPORTED_IN_SOURCES_CHECKED != PROVED_FALSE`.

The case exists to make the evidence ancestry walkable: original viral presentation, downstream repetition, community challenge, later research, stronger historical sources for nearby facts, and remaining unknowns.

## Hosting boundary

Do **not** deploy this directory by replacing COM's existing `gh-pages` branch. That branch serves Please Start From Here and is a separate public object.

Current deployment path:

```text
markgoodbody-bit/human-record repository root
-> GitHub Pages from main/root
-> custom domain thehumanrecord.net
-> Namecheap DNS to the GitHub Pages site
-> HTTPS
-> verify index.html + specimen.md + specimen.json + llms.txt + cases/*
-> stop and observe
```

An independent operator should follow `CONTINUE.md`; in particular, do not copy or claim the existing `CNAME`/custom-domain association without legitimate control of that domain.

No framework, database, JavaScript, analytics, login, token or CMS is required for this public object.

## Ceilings

```text
PROVENANCE != AUTHORSHIP_DETECTOR
SELECTION != SIGNIFICANCE
WORK_RIGHTS != REPRODUCTION_RIGHTS
SOURCE_LINK != SOURCE_PRESERVED
HASH != TRUTH
REPETITION != CORROBORATION
UNSUPPORTED != PROVED_FALSE
OFFERED != ACCEPTED
CC0_GRANT != THIRD_PARTY_RIGHTS_GRANT
INDEPENDENT_COPY != INDEPENDENT_GOVERNANCE
PLUMBING_SPECIMEN != SYNTHETIC_ERA_PURPOSE_TEST
PUBLICATION != VALIDATION
```
