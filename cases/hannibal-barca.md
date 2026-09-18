# Human Record — Hannibal through surviving evidence

Status: **PUBLIC RECORD 4 / HISTORICAL-PERSON SOURCE-SURVIVAL / PUBLIC SOURCES / NOT BIOGRAPHICAL CANON / OPEN TO CORRECTION**

Record ID: `hannibal-source-survival`  
Record version: **0.1.0**  
Recorded: 18 September 2026.

## Purpose

This record asks a narrow Human Record question:

> What is the smallest inspectable evidence path by which the historical human conventionally called Hannibal Barca remains reachable now, without turning surviving literary tradition into the person himself?

The record does **not** attempt a definitive biography, settle the Alpine route, reconstruct Hannibal's appearance, rank commanders, or treat every later retelling as an independent witness.

```text
NAME != ENTITY
ENTITY != BIOGRAPHY
ENTITY != CLAIMS ABOUT ENTITY
SURVIVING_SOURCE != COMPLETE_HISTORY
ATTESTED_WORK != INSPECTED_SOURCE
REPRESENTATION_OF_ENTITY != EVIDENCE_OF_ENTITY_APPEARANCE
SOURCE_REPORTS_X != THR_DIRECTLY_OBSERVED_X
```

## Thin entity anchor

Working entity: **Hannibal Barca**, the historical human named as Hannibal in the checked ancient literary surfaces below.

The entity anchor deliberately carries no exact birth/death date, portrait, Alpine pass, childhood-oath wording, or full office/kinship profile. Those are assertions requiring their own evidence paths.

The opaque candidate entity ID is a routing handle only. It is not evidence.

The full display string **Hannibal Barca** is used here as a conventional modern
routing label. The checked ancient passages in this fixture attest the literal
name **Hannibal**; this record does not claim that the full modern display
string is itself source-attested by those passages.

```text
CONVENTIONAL_DISPLAY_LABEL != SOURCE_ATTESTED_STRING
```

## Why this case was selected

Hannibal was selected deliberately as a **historical-person / source-survival
stress case** after the first three public Human Record entries had already
tested artwork provenance, repeated-claim ancestry, and living-practice
transmission.

The selection-time candidate pool and alternatives considered were not preserved
for this candidate. That gap does not establish that no alternatives were considered;
it means this record cannot honestly reconstruct them after the fact.

Selection does not establish representativeness, historical priority, importance,
or entitlement to become record 4.

```text
MISSING_SELECTION_HISTORY != PERMISSION_TO_INVENT_IT
SELECTED_AS_STRESS_CASE
!= REPRESENTATIVE_SAMPLE
!= MOST_IMPORTANT_PERSON
!= RECORD_4_ENTITLEMENT
```

## Checked source apertures

### Polybius, *Histories* Book 3

Public reading surface:

`https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Polybius/3*.html`

The host presents the English text as the 1922 Loeb translation and warns that
the web page has not yet been proofread. THR therefore treats it as a convenient
modern reading surface for bounded passage inspection, **not** as a manuscript
witness or a checked critical edition.

This record uses four bounded passages:

- **3.20.5** — Polybius names Chaereas and Sosylus and dismisses their authority sharply. This establishes that Polybius knew a Sosylus tradition; it does not make Polybius' evaluation neutral or final.
- **3.33.17–18** — Polybius says his unusually detailed troop figures came from a bronze tablet on the Lacinian promontory on which Hannibal had made out the lists. THR has not observed that tablet and does not convert Polybius' report into a surviving inscription object.
- **3.48.12** — Polybius says he inquired from men present at the crossing and personally inspected the country and crossed the Alps himself. This is evidence about Polybius' claimed method, not automatic proof of every detail in his reconstruction.
- **3.56.3–4** — Polybius reports Hannibal's post-crossing force totals and attributes them to an inscription/column at Lacinium. This candidate does **not** establish that the carrier described here is physically identical to the bronze tablet described at 3.33.17–18.

### Cornelius Nepos, *Life of Hannibal* 13.3

Public Latin/commentary surface:

`https://dcc.dickinson.edu/nepos-hannibal/chapter-13`

Nepos reports that Silenus and Sosylus lived with Hannibal in camp and wrote about the war, and identifies Sosylus as Hannibal's teacher of Greek literature.

This record records that **Nepos reports this relationship**. It does not create Silenus' or Sosylus' lost/fragmentary works as inspected THR sources merely because later authors attest them.

## Source-survival pressure

These two checked texts do not establish two independent witnesses to the same
event. They support different attributed propositions; their number is not a
corroboration count. This record does not establish direct dependence between
Nepos and Polybius either.

Polybius is both:
- a surviving narrative source for Hannibal's campaign; and
- a source critic who names and rejects Sosylus.

Nepos, writing later, attests Hannibal-entourage historians whose works are not preserved here as complete inspected source objects.

Modern scholarship also treats later Hannibal narratives as source-dependent. A current source-criticism orientation checked for this record is the Cambridge *Libyan Studies* article “Generals and judges: command, constitution and the fate of Carthage”:

`https://www.cambridge.org/core/journals/libyan-studies/article/generals-and-judges-command-constitution-and-the-fate-of-carthage/757F46BAE0CA1A08373A15D1E497198F`

It notes Polybius' use of Carthaginian documentary/informant material, Sosylus in Hannibal's entourage, and heavy later reliance on Polybius while preserving the existence of additional sources and interpretive lenses. This is orientation for source ancestry, not a substitute for reading the ancient passages.

Livy is therefore **not counted as an independent corroborating witness by default** in this record. A later source can be added when its relation to earlier material is itself evidenced.

```text
LATER_SOURCE != INDEPENDENT_WITNESS
SOURCE_DEPENDENCE_UNKNOWN != SOURCE_INDEPENDENT
ONE_SIDED_BY_SURVIVAL != FALSE
MISSING_CARTHAGINIAN_APERTURE != CARTHAGINIAN_HISTORY_DID_NOT_EXIST
```

The current checked narrative aperture is Greek/Roman-mediated. That asymmetry is part of the record, not a footnote to hide.

## Public machine route

The public machine record is:

`https://thehumanrecord.net/cases/hannibal-barca.json`

It keeps two source-literal `Hannibal` mentions separate — one from Nepos and one
from Polybius — and candidate-links both to the same thin entity anchor. That
allows later evidence to split or revise the mappings without rewriting either
source literal.

```text
SAME_LITERAL_ACROSS_SOURCES != IDENTITY_PROVED
CANDIDATE_LINK != ENTITY_CERTAINTY
```

The earlier research fixture remains in the repository as build/test lineage. It
is not the public machine record.

## What the executable fixture represents

The fixture attached to this candidate contains only:

- one candidate person entity;
- one literal Hannibal mention;
- two inspected web reading surfaces;
- source-attributed assertions;
- no direct-observation assertion;
- no invented Sosylus/Silenus source object;
- no catalogue identity.

It deliberately tests the current production validators after the 18 September semantic repairs.

Default/public validation continues to reject the research fixture's fabricated unpublished `record_id`; the public machine record uses `hannibal-source-survival`.

Explicit isolated research validation may omit `record_id` while retaining source + owned observation + context. That is workflow permission, not privacy or publication.

## Current bounded findings

1. The existing entity/source/assertion envelopes can carry a thin historical-human candidate without adding a new entity type or truth scale.
2. A source can report a claim about Hannibal without the entity anchor absorbing that claim as identity.
3. A later source can attest an earlier source tradition without THR pretending to have inspected the earlier work.
4. Polybius' claimed investigative method and documentary source can be recorded as **claims by Polybius** without becoming direct THR observations.
5. The current source set is asymmetrical and incomplete. The candidate should show that asymmetry rather than multiply later repetitions.

None of these findings establishes the historical truth of every underlying event.

## What remains unknown or deliberately unclaimed

This record does not establish:

- exact birth or death dates;
- the exact Alpine pass;
- a complete source genealogy between Polybius, Livy and other surviving writers;
- the contents of all surviving Sosylus/Silenus fragments;
- the full Punic/Carthaginian documentary record;
- Hannibal's appearance;
- the exact wording/historicity of the childhood oath;
- complete archaeological, numismatic or epigraphic evidence;
- a current scholarly consensus on every disputed episode.

```text
NOT_CHECKED != ABSENT
UNKNOWN != EMPTY_FIELD_TO_FILL
NO_SURVIVING_WHOLE != NO_FRAGMENT
```

## Publication boundary

Publication makes this a fourth Human Record encounter. It does not establish:
- reader benefit;
- historical authority over specialist scholarship;
- completeness of the source genealogy;
- identity certainty merely because the record has an entity handle.

The record was exposed as a non-catalogued reader proposal before promotion. No
reader-specific outside falsifier arrived in that interval. That null result is
recorded as a null result, not as approval.

```text
PUBLICATION != VALIDATION
NO_OUTSIDE_READER_REPLY != ENDORSEMENT
RECORD_4 != FOURTH_MOST_IMPORTANT_HUMAN_RECORD
```

## Strong-owner boundary

THR does not need a new historical ontology for this case.

Relevant owners already include:
- CIDOC CRM family for cultural-heritage/event semantics;
- W3C PROV for provenance/derivation;
- CRMinf for argumentation/inference provenance;
- Wikibase-style qualified statements/references/revision history;
- classical citation and historical source criticism for text identity and dependence.

The Human Record residue being tested is smaller: make source ancestry, unknowns, disagreement and correction visible to ordinary human and machine readers without pretending the sparse graph is the world.

## Promotion gate

This candidate does **not** become public record 4 merely because it validates structurally.

Before any catalogue promotion:

1. preserve direct-source locators and the Greek/Roman survival asymmetry;
2. hostile-review source dependence and any statement that reads like biography fact;
3. check whether the candidate adds human/public value beyond existing owner systems;
4. ensure the readable encounter does not flatten source reports into historical truth;
5. retain a correction route and explicit unexamined material;
6. decide whether publication adds more recoverability than noise.

```text
CANDIDATE != RECORD_4
STRUCTURAL_PASS != HISTORICAL_TRUTH
PUBLICATION != VALIDATION
THR_SURVIVAL != PURPOSE
```


## Public routes

- Human view: https://thehumanrecord.net/records/hannibal.html
- Machine record: https://thehumanrecord.net/cases/hannibal-barca.json
- Catalogue: https://thehumanrecord.net/records/catalog.json
- Correction route: https://thehumanrecord.net/CONTRIBUTE.md

The repository history preserves the earlier candidate state and the issue #40
identity-model repairs that preceded publication.

```text
PUBLIC_RECORD != HISTORICAL_ORACLE
CORRECTED_RECORD != ORIGINAL_EVENT_CHANGED
```
