# Human Record registries

Status: **WORKING CROSS-RECORD INDEX / NOT A DATABASE OF EVERYONE / NOT CANON**

This directory holds small cross-record registries needed when the same source, subject, mention, maintenance check or evidence-bearing assertion can appear in more than one Human Record entry.

Current files:

- `entities.json` — opaque identifiers for persistent subjects already useful across the current collection;
- `mentions.json` — literal source mentions and their current resolution state, including unresolved/not-required cases;
- `sources.json` — opaque identifiers for evidence sources, their known locators, bounded observations, source relationships and preservation status;
- `source-checks.json` — append-only operational receipts for locator/currentness checks that do not silently become record evidence;
- `assertions.json` — sparse evidence-bearing propositions that need durable cross-record reference without becoming properties baked into entity identity.

The registries are indexes over evidence-bearing records. They do not replace those records.

```text
REGISTRY ENTRY != TRUTH CERTIFICATE
MENTION != ENTITY
MENTION EXISTS != ENTITY PROFILE REQUIRED
ENTITY ID != CLAIM ABOUT ENTITY
SOURCE ID != SOURCE AUTHENTICITY
SOURCE CHECK != RECORD EVIDENCE
LIVE TODAY != PRESERVED
ASSERTION != TRUTH
URL != SOURCE ID
```

## Why registries exist

At three records, repeated identity and source references can be read manually.

At thousands or millions of records, that becomes dangerous:

- two people with one name can be silently merged;
- one person with several names can be silently split;
- a literal mention can be converted into a profile merely because a machine can resolve it;
- derivative URLs can look like independent sources;
- one changing URL can stand in for several different observed states;
- a routine currentness check can silently become evidence if maintenance and record observations are not separated;
- a source statement can be silently baked into an entity as though it were identity;
- a correction in one record can fail to propagate to other views.

Stable opaque IDs and explicit event/mention state let relationships remain correctable without making names, URLs or current claims into primary keys.

## Growth rule

Do not populate the registries merely because an entity, URL or extractable proposition exists.

Add an entry when at least one of these is true:

- it is already used by a Human Record entry and cross-record reference would be useful;
- identity ambiguity needs explicit handling;
- a source-literal mention must remain distinct from its proposed referent;
- a source is shared or derivative across records;
- preservation/currentness needs to be tracked independently of one record;
- an assertion needs stable evidence/scope/correction across records;
- a correction would otherwise require finding the same object by brittle text matching.

```text
COMPREHENSIVE PURPOSE != COLLECT EVERYTHING NOW
CROSS-RECORD NEED -> SHARED OBJECT
NO CROSS-RECORD NEED -> RECORD-LOCAL STRUCTURE MAY BE ENOUGH
```

## Mentions and living people

A mention is cheap to preserve; an entity profile is a stronger act.

The current registry deliberately includes a public mention of Mike Turnock without creating a living-person entity because the sieve/riddle record does not currently need cross-record person resolution. That boundary is part of the scale design, not missing data.

```text
PUBLIC NAME != ENDORSEMENT
BETTER MATCHING != MORE SURVEILLANCE
```

## Source checks

`source-checks.json` is an operational ledger, not a second evidence registry.

A check may establish that a locator was retrievable, failed, redirected or was access-restricted. Unless a check is explicitly promoted into a record observation with its own evidence basis, it does not alter the evidence state of a Human Record entry.

```text
RETRIEVED AGAIN != UNCHANGED
NO COMPARABLE DIGEST != CONTENT MATCH
FAILED CHECK != SOURCE NEVER EXISTED
CHECK RECEIPT != PRESERVATION ACTION
```

## Sensitive material

A public registry must not expose private or restricted identifiers merely to improve machine reconciliation.

For living people and community-held knowledge, follow `IDENTITY_MODEL.md`, `SOURCE_MODEL.md`, `ASSERTION_MODEL.md` and `SELECTION.md`.

## Validation

Run:

```bash
python tools/validate_all.py
python -m unittest discover -s tools -p 'test_validate*.py'
```

The single command runs both validators and exits nonzero if either fails or cannot complete. An optional checkout path selects the same target for both: `python tools/validate_all.py /path/to/checkout`. Warnings remain visible; the command does not fetch sources or edit data.

The structural validator checks catalogue/view pins and entity/source/observation/assertion relationships. The operational validator checks mention/entity/source/observation references, resolution-state coherence and source-check/source relationships.

Neither validator decides whether an entity match, source claim, assertion, currentness result or preservation route is true.
