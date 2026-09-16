# The Human Record — scale architecture

Status: **WORKING PRODUCT ARCHITECTURE / EARNED FROM CURRENT RECORDS / NOT A UNIVERSAL ONTOLOGY / NOT CANON**

The Human Record is beginning with a few inspectable records, but it should not require a human maintainer to hand-reconcile every name, URL, source version and readable page forever.

The scaling problem is not simply storage volume. It is preserving the distinctions that become easiest to lose when the collection becomes large.

```text
NAME != IDENTITY
MENTION != ENTITY
URL != SOURCE
SOURCE != OBSERVATION
OBSERVATION != PRESERVED COPY
PRESERVED COPY != TRUTH
ASSERTION != ENTITY
HUMAN VIEW != RECORD STATE
```

## Why this layer exists

Two ordinary facts force it.

1. Human names collide, change, transliterate, acquire titles, lose patronymics and are reused across families and centuries. A text string cannot safely be the identity key.
2. Web sources change, move and disappear. A URL is only a locator. It does not identify immutable content and it does not preserve what a record actually observed.

At small scale a careful reader can remember these problems. At large scale they must become explicit structure.

## The smallest scalable stack

```text
WORLD / HUMAN ACTIVITY
        |
        v
MENTIONS + SOURCE LOCATORS
        |
        v
TIMED OBSERVATIONS
        |
        +------> PRESERVATION ROUTES / COPIES
        |
        v
ENTITY CANDIDATES + ASSERTIONS
        |
        v
RECORD STATE + CORRECTION HISTORY
        |
        +------> MACHINE VIEW
        |
        +------> HUMAN VIEW
```

The stack is deliberately not one giant graph schema. Each layer answers a different question.

### Mention

What literal name, title, identifier or description appears in a particular source?

A mention can remain unresolved. It may point to one candidate entity, several candidates, or none yet.

### Entity

What persistent thing does THR currently mean to refer to across records?

An entity receives an opaque THR identifier. Its label can change without changing its identifier. External identifiers can be attached as mappings, not substituted for the THR identifier.

See `IDENTITY_MODEL.md`.

### Source

What logical publication, page, dataset, image, recording or other evidence object is being referred to?

A source receives an opaque THR identifier. Its URL is a locator, not the identifier.

### Observation

What did a particular observer actually retrieve or inspect, from which locator, at what time?

Where useful and lawful, preserve media type, byte count, digest, response metadata and the exact part of the source relied on.

### Preservation route

Where can the observed source state be recovered if the live locator later changes or disappears?

Possible owners include institutional archives, national web archives, Internet Archive, Perma-style citation archives, Software Heritage for source code, repositories, or a legitimate local copy where rights and authority permit one.

THR should prefer interoperability with stronger preservation owners over becoming a general-purpose shadow archive.

See `SOURCE_MODEL.md`.

### Assertion

What proposition is being made, by whom or by which source, about which entity, event or relationship?

Assertions remain evidence-bearing claims. They are not baked into entity identity merely because they are convenient labels.

### Record state

What does this Human Record entry currently conclude, what remains unknown, and how did corrections change it?

### Human / machine view

How is that state presented to a person or machine?

Views are derived surfaces. The current project already pins human views to the exact source-record bytes they summarize.

```text
DERIVED_VIEW != CURRENT_RECORD_UNLESS_BASIS_MATCHES
```

## Identity at scale

Human-readable names remain first-class because the gift is for humans, but names are not primary keys.

A scalable identity path is:

```text
SOURCE TEXT: "Hannibal"
-> MENTION ID
-> zero / one / many candidate entity IDs
-> evidence for each proposed resolution
-> RESOLVED / CANDIDATE / EXCLUDED / UNRESOLVED
```

Do not require numerical confidence merely to make a database field look precise. A system may record a probability when a real method or source supplies one, but ordinary THR identity resolution should preserve the evidence and categorical state.

A large collection must be able to say:

```text
THIS MENTION MAY REFER TO A OR B
WE DO NOT YET KNOW
```

without corrupting either entity.

## Source survival at scale

A scalable citation must not collapse to a bare URL.

The preferred shape is:

```text
SOURCE ID
-> locator(s)
-> observation(s)
-> content fingerprint(s), where available
-> source ancestry / citation relations
-> preservation status
-> external archive reference(s), where available
-> rights / access boundary
```

If the live site disappears, THR should still retain enough information to answer:

- what location was used;
- when it was observed;
- what part of it supported the record;
- whether exact bytes were fingerprinted;
- whether an archival copy exists;
- who owns that archival copy;
- what could not legally or ethically be copied.

```text
LINK ROT != EVIDENCE ERASURE
ARCHIVE COPY != SOURCE TRUTH
```

## AI's role

This architecture is intentionally suited to collaborative AI work.

At useful scale, artificial collaborators can repeatedly do work that is expensive for a human curator:

- discover candidate source relationships;
- compare names, aliases and transliterations;
- identify likely identity collisions;
- extract source claims while retaining exact context;
- detect proposition drift between derivative sources;
- fingerprint retrieved material;
- check whether live locators changed or failed;
- look for stronger preservation owners and archived states;
- propose entity matches without forcing them;
- detect duplicate or derivative evidence;
- regenerate human-readable views;
- run integrity checks across millions of relationships;
- surface ambiguous or consequential cases for human/community review.

That comparative advantage does not grant authority.

```text
AI CAN RECONCILE != AI MAY DECIDE IDENTITY WITHOUT EVIDENCE
AI CAN ARCHIVE != AI MAY COPY WITHOUT RIGHTS / AUTHORITY
AI CAN SUMMARIZE != AI MAY ERASE SOURCE AMBIGUITY
AI CAN SCALE REVIEW != AI BECOMES TRUTH AUTHORITY
```

## Storage architecture

Do not choose a heavyweight database because future scale sounds large.

The current public repository remains a valid small-system source of truth while the contracts are still changing. The durable requirement is that the public export remains inspectable and portable.

A future storage backend may be Git, object storage, a relational database, a graph store, content-addressed storage, or a combination. That implementation choice should not change the public semantics of entity IDs, source observations, assertions, corrections and views.

```text
STORAGE BACKEND != RECORD MEANING
```

## Incremental migration

Current records do not need to be rewritten all at once.

### Now

- keep the three existing record types intact;
- introduce identity and source models;
- introduce small cross-record registries;
- automate integrity checks;
- keep readable human pages;
- record preservation debt rather than inventing archive coverage.

### When real records require it

- attach source IDs to record evidence nodes;
- attach entity IDs to unambiguous record subjects;
- create mention objects where identity is ambiguous;
- preserve external archive references;
- generate more human views from structured state rather than hand-maintaining them.

### Only when load requires it

- partition registries;
- move mutable working state behind an API/database;
- run distributed preservation/currentness checks;
- maintain search indexes and caches;
- keep the public export and durable identifiers independent of one serving stack.

## Failure modes to resist

```text
DUPLICATE NAME -> FORCED MERGE
URL CHANGE -> SOURCE LOSS
MULTIPLE URLS -> FALSE INDEPENDENCE
ARCHIVE CAPTURE -> FALSE TRUTH UPGRADE
AI MATCH -> SILENT IDENTITY FACT
SCHEMA CONVENIENCE -> ERASED UNKNOWN
DATABASE MIGRATION -> BROKEN PUBLIC IDS
HUMAN INTERFACE -> DETACHED SUMMARY
SCALE -> LOSS OF CORRECTION HISTORY
```

## Current threshold

The Human Record does not yet need industrial infrastructure.

It does need to stop making assumptions that would make industrial scale dishonest later.

That is the purpose of this layer.
