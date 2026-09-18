# The Human Record — assertion model

Status: **WORKING INTEROPERABILITY MODEL / NOT A UNIVERSAL KNOWLEDGE GRAPH / NOT CANON**

Entity identifiers answer **what persistent referent are we talking about?**

Assertions answer **what is being said about that referent, by which evidence, at what scope and time?**

Keeping those separate prevents a convenient database field from becoming an unchallengeable identity fact.

```text
ENTITY != ASSERTION
ASSERTION != TRUTH
SOURCE STATEMENT != THR ENDORSEMENT
CURRENT RECORD FINDING != PERMANENT WORLD FACT
```

## 1. Opaque assertion identifiers

A cross-record assertion that needs durable reference can receive:

```text
thr:assertion:<UUID>
```

The ID says nothing about whether the assertion is true, false, disputed or current.

## 2. Minimum assertion envelope

A working assertion may look like:

```json
{
  "id": "thr:assertion:<uuid>",
  "subject": {"entity_id": "thr:entity:<uuid>"},
  "predicate": "creator_attribution",
  "object": {"entity_id": "thr:entity:<uuid>"},
  "state": "reported_by_source",
  "evidence": {
    "source_ids": ["thr:source:<uuid>"],
    "observation_ids": ["thr:observation:<uuid>"]
  },
  "scope": {},
  "record_links": [],
  "corrections": []
}
```

This is an envelope, not a mandatory universal triple grammar. Complex claims may remain in their record-specific structures until cross-record use actually requires an assertion object.

## 3. Subject and object

An assertion can refer to:

- an entity;
- another assertion;
- a record-local subject or claim;
- a bounded literal value;
- a date/range;
- a source-reported category;
- an unresolved referent.

Do not invent an entity merely because a field wants an object ID.

## 4. Assertion state

Working states should describe the evidence relationship rather than issue a universal truth verdict.

Examples:

- `observed` — the record directly observed the stated feature within a bounded observation;
- `reported_by_source` — a source states the proposition;
- `reconciled` — two bounded representations were compared and matched on stated terms;
- `inferred` — the proposition is an explicit inference from evidence;
- `disputed` — materially challenged with unresolved disagreement;
- `unsupported_in_sources_checked` — not supported by the bounded source set examined;
- `unknown` — the current record cannot establish the proposition;
- `superseded` — a later assertion state replaces it while history remains.

These are not a complete epistemology.

```text
STATE LABEL != UNIVERSAL TRUTH VALUE
```

## 4a. Direct-evidence implementation boundary

The source registry's current observation envelope records a bounded retrieval or
inspection of a source representation. It does **not** yet carry a typed relation
to the entity, observable situation, or proposition that a cross-record assertion
claims was directly observed.

This distinction is owned rather than invented here. CRMsci 3.2 gives an
observation explicit relations to what was observed, including observable
situations/entities/propositions. THR does not yet implement an equivalent typed
target relation.

Official owner reference:
https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v3.2.html

Until a concrete THR case earns and tests such a representation, the
cross-record assertion validator must fail closed on direct-evidence states that
would otherwise be asserted by changing only the state word.

Working direct-evidence states requiring typed target/reconciliation support:

- `observed`
- `reconciled`

`reported_by_source` remains appropriate where the record inspected a source
that states the proposition. A source retrieval/inspection observation is
evidence that THR inspected the representation at a bounded time and scope; it
is not by itself evidence that THR directly observed the world-state described
inside that representation.

```text
SOURCE_OBSERVATION != DIRECT_WORLD_OBSERVATION
SOURCE_MEDIUM != OBSERVED_OBJECT
STATE_WORD != EVIDENCE_RELATION
FAIL_CLOSED_NOW != PERMANENT_SCHEMA_DECISION
```

This is an implementation boundary, not a claim that direct observation or
reconciliation can never be represented. A later repair should add the smallest
typed observation/reconciliation relation justified by real records and owner
semantics, then remove this temporary fail-closed guard with red-before /
green-after tests.

## 5. Scope is part of the assertion

Population, denominator, time window, place, version and other qualifiers can change the proposition materially.

The flak case demonstrates why this matters: “share of sampled Allied aircrew casualties caused by flak” is not the same assertion as “share of German flak crew members who died.”

Where material, preserve:

- population;
- denominator;
- time interval;
- geography;
- source version / observation time;
- unit or measure;
- whether the scope itself is uncertain.

```text
SAME NUMBER != SAME CLAIM
```

## 6. Evidence links

An assertion should point back to the evidence that currently supports its state.

Prefer stable source/observation IDs over bare URLs where the registry already has them.

Evidence can include:

- source IDs;
- observation IDs;
- record-local node IDs;
- archival/preservation references;
- review or challenge receipts;
- exact table/page/field locators.

A source can support one part of an assertion and not another. Keep those boundaries visible.

For registry integrity, every evidence observation must belong to a source named
in that assertion's evidence `source_ids`. Multiple sources and observations are
allowed; citing a source without an observation remains allowed. This ownership
check prevents mismatched references, not misinterpretation of source content.

One assertion state is intentionally stricter:

`unsupported_in_sources_checked` means a bounded source set was actually
examined. It therefore requires a non-empty evidence source set and at least one
owned **inspected** observation for every source counted as checked. An empty list
cannot support that state. In the current structural implementation,
`retrieved`, `partial`, and `reported_by_reviewer` observations can witness a
checked source; `metadata_only`, `not_retrieved`, `failed`,
`access_restricted`, and citation-only/open-vocabulary outcomes cannot.

This is still a structural proxy rather than claim-level semantic proof. The
observation scope must remain inspectable, and a later typed claim-inspection
model may narrow this further.

This structural rule still does **not** make the checked set exhaustive. The
record should preserve the selection/search boundary and material unexamined
sources where they affect interpretation. Mature systematic-review reporting
owners such as PRISMA / PRISMA-S require detailed reporting of sources searched,
dates and search methods for claims that depend on search completeness. THR does
not inherit that whole review schema; it borrows the narrower discipline that a
negative/unsupported finding must expose its bounded evidence aperture.

```text
SOURCES_CHECKED != ALL_POSSIBLE_SOURCES
EMPTY_CHECKED_SET != UNSUPPORTED_FINDING
NOT_FOUND_IN_BOUND != ABSENT_FROM_WORLD
```

## 7. Source statement versus record finding

THR must distinguish:

```text
SOURCE SAYS X
```

from:

```text
THR CURRENTLY FINDS X SUPPORTED
```

and from:

```text
THR CURRENTLY CANNOT ESTABLISH X
```

A source-reported status can therefore remain an assertion attributed to that source even if THR does not independently verify the underlying world state.

## 8. Corrections

Assertions should change without deleting earlier states.

A correction may:

- narrow scope;
- replace an object/value;
- change evidence state;
- attach stronger evidence;
- detach a source shown to be derivative;
- move an assertion to a different entity after identity correction;
- split one assertion into several scoped assertions.

Preserve the earlier assertion ID/state or a durable supersession relation where practical.

```text
CORRECTION != RETROACTIVE ORIGINAL CERTAINTY
```

## 9. Identity corrections do not blindly move assertions

If two entities are merged or one entity is split, every assertion attached to the old identity must be re-evaluated.

Do not automatically copy all properties from a merged/split entity to the replacement identities.

```text
ENTITY MERGE != ASSERTION MERGE
ENTITY SPLIT != AUTOMATIC CLAIM DISTRIBUTION
```

## 10. AI role

AI can extract candidate assertions from large source sets, compare propositions, notice changed scope, attach source ancestry and detect contradictions.

The scalable path is:

```text
AI EXTRACTS CANDIDATE PROPOSITION
-> SOURCE / OBSERVATION ATTACHED
-> SCOPE PRESERVED
-> IDENTITY CANDIDATES KEPT SEPARATE
-> RECORD-SPECIFIC CHECKS APPLIED
-> ASSERTION STATE MADE INSPECTABLE
-> CORRECTION REMAINS OPEN
```

```text
EXTRACTION != ENDORSEMENT
CONTRADICTION DETECTION != ADJUDICATION
```

## Current implementation

`registry/assertions.json` contains only a few cross-record examples already earned by the current records.

It is intentionally sparse. Do not atomize every sentence into assertions merely because automation can.

```text
CROSS-RECORD NEED -> ASSERTION OBJECT
NO CROSS-RECORD NEED -> RECORD-LOCAL STRUCTURE MAY BE ENOUGH
```
