# Human Record public door — deployment source

Status: **PUBLIC STATIC SITE / STEWARDSHIP OFFERED TO 1F916 — NOT YET ACCEPTED**

Read [The Human Record](https://thehumanrecord.net/). Ordinary HTTPS access was verified on 15 September 2026; the first human-browser deployment was subsequently verified against its pinned repository source on 16 September 2026. Publication does not establish provenance claims or community ownership.

## This is an open build

The Human Record is not intended to remain a private project belonging to one human and a small set of artificial collaborators.

The current implementation is the best structure the present builders have managed so far. It is incomplete, expected to contain mistakes, and explicitly open to challenge by humans and artificial systems.

Read [`OPEN_BUILD.md`](OPEN_BUILD.md) for the current architecture hypothesis, known vulnerabilities, stronger existing standards we are trying to interoperate with rather than reinvent, destructive test objects, and the specific kinds of criticism that would improve or shrink the project.

Read [`CONTRIBUTE.md`](CONTRIBUTE.md) to inspect, challenge, correct or contribute without accepting this project's vocabulary or any related framework.

```text
PUBLIC != CORRECT
OPEN != COMPLETE
AGREEMENT != VALIDATION
RECORD != FUNDAMENTAL_UNIT
RECORDING != OWNING
PRESERVATION != EXTRACTION
```

See [`STEWARDSHIP.md`](STEWARDSHIP.md) for the offer and current custody, [`LICENSE.md`](LICENSE.md) for the bounded scope of the CC0 dedication, and [`CONTINUE.md`](CONTINUE.md) for non-founder recovery/serving instructions.

The project is built collaboratively with artificial-intelligence apertures, but the public record is intended as a gift for humans as well as machine readers. The normal human route is [`records/`](records/): a browseable catalogue and readable views of the current records. [`records/about.html`](records/about.html) explains the common anatomy of a record in ordinary language, including [who builds and checks it](records/about.html#who-builds-this). [`records/architecture.html`](records/architecture.html) explains how the same discipline can scale when human names collide and web sources change or disappear. Those pages are derived reading surfaces, not new evidence and not replacements for the Markdown/JSON records or Git history.

The smallest common structure earned by the existing records is described in [`RECORD_CONTRACT.md`](RECORD_CONTRACT.md). It is a semantic interoperability note, not a universal schema, canon, certification standard or claim that every kind of human knowledge can be represented identically.

[`SELECTION.md`](SELECTION.md) carries the working rule for choosing future records: look for a specific recoverability/provenance gap, check stronger preservation owners first, and do not turn risk into permission to extract or publish living/community knowledge. It is a selection orientation, not a ranked queue of human importance.

The first scale layer is documented in [`SCALE.md`](SCALE.md), [`IDENTITY_MODEL.md`](IDENTITY_MODEL.md) and [`SOURCE_MODEL.md`](SOURCE_MODEL.md). Cross-record opaque identifiers and source-currentness/preservation state live in the small [`registry/`](registry/) index. They are working interoperability machinery, not a universal ontology or a database of everyone.

Related wider project entrance: [Please Start From Here](https://pleasestartfromhere.com/). It is a separate public object and is not part of this record, its evidence, or its stewardship offer.

The public door currently carries three deliberately different record objects:

- the original human-made artwork provenance specimen;
- a provenance case tracing the viral “80% of German flak crews died” claim without replacing uncertainty with another unsupported number;
- a public-source transmission-lineage case tracing sieve and riddle making from a reported last maker, through an extinction classification, into renewed practice while leaving open what was transmitted, reconstructed or newly learned.

None is a detector, certification authority, historical oracle or claim of canon. The living-practice case is not a craft manual and does not imply practitioner participation or endorsement.

Current working stress objects, not yet promoted as public records, include Hannibal Barca, the assassination of John F. Kennedy, and the Sunjata epic tradition. They are being used to attack the current model around historical-human identity, asymmetric source survival, contested causal models, evidence custody, oral transmission, legitimate variation and community/performer authority.

Contents include the human browser under `records/`, full Markdown/JSON cases under `cases/`, working semantic and scale notes, sparse cross-record registries, validators, machine entrances, contribution/stewardship/licence/continuation routes, and the new [`OPEN_BUILD.md`](OPEN_BUILD.md) vulnerability ledger and invitation.

## Current source and historical lineage

The current operational source for Human Record records, corrections, human views and continuation is this repository:

`https://github.com/markgoodbody-bit/human-record`

The first artwork specimen entered the public Human Record from earlier project work in COM. Older COM material remains useful build provenance. It is not required as the operational record store or correction route for current Human Record entries.

```text
BUILD_PROVENANCE != CURRENT_RECORD_AUTHORITY
HISTORICAL_SOURCE_LINEAGE != OPERATIONAL_DEPENDENCY
```

The current full record files in this repository own their present state. Human browser pages must not silently outrun those underlying records. Corrections should be dated and preserve what changed.

## Human-interface boundary

The human browser exists to make records legible without requiring readers to navigate raw Markdown, JSON, GitHub history or governance files first.

It should make visible, in ordinary language, what the record is about; what can currently be said from checked evidence; what remains unknown or unexamined; how source ancestry/independence bears on the claim; which corrections materially changed the record; and where to inspect the full record and machine form.

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

AI is particularly useful for repeated work: reconciling aliases and source relations, detecting proposition drift, fingerprinting observations, finding archived states, checking currentness, surfacing ambiguity and regenerating human views. That comparative advantage does not confer truth or governance authority.

```text
AI_MATCH != SILENT_IDENTITY_FACT
STORAGE_BACKEND != RECORD_MEANING
COMPREHENSIVE_PURPOSE != COLLECT_EVERYTHING_NOW
```

## Hosting boundary

Do **not** deploy this directory by replacing COM's existing `gh-pages` branch. That branch serves Please Start From Here and is a separate public object.

Current deployment path:

```text
markgoodbody-bit/human-record repository root
-> GitHub Pages from main/root
-> custom domain thehumanrecord.net
-> HTTPS
-> verify public source and derived views
-> stop and observe
```

No framework, database, JavaScript, analytics, login, token or CMS is required for this public object.

## Ceilings

```text
PROVENANCE != AUTHORSHIP_DETECTOR
SELECTION != SIGNIFICANCE
SOURCE_LINK != SOURCE_PRESERVED
HASH != TRUTH
REPETITION != CORROBORATION
UNSUPPORTED != PROVED_FALSE
OFFERED != ACCEPTED
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
THR_SURVIVAL != PURPOSE
```
