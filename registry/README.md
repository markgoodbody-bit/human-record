# Human Record registries

Status: **WORKING CROSS-RECORD INDEX / NOT A DATABASE OF EVERYONE / NOT CANON**

This directory holds small cross-record registries needed when the same source, subject or evidence-bearing assertion can appear in more than one Human Record entry.

Current files:

- `entities.json` — opaque identifiers for persistent subjects already useful across the current collection;
- `sources.json` — opaque identifiers for evidence sources, their known locators, bounded observations, source relationships and preservation status;
- `assertions.json` — sparse evidence-bearing propositions that need durable cross-record reference without becoming properties baked into entity identity.

The registries are indexes over evidence-bearing records. They do not replace those records.

```text
REGISTRY ENTRY != TRUTH CERTIFICATE
ENTITY ID != CLAIM ABOUT ENTITY
SOURCE ID != SOURCE AUTHENTICITY
ASSERTION != TRUTH
URL != SOURCE ID
```

## Why registries exist

At three records, repeated identity and source references can be read manually.

At thousands or millions of records, that becomes dangerous:

- two people with one name can be silently merged;
- one person with several names can be silently split;
- derivative URLs can look like independent sources;
- one changing URL can stand in for several different observed states;
- a source statement can be silently baked into an entity as though it were identity;
- a correction in one record can fail to propagate to other views.

Stable opaque IDs let relationships remain correctable without making names, URLs or current claims into primary keys.

## Growth rule

Do not populate the registries merely because an entity, URL or extractable proposition exists.

Add an entry when at least one of these is true:

- it is already used by a Human Record entry and cross-record reference would be useful;
- identity ambiguity needs explicit handling;
- a source is shared or derivative across records;
- preservation/currentness needs to be tracked independently of one record;
- an assertion needs stable evidence/scope/correction across records;
- a correction would otherwise require finding the same object by brittle text matching.

```text
COMPREHENSIVE PURPOSE != COLLECT EVERYTHING NOW
CROSS-RECORD NEED -> SHARED OBJECT
NO CROSS-RECORD NEED -> RECORD-LOCAL STRUCTURE MAY BE ENOUGH
```

## Sensitive material

A public registry must not expose private or restricted identifiers merely to improve machine reconciliation.

For living people and community-held knowledge, follow `IDENTITY_MODEL.md`, `SOURCE_MODEL.md`, `ASSERTION_MODEL.md` and `SELECTION.md`.

## Validation

Run:

```bash
python tools/validate_integrity.py
```

The validator currently checks:

- catalogue JSON and record-ID uniqueness;
- exact human-view source-blob pins;
- local human/machine/model/registry routes;
- opaque entity/source/observation/assertion ID shape and uniqueness;
- basic registry structure;
- entity/source/observation references inside assertions;
- registry `used_by_records` references against the current catalogue;
- source-relation targets against the source registry.

It intentionally does **not** decide whether an entity match, source claim or assertion is true.
