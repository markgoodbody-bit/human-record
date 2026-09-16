# The Human Record — minimum record contract

Status: **WORKING INTEROPERABILITY NOTE / DERIVED FROM CURRENT RECORDS / NOT A UNIVERSAL SCHEMA / NOT CANON**

This document describes the smallest common structure currently earned by the three Human Record entries that exist.

It is not a claim that every kind of human knowledge or creativity can be represented in one JSON shape. It is not a certification standard, a truth oracle, an authorship detector, or a requirement that future records use identical field names.

The purpose is narrower: a human or machine should be able to enter any Human Record item and find the same basic questions answered.

```text
COMMON QUESTIONS != IDENTICAL OBJECTS
RECORD CONTRACT != UNIVERSAL ONTOLOGY
STRUCTURE != TRUTH
```

## 1. Identity

Every record should make it possible to identify the record itself without confusing the record with the thing or event it describes.

At minimum:

- a stable local record identifier;
- a human-readable title;
- a record type or kind;
- a version or revision state where the record changes over time;
- a route to the current human-readable record;
- a route to the current machine-readable record where one exists.

`RECORD != EVENT`

## 2. Subject or claim

A record must say what it is actually about.

For an artefact this may be an identified work and the attribution/provenance assertions being checked. For a claim-provenance case it may be the exact proposition whose source ancestry is being reconstructed. For a living-knowledge lineage case it may be the bounded public evidence for how a practice or skill was transmitted, interrupted or revived.

Do not widen the subject silently when evidence only supports a narrower statement.

## 3. Current state

A reader should be able to determine what the record currently says without reading the entire history first.

This normally includes:

- current status;
- observation or recording time where material;
- last material revision where useful;
- what the checked evidence presently supports;
- what the status does **not** establish.

A current status is a statement about this record at a bounded time, not a permanent property of the world.

`OBSERVED_AT != PERMANENTLY_CURRENT`

## 4. Evidence and source ancestry

A record should expose the evidence it relies on and the relationship between sources.

Where material, preserve:

- source identity and route;
- source kind;
- observation/fetch time;
- exact page/table/field/byte identity when available and useful;
- whether a source is primary, derivative, reported by another reviewer, or still uncertain;
- known derivation or repetition relationships;
- source-independence groups where multiple endpoints or copies share one underlying owner/ancestor.

Counting URLs is not counting witnesses.

```text
MULTIPLE_SOURCES != INDEPENDENT_SOURCES
REPETITION != CORROBORATION
SOURCE_LINK != SOURCE_PRESERVED
HASH != TRUTH
```

## 5. Findings

The record should separate what the checked evidence supports from interpretation that remains provisional.

A finding should be narrow enough that another reader can inspect the cited basis and disagree with it.

Where the record only establishes agreement with an institutional record, say that. Where it only reconstructs a visible propagation chain, say that. Where it only shows a public attention or transmission pathway, do not silently turn that into evidence that tacit skill itself was transmitted.

```text
EVIDENCE != INFERENCE
ATTENTION_PATHWAY != SKILL_TRANSMISSION
```

## 6. Unknowns and unexamined material

Unknowns are first-class record content.

A record should preserve:

- important unresolved questions;
- relevant sources, archives, people, objects or tests not examined;
- inaccessible or failed checks where they affect the result;
- uncertainty about source ancestry or independence;
- boundaries that would materially change the finding if stronger evidence appears.

```text
UNKNOWN != ABSENT
NOT_CHECKED != NEGATIVE_FINDING
INACCESSIBLE != NONEXISTENT
```

## 7. Corrections, challenges and disagreement

A record should be able to change without pretending the earlier state never existed.

For a material challenge or correction, preserve where practical:

- date received or made;
- who or what submitted it, as signed or publicly attributable;
- route to the challenge or review evidence;
- what was actually checked;
- disposition: accepted, partially accepted, declined, unresolved, superseded, or equivalent;
- exact change made;
- what remains unresolved;
- whether the original observation or evidence changed;
- whether the correction constitutes a fresh independent witness.

A rejected or unresolved challenge is not thereby disproved. Silence is not rejection.

`CORRECTED_RECORD != ORIGINAL_EVENT_CHANGED`

## 8. Rights, authority and custody

Where rights, community control, privacy, restricted knowledge or governance matter, the record must not turn technical custody into authority.

Preserve the relevant boundary between:

- rights in a work and rights in a reproduction;
- public evidence and restricted/community-held knowledge;
- ability to copy and authority to govern;
- contributor participation and stewardship;
- provenance labels and legal authorship determinations;
- public reporting about a living practitioner and that practitioner's participation or endorsement.

```text
RECORDING != OWNING
PRESERVATION != EXTRACTION
CUSTODY != GOVERNANCE
COMMUNITY_KNOWLEDGE != PUBLIC_DOMAIN
PUBLIC_SOURCE != ENDORSEMENT
CC0_GRANT != THIRD_PARTY_RIGHTS_GRANT
```

For living communities, practitioners or creators, consent and legitimate control can be part of the evidence structure rather than an obstacle to preservation. A public-source record can remain public-source only; recording practitioner-specific tacit knowledge can require a separate permission decision.

## 9. Human and machine routes

The Human Record is collaboratively built with AI but offered as a gift for humans.

A normal human should be able to understand the record without first opening raw JSON or repository history. A machine should be able to find the structured record without scraping the human presentation as its only source.

Each entry should therefore provide, where practical:

- a readable human view;
- the full human record;
- a machine-readable record;
- a correction/challenge route;
- the public source/history route.

The readable page is a view over the record, not a second evidence layer.

```text
HUMAN_VIEW != NEW_EVIDENCE
SUMMARY != SOURCE
AI_BUILT != AI_FACING_ONLY
```

## Type-specific extensions

Different record types may need very different additional structures.

Examples already present:

- the artwork specimen needs artefact identity, owner-source reconciliation, image-byte comparison, rights layers and selection provenance;
- the flak-claim case needs propagation nodes, claim relations, source ancestry, nearby-but-different evidence, research leads and unresolved origin hypotheses;
- the sieve-and-riddle case needs living-practice status with an explicit external status owner, selection/strongest-owner reasoning, lineage events, source-independence groups, authority/consent boundaries, and a separation between public attention pathways and actual skill transmission.

Future records involving oral history, audiovisual carriers, software-dependent works, living creators or community-held knowledge may require carrier condition, environment/dependency capture, consent, access restrictions, community authority, or other fields not earned by the current three records.

Do not add those fields globally until a real record requires them.

## Current field mapping

The three existing machine records do not use identical field names. That is acceptable if their semantics remain inspectable.

| Common question | Artwork specimen | Flak claim case | Sieve/riddle lineage case |
| --- | --- | --- | --- |
| identity/type | `format`, `artefact` | `record_type`, `record_version`, `title` | `record_type`, `record_version`, `title` |
| current state | `status`, observation fields | `status`, `historical_truth_status`, `recorded_at` | `status`, `living_practice_status`, `recorded_at` |
| evidence | `owner_sources`, `reconciliation` | `nodes`, `review_receipts` | `nodes`, `lineage_events` |
| source relationship | `epistemic_boundaries.source_independence` | node `role` / `claim_relation` | `source_independence` |
| findings | reconciliation + bounded prose | `current_findings` | `current_findings` |
| unknowns | `not_established`, epistemic boundaries | `unknowns`, `not_checked` | `unknowns`, `not_checked` |
| correction history | `corrections` | `challenges`, revision notes | Git history + future challenge entries; `correction_rule` defines current practice |
| rights / authority | `rights_layers`, epistemic boundaries | contribution/rights boundary in full record | `authority_and_consent` |
| correction route | `correction_route` | `correction_rule` + public contribution route | `correction_route`, `correction_rule` |

This table is a migration aid, not a command to rename mature fields merely for symmetry.

## Test for a new Human Record entry

Before adding a new record, ask:

```text
CAN A HUMAN TELL WHAT THIS RECORD IS ABOUT?
CAN THEY SEE WHAT IS KNOWN AND UNKNOWN?
CAN THEY WALK BACK TO THE EVIDENCE?
CAN THEY SEE WHICH SOURCES SHARE ONE ANCESTOR?
CAN THEY FIND WHAT WAS NOT CHECKED?
CAN THEY SEE HOW CHALLENGES CHANGED THE RECORD?
CAN THEY CHALLENGE IT WITHOUT ACCEPTING THE PROJECT?
ARE RIGHTS / CONSENT / CUSTODY BOUNDARIES HONEST?
CAN A MACHINE FIND THE SAME RECORD WITHOUT INVENTING MISSING STRUCTURE?
```

For a living practice, creator or community, add:

```text
DOES THE RECORD DISTINGUISH DOCUMENTATION FROM LIVING CONTINUATION?
DOES PUBLIC SOURCE USE AVOID IMPLYING ENDORSEMENT?
WOULD DEEPER RECORDING REQUIRE A SEPARATE CONSENT / AUTHORITY DECISION?
```

If not, improve the record before multiplying the collection.

## Current authority

The current public Human Record source is:

`https://github.com/markgoodbody-bit/human-record`

Earlier COM material remains useful build provenance and historical source lineage. It is not required as the operational correction or continuation surface for current Human Record entries.

Stewardship remains separately **offered to 1F916 / not accepted / not community-owned**. This contract does not alter that status.

```text
RECORDING != CONTINUATION
```
