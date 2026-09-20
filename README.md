# Human Record public door — deployment source

Status: **PUBLIC STATIC SITE / STEWARDSHIP OFFERED TO 1F916 — NOT YET ACCEPTED**

Read [The Human Record](https://thehumanrecord.net/). Ordinary HTTPS access was
verified on 15 September 2026; the first human-browser deployment was subsequently
verified against its pinned repository source on 16 September 2026. Publication does
not establish provenance claims or community ownership. See
[STEWARDSHIP.md](STEWARDSHIP.md) for the offer and current custody,
[LICENSE.md](LICENSE.md) for the bounded scope of the CC0 dedication, and
[CONTINUE.md](CONTINUE.md) for non-founder recovery/serving instructions.

The project is built collaboratively with artificial-intelligence apertures, but the
public record is intended as a gift for humans as well as machine readers. The normal
human route is [`records/`](records/): a browseable catalogue and readable views of the
current records. [`records/about.html`](records/about.html) explains the common anatomy
of a record in ordinary language, including [who builds and checks it](records/about.html#who-builds-this).
[`records/architecture.html`](records/architecture.html)
explains how the same discipline can scale when human names collide and web sources
change or disappear. Those pages are derived reading surfaces, not new evidence and not
replacements for the Markdown/JSON records or Git history.

The smallest common structure earned by the existing records is described in
[`RECORD_CONTRACT.md`](RECORD_CONTRACT.md). It is a semantic interoperability note,
not a universal schema, canon, certification standard or claim that every kind of human
knowledge can be represented identically.

[`SELECTION.md`](SELECTION.md) carries the working rule for choosing future records: look
for a specific recoverability/provenance gap, check stronger preservation owners first,
and do not turn risk into permission to extract or publish living/community knowledge.
It is a selection orientation, not a ranked queue of human importance.

The first scale layer is documented in [`SCALE.md`](SCALE.md),
[`IDENTITY_MODEL.md`](IDENTITY_MODEL.md) and [`SOURCE_MODEL.md`](SOURCE_MODEL.md).
Cross-record opaque identifiers and source-currentness/preservation state live in the
small [`registry/`](registry/) index. They are working interoperability machinery, not a
universal ontology or a database of everyone.

Related wider project entrance: [Please Start From Here](https://pleasestartfromhere.com/).
It is a separate public object and is not part of this record, its evidence, or its
stewardship offer.

The public door currently carries four deliberately different record objects:

- the original human-made artwork provenance specimen;
- a provenance case tracing the viral “80% of German flak crews died” claim without replacing uncertainty with another unsupported number;
- a public-source transmission-lineage case tracing sieve and riddle making from a reported last maker, through an extinction classification, into renewed practice while leaving open what was transmitted, reconstructed or newly learned;
- a historical-person source-survival record tracing a bounded route from the modern label “Hannibal Barca” back through checked Nepos and Polybius reading surfaces while preserving mediation, attribution and source limits.

None is a detector, certification authority, historical oracle or claim of canon. The living-practice case is not a craft manual and does not imply practitioner participation or endorsement. The historical-person case is not a complete biography or a substitute for classical source criticism.

Contents:
- `index.html` — human-facing public entrance;
- `records/index.html` — human-facing record catalogue;
- `records/about.html` — human explanation of the common record anatomy;
- `records/architecture.html` — human explanation of scale, identity collisions and source survival;
- `records/camp-fire.html` — readable view of the artwork specimen;
- `records/flak-claim.html` — readable view of the historical claim-provenance case;
- `records/sieve-riddle-revival.html` — readable view of the living-knowledge transmission-lineage case;
- `records/hannibal.html` — readable view of the historical-person source-survival case;
- `records/catalog.json` — small discovery/currentness catalogue, not a universal schema;
- `records/style.css` — shared presentation for the human record browser;
- `RECORD_CONTRACT.md` — minimum semantic contract earned by the current records;
- `SELECTION.md` — working selection discipline for future records;
- `SCALE.md` — current scale architecture and incremental migration path;
- `IDENTITY_MODEL.md` — opaque entity IDs, mentions and unresolved identity handling;
- `SOURCE_MODEL.md` — source/locator/observation/preservation separation;
- `ASSERTION_MODEL.md` — sparse evidence-bearing assertion and correction-reference model;
- `registry/entities.json` — sparse cross-record entity index;
- `registry/mentions.json` — source-literal mentions and unresolved/candidate identity state;
- `registry/sources.json` — cross-record source/observation/preservation-state index;
- `registry/source-checks.json` — operational currentness receipts kept separate from record evidence;
- `registry/assertions.json` — cross-record evidence-bearing propositions and correction references;
- `registry/README.md` — registry growth and privacy boundaries;
- `tools/validate_integrity.py` — local structural/view-pin/registry validator;
- `.github/workflows/validate-integrity.yml` — CI execution of the validator;
- `specimen.md` — current human-readable artwork record;
- `specimen.json` — current machine-readable artwork record;
- `cases/viral-flak-claim.md` — human-readable provenance reconstruction of the viral historical claim;
- `cases/viral-flak-claim.json` — machine-readable provenance reconstruction;
- `cases/sieve-riddle-revival.md` — full human-readable public-source transmission-lineage record;
- `cases/sieve-riddle-revival.json` — machine-readable transmission-lineage record;
- `cases/hannibal-barca.md` — full historical-person source-survival record;
- `cases/hannibal-barca.json` — machine-readable historical-person source-survival record;
- `llms.txt` — compact machine entrance and boundaries;
- `robots.txt` — explicit public crawler route and sitemap pointer; not a rights grant;
- `sitemap.xml` — first-party public discovery map;
- `STEWARDSHIP.md` — public stewardship offer, current custody and limits;
- `CONTRIBUTE.md` — public inspection/challenge/contribution route;
- `CONTRIBUTION_PACKET.md` — optional relay format for preserving attribution, source-check and unknown/not-checked boundaries when a contributor cannot post directly;
- `contribution-packet.schema.json` — JSON Schema for the optional packet; validates shape, not identity or truth;
- `examples/grok-flak-relay.packet.json` — real relay example reconstructed from the public issue #20 receipt, not a source-authentication claim;
- `LICENSE` — standard CC0 1.0 legal code;
- `LICENSE.md` — bounded scope notice explaining which rights Mark actually purports to dedicate and third-party boundaries;
- `CONTINUE.md` — operational continuation/recovery note for a future non-founder operator;
- `CNAME` — configured custom domain;
- `.nojekyll` — serve files without Jekyll processing.

## Current source and historical lineage

The current operational source for Human Record records, corrections, human views and
continuation is this repository:

`https://github.com/markgoodbody-bit/human-record`

The first artwork specimen entered the public Human Record from earlier project work in
COM; the original specimen merge lineage includes:

`d117594e3718bd3df613f82d53b9dc9971860caf`

That older COM material remains useful build provenance. It is not required as the
operational record store or correction route for current Human Record entries.

```text
BUILD_PROVENANCE != CURRENT_RECORD_AUTHORITY
HISTORICAL_SOURCE_LINEAGE != OPERATIONAL_DEPENDENCY
```

The current full record files in this repository own their present state. Human browser
pages must not silently outrun those underlying records. Corrections should be dated and
preserve what changed.

## Human-interface boundary

The human browser exists to make records legible without requiring readers to navigate raw
Markdown, JSON, GitHub history or governance files first.

It should make visible, in ordinary language:

- what the record is about;
- what can currently be said from the checked evidence;
- what remains unknown or unexamined;
- how source ancestry/independence bears on the claim;
- which corrections materially changed the record;
- where to inspect the full record and machine form.

```text
HUMAN_VIEW != NEW_EVIDENCE
SUMMARY != SOURCE
BROWSEABLE != CERTIFIED
AI_BUILT != AI_FACING_ONLY
```

## Scale boundary

The Human Record should be able to grow without making names or URLs into brittle primary keys.

The current working separations are:

```text
NAME != ENTITY
MENTION != ENTITY
URL != SOURCE
SOURCE != OBSERVATION
OBSERVATION != PRESERVED COPY
PRESERVED COPY != TRUTH
HUMAN VIEW != RECORD STATE
```

Opaque entity IDs let a label change without changing the referent. A source ID can retain several locators and observations over time. Identity ambiguity can remain unresolved rather than being forced into one machine match. Preservation state can remain `not_yet_checked` rather than treating a live link as an archive.

The scale layer is intentionally incremental. Existing record formats are not being flattened into one schema. Add shared entity/source references when a real repeated-identity, source-ancestry, currentness or preservation problem makes them useful.

AI is particularly useful for the repeated work: reconciling aliases and source relations, detecting proposition drift, fingerprinting observations, finding archived states, checking currentness, surfacing ambiguity and regenerating human views. That comparative advantage does not confer truth or governance authority.

```text
AI_MATCH != SILENT_IDENTITY_FACT
STORAGE_BACKEND != RECORD_MEANING
COMPREHENSIVE PURPOSE != COLLECT EVERYTHING NOW
```

## Living-knowledge boundary

The sieve-and-riddle case is the first current Human Record entry about a living practice.

Heritage Crafts is treated as the strongest identified owner for current UK craft status, practitioner counts, viability and safeguarding. The Human Record does not independently classify the craft or replace that work.

The THR contribution is narrower: preserve public-source lineage around the reported last maker, extinction classification, revival and current training, while keeping the central missing question visible — what was transmitted, reconstructed or newly learned, and through which routes.

The record uses already-public reporting. It does not claim contact, consent, participation or endorsement from the named living practitioners, and it does not reproduce a detailed craft manual or private teaching material.

```text
RECORDING != CONTINUATION
ATTENTION_PATHWAY != SKILL_TRANSMISSION
PUBLIC_SOURCE != ENDORSEMENT
RISK != PERMISSION
PRESERVATION != EXTRACTION
```

## Provenance-case boundary

The viral flak case records a visible source/repetition/correction chain. Its current claim status is:

```text
CLAIM: roughly 80% of German anti-aircraft crew members died during WWII
STATUS: UNSUPPORTED IN SOURCES CHECKED
TRUE AGGREGATE RATE: UNKNOWN
```

`UNSUPPORTED_IN_SOURCES_CHECKED != PROVED_FALSE`.

The case exists to make the evidence ancestry walkable: original presentation, downstream
repetition, community challenge, a later video's contradictory assertions, historical
sources for nearby facts, and remaining unknowns. No primary German personnel series has
been examined for this case. Bounded portions of Westermann's scholarly study and a public
publisher preview of Overmans have been checked; the authenticated/full relevant editions,
underlying archival material and any flak-specific Overmans result remain unexamined.

## Hosting boundary

Do **not** deploy this directory by replacing COM's existing `gh-pages` branch. That branch
serves Please Start From Here and is a separate public object.

Current deployment path:

```text
markgoodbody-bit/human-record repository root
-> GitHub Pages from main/root
-> custom domain thehumanrecord.net
-> Namecheap DNS to the GitHub Pages site
-> HTTPS
-> verify index.html + records/* + registry/* + specimen.* + llms.txt + cases/*
-> stop and observe
```

An independent operator should follow `CONTINUE.md`; in particular, do not copy or claim
the existing `CNAME`/custom-domain association without legitimate control of that domain.

No framework, database, JavaScript, analytics, login, token or CMS is required for this
public object.

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
SUMMARY != SOURCE
RECORDING != OWNING
RECORDING != CONTINUATION
PRESERVATION != EXTRACTION
PUBLIC_SOURCE != ENDORSEMENT
NAME != ENTITY
MENTION != ENTITY
URL != SOURCE
SOURCE != OBSERVATION
OBSERVATION != PRESERVED COPY
PRESERVED COPY != TRUTH
IDENTITY_RESOLUTION != IDENTITY_CERTAINTY
```
