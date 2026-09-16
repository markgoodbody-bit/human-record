# Human Record registries

Status: **WORKING CROSS-RECORD INDEX / NOT A DATABASE OF EVERYONE / NOT CANON**

This directory holds small cross-record registries needed when the same source or subject can appear in more than one Human Record entry.

Current files:

- `entities.json` — opaque identifiers for persistent subjects already useful across the current collection;
- `sources.json` — opaque identifiers for evidence sources, their known locators, bounded observations, source relationships and preservation status.

The registries are indexes over evidence-bearing records. They do not replace those records.

```text
REGISTRY ENTRY != TRUTH CERTIFICATE
ENTITY ID != CLAIM ABOUT ENTITY
SOURCE ID != SOURCE AUTHENTICITY
URL != SOURCE ID
```

## Why registries exist

At three records, repeated identity and source references can be read manually.

At thousands or millions of records, that becomes dangerous:

- two people with one name can be silently merged;
- one person with several names can be silently split;
- derivative URLs can look like independent sources;
- one changing URL can stand in for several different observed states;
- a correction in one record can fail to propagate to other views.

Stable opaque IDs let relationships remain correctable without making names and URLs into primary keys.

## Growth rule

Do not populate the registries merely because an entity or URL exists.

Add an entry when at least one of these is true:

- it is already used by a Human Record entry and cross-record reference would be useful;
- identity ambiguity needs explicit handling;
- a source is shared or derivative across records;
- preservation/currentness needs to be tracked independently of one record;
- a correction would otherwise require finding the same object by brittle text matching.

```text
COMPREHENSIVE PURPOSE != COLLECT EVERYTHING NOW
```

## Sensitive material

A public registry must not expose private or restricted identifiers merely to improve machine reconciliation.

For living people and community-held knowledge, follow `IDENTITY_MODEL.md`, `SOURCE_MODEL.md` and `SELECTION.md`.

## Validation

Run:

```bash
python tools/validate_integrity.py
```

The validator currently checks:

- catalogue JSON and record-ID uniqueness;
- exact human-view source-blob pins;
- local human/machine record routes;
- opaque entity/source/observation ID shape and uniqueness;
- basic registry structure;
- registry `used_by_records` references against the current catalogue.

It intentionally does **not** decide whether an entity match or source claim is true.
