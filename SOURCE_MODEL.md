# The Human Record — source and preservation model

Status: **WORKING INTEROPERABILITY MODEL / NOT A GENERAL WEB ARCHIVE / NOT CANON**

A URL is a locator. It is not a durable source identity and it does not freeze the content that was present when a Human Record entry relied on it.

```text
URL != SOURCE
SOURCE != OBSERVATION
OBSERVATION != PRESERVED COPY
PRESERVED COPY != TRUTH
SOURCE LINK != SOURCE PRESERVED
```

The purpose of this model is to let a future reader recover what THR actually saw and where stronger preservation copies may exist, without turning THR into a copy of the whole web.

## 1. Source identity

A logical source receives an opaque THR source ID:

```text
thr:source:<UUID>
```

The identifier does not encode the current URL, title, publisher or date.

A source can have multiple locators over time.

```json
{
  "id": "thr:source:<uuid>",
  "kind": "web_page",
  "title": "...",
  "publisher": "...",
  "locators": [],
  "observations": [],
  "relations": [],
  "preservation": {}
}
```

## 2. Locator

A locator tells a reader where a source may be found.

Possible locator schemes include:

- URL;
- DOI;
- ISBN / catalogue identifier;
- archival reference;
- institutional accession;
- Software Heritage persistent identifier;
- Perma or other archival link;
- local repository path where legitimate.

A locator may cease to work without the logical source ceasing to have existed.

```text
404 != NEVER EXISTED
URL REUSE != SAME CONTENT
```

## 3. Observation

An observation records a bounded retrieval or inspection event.

Working form:

```json
{
  "id": "thr:observation:<uuid>",
  "observed_at": "2026-09-16T12:34:56Z",
  "locator": "https://example.org/page",
  "outcome": "retrieved",
  "media_type": "text/html",
  "bytes": 12345,
  "digest": {
    "algorithm": "sha256",
    "value": "..."
  },
  "scope": "whole response body",
  "observer": "...",
  "notes": []
}
```

Not every historical or manually consulted source will have exact bytes. Record what was actually observed rather than inventing a fingerprint after the fact.

The current `registry/sources.json` observation envelope is deliberately about
the bounded retrieval/inspection of **this source representation**. Its
`scope`, `outcome`, observer and digest can say what part of the representation
was inspected and what happened during retrieval. They do not currently encode
a typed observable situation/proposition in the world described by the source.

CRMsci 3.2 is the stronger semantic owner for observations that explicitly bind
an observation to an observed entity/situation/proposition:
https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v3.2.html

Therefore a source observation ID must not be treated as sufficient structural
support for a cross-record assertion state of `observed` or `reconciled`.
Those states need an explicit typed observation/reconciliation relation that THR
does not yet implement.

```text
OBSERVED_SOURCE_REPRESENTATION != OBSERVED_WORLD_STATE
SCOPE_TEXT != TYPED_OBSERVATION_TARGET
```

Possible outcomes include:

- `retrieved`
- `partial`
- `metadata_only`
- `reported_by_reviewer`
- `not_retrieved`
- `failed`
- `access_restricted`

```text
FAILED_FETCH != SOURCE_GONE
```

## 4. Fingerprints

A content digest is useful for answering whether two observed byte streams are identical.

It does not answer:

- whether the source is authentic;
- whether the source is historically correct;
- whether the publisher had authority;
- whether the observed bytes are complete;
- whether two semantically equivalent representations have different bytes.

```text
HASH MATCH -> BYTE IDENTITY CLAIM
HASH MATCH != TRUTH
```

Where bytes cannot legitimately be retained, a digest can still preserve a limited fixity signal, subject to the same boundary.

## 5. Source ancestry and relationships

Different URLs may descend from one source.

A source that is real and retrievable at observation time may still have been
created **after** the claim it appears to support, including by the claimant or
answering system itself. Observation time therefore does not establish source
generation time, prior existence, or independence.

```text
SOURCE RETRIEVABLE AT T2 != SOURCE EXISTED BEFORE CLAIM AT T1
OBSERVED_AT != GENERATED_AT
PUBLIC URL != PREEXISTING EVIDENCE
CLAIMANT-CREATED SUPPORT != INDEPENDENT CORROBORATION
```

When source genesis is material, prefer established provenance semantics rather
than inventing THR-specific ontology. W3C PROV already provides relations such
as `prov:generatedAtTime`, `prov:wasGeneratedBy`, `prov:wasAttributedTo`,
`prov:wasDerivedFrom` and `prov:hadPrimarySource`. C2PA provides
asset-origin/action/ingredient provenance for media and other bound assets.

THR does not currently require these fields in `registry/sources.json`.
A concrete record may preserve a bounded generation/attribution fact in its
record-specific structure, or reference an external provenance object, when
that distinction changes whether evidence is genuinely antecedent or
independent.


Useful source relations may include:

- `cites`
- `quotes`
- `summarizes`
- `derives_from`
- `mirrors`
- `reposts`
- `transcodes`
- `machine_summarizes`
- `same_institutional_owner`
- `relation_unknown`

Relations should be evidence-bearing. Chronology or textual similarity alone should not silently become a direct-copying claim.

```text
MULTIPLE URLS != INDEPENDENT SOURCES
DIFFERENT PUBLISHERS != CLAIM-LEVEL INDEPENDENCE
```

## 6. Preservation state

Every source can carry a preservation block even when the honest state is that preservation has not yet been checked.

```json
{
  "status": "not_yet_checked",
  "copies": [],
  "rights_boundary": "...",
  "last_checked_at": null
}
```

Working preservation states:

- `not_yet_checked`
- `related_copy_observed`
- `external_archive_found`
- `institutional_preservation_route_identified`
- `multiple_preservation_routes`
- `restricted_archive`
- `capture_not_permitted_or_not_appropriate`
- `preservation_unknown`

These labels should describe what was actually established. For example, a project-hosted byte-identical copy can be `related_copy_observed` without making a legal conclusion that the copy is universally authorised or durable forever.

The state is about recoverability, not truth.

## 7. Stronger preservation owners

THR should interoperate rather than reproduce mature preservation infrastructure.

Examples of relevant patterns and owners include:

- general and national web archives for public web material;
- citation-preservation services such as Perma-style archives for cited pages;
- Memento-compatible archives for datetime-based access to prior web resource states;
- Software Heritage and SWHIDs for source code and software artefacts;
- institutional repositories, museums, libraries and archives for material already under durable custody;
- domain repositories for research data and specialist records.

For web captures, WARC is a common archival container and Memento provides a standard model for accessing prior resource states. THR does not need to replace either.

Useful public interoperability references:

- Memento / RFC 7089: https://www.rfc-editor.org/rfc/rfc7089
- Perma record/capture documentation: https://perma.cc/docs/perma-link-creation
- Software Heritage persistent identifiers: https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html

Those systems have their own scope, access, policy and durability boundaries. Referencing them is not a guarantee that a particular THR source is archived there.

A preservation reference should record enough to identify the external copy and its relationship to the observed source state.

```json
{
  "provider": "example archive",
  "kind": "memento",
  "persistent_locator": "...",
  "captured_at": "...",
  "access": "public",
  "relationship": "archive_capture_of_source_locator",
  "verified_against_observation": "not_checked"
}
```

## 8. Local preservation

THR should not default to downloading and republishing everything it cites.

Local retention may be appropriate when:

- the material is owned or licensed for that use;
- it is public-domain / openly licensed and the scope is clear;
- the source owner provides a preservation copy;
- a legitimate preservation exception or institutional route applies;
- the record itself is THR-owned material.

For third-party material, prefer source fingerprint + preservation-owner route when full copying would create legal, ethical, privacy or cultural-control problems.

```text
AT RISK != FREE TO COPY
PUBLICLY ACCESSIBLE != UNLIMITED REPUBLICATION RIGHT
PRESERVATION != EXTRACTION
```

## 9. Restricted or community-held material

Sometimes even revealing that material exists, where it is held, or who it is associated with can be sensitive.

A source registry may therefore need a public stub while the underlying locator, capture or description remains restricted.

Do not treat preservation architecture as an excuse to expose knowledge whose legitimate holders restrict it.

## 10. Drift and re-observation

A live locator should be re-observable without overwriting previous observations.

```text
SOURCE
  observation A @ T1 -> digest X
  observation B @ T2 -> digest Y
```

If X and Y differ, record the difference. Do not assume the cause.

Possible causes include legitimate update, personalization, region, content negotiation, replacement, compromise, redirect changes or capture error.

```text
CHANGED BYTES != KNOWN CAUSE
```

## 11. Link-rot response

When a locator stops resolving:

```text
LIVE LOCATOR FAILS
-> preserve failure observation
-> search known external identifiers / archives
-> inspect Memento / archive routes where appropriate
-> verify candidate archived copy against earlier fingerprints where possible
-> update preservation status
-> keep original locator and history
```

Do not erase the dead URL. Its failure is part of source history.

## 12. AI role

AI can make this tractable at scale by repeatedly:

- testing locators;
- fingerprinting successful observations;
- detecting changed content;
- finding archival copies;
- comparing archived copies with earlier fingerprints;
- extracting citation and derivation relations;
- grouping false source multiplicity;
- identifying sources at high disappearance risk;
- routing material to stronger preservation owners;
- surfacing rights/consent ambiguity rather than automatically copying.

The automation should produce receipts, not invisible maintenance.

## Current implementation

`registry/sources.json` is the first cross-record source registry.

It records current source identity and known observation/preservation state without claiming that every existing web source has already been archived.

Preservation debt is allowed to be explicit:

```text
NOT_YET_CHECKED != PRESERVED
```
