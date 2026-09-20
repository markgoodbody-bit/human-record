# The Human Record — zero-new-types implementation audit

Status: **IMPLEMENTATION AUDIT / CURRENT-REPOSITORY EVIDENCE / NOT CANON / NO SCHEMA CHANGE**

Date: 19 September 2026

Purpose:

> Test whether the current public THR structures can route a material source change to
> affected assertions, records and human-view review without introducing a new shared
> dependency/correction type.

This audit uses live `main` objects from the current four-record public baseline.

It does not mutate those records.

---

## 1. Existing route shape

The current implementation already contains these joins:

~~~text
SOURCE
-> OBSERVATION
-> ASSERTION.evidence.source_ids / observation_ids
-> ASSERTION.record_links
-> RECORD FILES
-> records/catalog.json
-> HUMAN VIEW + VIEW BASIS
~~~

This is enough to answer a bounded impact question:

> If this evidence source materially changes, which current THR assertions and public
> record surfaces need re-examination?

The result is a review route, not an automatic correction.

~~~text
DEPENDENCY FOUND
-> REVIEW REQUIRED

DEPENDENCY FOUND
!= DESCENDANT FALSE
~~~

---

## 2. Real single-assertion route — Heritage Crafts status

Current assertion:

`thr:assertion:5a39064c-4cd4-4d41-92e5-dff7f38799ea`

Predicate:

`current_craft_status`

Current object:

`critically endangered`

Evidence source:

`thr:source:2790ee98-28a4-4fca-bd80-b5b5484c47ef`

Source:
Heritage Crafts — "Sieve and riddle making"

Bounded observation:

`thr:observation:9b4e00c3-7803-4ee7-9392-b1a3b0a642e0`

Assertion record links:

- `cases/sieve-riddle-revival.json`
- `cases/sieve-riddle-revival.md`

Catalogue route:

`sieve-riddle-revival`

Human view:

`records/sieve-riddle-revival.html`

The catalogue pins the human view to exact source-record blobs.

Therefore a material new Heritage Crafts status does **not** require a new dependency
object to find the present review surface.

The existing path is:

~~~text
HERITAGE CRAFTS SOURCE
-> CURRENT STATUS ASSERTION
-> SIEVE/RIDDLE RECORD FILES
-> CATALOGUE ENTRY
-> HUMAN VIEW REVIEW
~~~

Important ceiling:

the current `source-checks.json` entry for this source is operational currentness
evidence only and explicitly says it was **not promoted into record evidence**.

So:

~~~text
SOURCE CHECK CHANGED
!= ASSERTION CHANGED

FRESH SOURCE OBSERVATION / CORRECTION
-> MAY TRIGGER ASSERTION + RECORD REVIEW
~~~

This preserves the maintenance/evidence boundary.

---

## 3. Real one-source / four-assertion fan-out — Polybius

Source:

`thr:source:7a1b2e15-a9b2-4af4-9e0b-2c44b10eb9d2`

Title:
"Polybius, Histories Book 3 — LacusCurtius/Thayer"

Current bounded observation:

`thr:observation:1ea96911-3e2c-42f8-b55e-63b45a9ad2d0`

The observation is explicitly partial and covers four cited passages.

That one source currently supports four different assertions:

1. `thr:assertion:72388414-cbc8-47b2-99af-51b639b14472`
   - `reported_source_evaluation`
   - Polybius' dismissal of Sosylus and Chaereas

2. `thr:assertion:3e38d580-5c88-463c-8a3a-9eeab8074fea`
   - `reported_documentary_source`
   - Polybius' report of the bronze tablet / troop lists

3. `thr:assertion:de8cb921-d655-46ba-8543-6ad14f6249ca`
   - `reported_investigative_method`
   - Polybius' claimed inquiry / inspection / Alpine crossing

4. `thr:assertion:ace95214-7288-414b-9982-78c65cfdf088`
   - `reported_alpine_crossing`
   - the attributed report that Hannibal crossed the Alps into Italy

All four already point to:

- `cases/hannibal-barca.json`
- `cases/hannibal-barca.md`

The catalogue then identifies:

- record: `hannibal-source-survival`
- human view: `records/hannibal.html`
- exact view-basis blobs

Therefore the current implementation already supports a real one-to-many impact query:

~~~text
ONE SOURCE CHANGED
-> FOUR ASSERTIONS REQUIRE REVIEW
-> ONE RECORD PAIR REQUIRES REVIEW
-> ONE HUMAN VIEW FRESHNESS MAY NEED RE-ESTABLISHMENT
~~~

No new `thr:dependency`, `thr:impact` or `thr:correction-propagation` object is needed
for this current specimen.

---

## 4. What this does not prove

The current public four-record corpus does **not** contain a source whose
`used_by_records` spans multiple public Human Record entries.

Likewise, the current assertion registry does not yet exercise:

~~~text
ONE CHANGED SOURCE
-> ASSERTIONS IN RECORD A
-> ASSERTIONS IN RECORD B
-> TWO INDEPENDENT HUMAN VIEW REVIEW ROUTES
~~~

So:

~~~text
INTRA-RECORD FAN-OUT TESTED
MULTI-RECORD FAN-OUT NOT YET TESTED
~~~

The zero-new-shared-types result therefore survives the current corpus but should not be
misreported as proof that future cross-record fan-out will never expose a missing
relation.

A future real shared source or assertion is the correct pressure test.

Do **not** manufacture one solely for architecture testing.

---

## 5. Protocol pressure result

Nothing in these two real routes requires a new wire protocol.

Current routing is discoverable from ordinary inspectable files:

- JSON registries;
- record files;
- catalogue;
- Git blob identities;
- public URLs.

A second independent implementation could consume those published surfaces or a future
bounded export/profile without requiring THR to own a transport protocol now.

Current result:

~~~text
CURRENT IMPACT ROUTING
= QUERY OVER EXISTING PUBLIC RELATIONS

NOT
= NEW PROTOCOL REQUIRED
~~~

This does not prove a protocol can never be earned.

Protocol pressure remains absent until a real multi-implementation exchange requirement
cannot be handled by existing formats / mappings / profiles.

---

## 6. Small implementation observation

The registry README currently says:

> a correction in one record can fail to propagate to other views.

After the residue attack, the more exact architectural wording is:

~~~text
A MATERIAL CORRECTION CAN FAIL TO REACH AFFECTED DEPENDENTS
~~~

"Propagate" can sound like automatic state inheritance.

The intended operation is review routing.

No public-main wording change is made by this RFC branch; the observation is preserved
for later correction only if the RFC is adopted or a real operational defect appears.

---

## 7. Current verdict

~~~text
SINGLE ASSERTION IMPACT ROUTE = PRESENT
ONE SOURCE -> FOUR ASSERTIONS = PRESENT
ASSERTION -> RECORD LINKS = PRESENT
RECORD -> HUMAN VIEW BASIS = PRESENT

INTRA-RECORD FAN-OUT = TESTED
MULTI-RECORD SOURCE FAN-OUT = NOT YET PRESENT / NOT TESTED

NEW SHARED DEPENDENCY TYPE = NOT EARNED
NEW CORRECTION-PROPAGATION TYPE = NOT EARNED
NEW THR PROTOCOL = NOT EARNED

ZERO-NEW-SHARED-TYPES RESULT
= SURVIVES CURRENT IMPLEMENTATION AUDIT
  WITH MULTI-RECORD FAN-OUT CEILING
~~~

Next real falsifier:

> a genuine source/assertion reused across two or more public records whose material
> correction cannot be routed correctly using the current sparse relations.


---

## 8. Independent registry audit — direct-route union requirement

Codex review comment `5744972035` audited the public registry state pinned to:

`1f5a5919938f385f43f1e2383bdfbb52807b206e`

It queried:
- all **20 registered sources**;
- all **8 registered assertions**;
- assertion `record_links`;
- the four public catalogue entries.

It independently confirmed:
- the Polybius source reaches four assertions and one Hannibal record/view;
- no current source spans multiple public records;
- **11 of 20 sources have no assertion evidence edge**, despite each carrying a direct
  `used_by_records` route.

That exposes an important implementation rule:

~~~text
SOURCE IMPACT ROUTING
=
DIRECT source.used_by_records
UNION
ASSERTION-DERIVED record_links
~~~

Do not implement:

~~~text
SOURCE
-> ASSERTION ONLY
-> RECORD
~~~

because:

~~~text
NO ASSERTION EDGE
!=
NO RECORD DEPENDENCY
~~~

The 11 current direct-only sources are not defects. They are evidence that THR deliberately
does not globalise every record-local claim into the assertion registry.

Therefore the correct response is **not** to manufacture assertions for those sources.

---

## 9. Small executable safeguard

The RFC branch now includes:

- `tools/impact_routes.py`
- `tools/test_validate_impact_routes.py`

The tool is a read-only derived query.

For one registered source it returns:
- direct `used_by_records` routes;
- assertion-derived record routes;
- their union as affected review candidates;
- unresolved assertion record links;
- unresolved direct record IDs.

It does not mutate:
- source state;
- assertion state;
- record status;
- human-view freshness.

Ceilings:

~~~text
AFFECTED_RECORD != FALSE_RECORD
REVIEW_ROUTE != CORRECTION
NO_ASSERTION_EDGE != NO_RECORD_DEPENDENCY
ROUTE_DERIVED != COMPLETE_DEPENDENCY_PROOF
~~~

The tests cover:
1. direct-only route survives without any assertion edge;
2. unresolved direct record IDs remain visible;
3. assertion route can add a second affected record;
4. direct + assertion routes deduplicate;
5. assertion-only source can still route to a record;
6. unresolved assertion record link remains visible;
7. unknown source fails;
8. public URL / repository path normalisation resolves to the same catalogue record.

Hosted result at exact head
`bf68bf19b5ad9a81d9c3a22408bea291a00ebdaf`:

`Validate Human Record integrity — run 151 / 35466822817 — SUCCESS`

This is the first executable correction-impact routing check produced by the RFC.

It does **not** establish dependency completeness.

The current limit remains:

~~~text
CURRENT REGISTERED RELATIONS
-> REVIEW CANDIDATES

UNREGISTERED / IMPLICIT DEPENDENCY
-> MAY STILL BE MISSED
~~~

Codex explicitly did not exhaustively trace record-local prose, all ancestry relations or
implicit historical-source identity.

---

## 10. Architectural result after the audit

The new implementation evidence strengthens the narrow architecture while adding a
ceiling:

~~~text
NEW SHARED DEPENDENCY TYPE = NOT EARNED

DERIVED IMPACT QUERY = EARNED

DIRECT RECORD ROUTE
UNION
ASSERTION-DERIVED ROUTE
= CURRENT SMALLEST HELP
~~~

This is materially different from adding a dependency ontology.

The next pressure is not to store more edges by default.

It is to discover whether a **real material dependency** exists that cannot be recovered
from current direct routes, assertion evidence, record-local structures or stronger-owner
relations.


---

## 11. Record-local dependency ceiling — Homo Faber specimen

A direct audit of the four current machine records against `registry/sources.json` found
that not every consequential evidence locator is registered as a shared THR source.

Concrete current specimen:

`cases/sieve-riddle-revival.json`

contains record-local node:

`homo-faber-overthrow-interview`

with locator:

`https://2022.homofaber.com/en/discover/discover-steve-overthrow`

The node is a substantive published practitioner interview. The record currently uses it
for the bounded finding that Steve Overthrow reports learning partly from Mike Turnock.

It is also cited in a correction entry.

That locator is **not** currently represented by a shared `thr:source:<uuid>` entry.

This is not automatically a defect.

The current registry growth rule explicitly permits:

~~~text
NO CROSS-RECORD NEED
-> RECORD-LOCAL STRUCTURE MAY BE ENOUGH
~~~

Therefore the executable source-ID impact query has an honest scope:

~~~text
REGISTERED SOURCE
-> DERIVED IMPACT ROUTES AVAILABLE

RECORD-LOCAL SOURCE WITHOUT SHARED ID
-> NOT ADDRESSABLE BY source_id QUERY
-> RECORD-LOCAL REVIEW ROUTE STILL EXISTS
~~~

Do not infer:

~~~text
NOT IN SOURCE REGISTRY
-> NOT EVIDENCE

NOT QUERYABLE BY source_id
-> NO DEPENDENCY
~~~

### Why generic URL scraping is not the repair

The same audit also found unregistered URLs that are **not** evidence sources:
- correction/challenge receipts;
- GitHub review receipts;
- public correction routes;
- build/provenance routes.

Therefore:

~~~text
URL OCCURS IN RECORD
!=
SOURCE DEPENDENCY
~~~

A generic URL scraper would create false positives.

### Smallest future options

If a real operational need requires automated impact/currentness handling for this local
Homo Faber source, the project has two bounded options:

1. **Promote that source to the existing source registry**
   - only if repeated identity, currentness, preservation or cross-record routing earns it;
   - this uses an already-existing shared type.

2. **Use a record-type-specific adapter**
   - read the record-local source/node semantics;
   - emit review candidates without globalising the node.

Neither option currently earns a new global dependency/source type.

### Current ceiling

~~~text
REGISTERED-SOURCE IMPACT ROUTING = EXECUTABLE
ALL RECORD-LOCAL DEPENDENCY ROUTING = NOT YET GENERIC

SOURCE REGISTRY != COMPLETE EVIDENCE UNIVERSE
URL SCRAPE != SAFE DEPENDENCY GRAPH
~~~

This narrows the zero-new-types result rather than defeating it.


---

## 12. Independent code audit — four concrete repairs

Codex review comment `5745004069` audited the first executable helper at exact head:

`6c4eb7b774bbf3b96d866d7fe7545e8fffa2c521`

Verdict:

`REPAIR`

The direct-plus-assertion union was accepted as the right bounded operation, but four
helper-level defects were demonstrated with synthetic inputs.

### A. Foreign-origin false positive

First implementation stripped scheme/authority from any absolute URL.

Therefore:

~~~text
https://unrelated.example/cases/b.json
~~~

could falsely resolve to the same record as:

~~~text
https://thehumanrecord.net/cases/b.json
~~~

Repair:
- absolute URLs resolve only when scheme is exactly `https`;
- host is exactly `thehumanrecord.net`;
- credentials are absent;
- explicit port is absent;
- query and fragment are absent.

Foreign / unsupported absolute URLs remain unresolved.

~~~text
MATCHING PATH != SAME RESOURCE
ORIGIN IS MATERIAL IDENTITY
~~~

### B. Ambiguous catalogue path

First implementation used one path -> one record dictionary assignment.

Two catalogue records claiming the same path would silently leave whichever record was
processed last.

Repair:
- a path already owned by another record raises a clear error;
- repeated use of the same path within the same record is safe.

~~~text
AMBIGUOUS PATH OWNERSHIP
!=
CHOOSE BY ITERATION ORDER
~~~

### C. Malformed route containers

First implementation converted malformed `used_by_records` values such as a string to an
empty list. That could turn invalid dependency data into apparent absence.

Repair:
- present `used_by_records` must be a list of non-empty strings;
- present assertion `record_links` must be a list of non-empty strings;
- malformed values fail loudly;
- unknown but well-formed direct record IDs remain separately visible as unresolved.

~~~text
MALFORMED ROUTE
!=
NO ROUTE
~~~

### D. Query / fragment inconsistency

First implementation treated relative and absolute fragment-bearing paths differently.

Repair:
- both relative and canonical-public URL forms with query or fragment are unresolved;
- query/fragment are not stripped for convenience because they can alter resource
  identity.

~~~text
NORMALISATION
!=
ERASE IDENTITY-BEARING COMPONENTS
~~~

### Regression coverage

The focused impact-route suite now covers 15 tests including:
- direct-only route;
- unresolved direct record ID;
- malformed direct route container/items;
- assertion adds second record;
- route deduplication;
- assertion-only route;
- unresolved assertion record link;
- malformed assertion record-link container/items;
- unknown source;
- canonical public URL + repo-path equivalence;
- foreign-origin rejection;
- credentials / explicit port / wrong scheme rejection;
- consistent query / fragment policy;
- duplicate catalogue-path rejection;
- repeated same-record path acceptance.

Exact repaired head:

`e9ee7f4c5692f066ea9da5338bdae3ab1ecb8303`

Hosted:

`Validate Human Record integrity — run 154 / 35467002565 — SUCCESS`

This green run establishes structural/test success only.

A semantic re-audit remains useful.



---

## 13. Current-registry smoke test

After the hostile synthetic repairs, two tests were added against the actual repository
state inherited from public `main`.

They check:

1. every current catalogue `full_human_record`, `machine_record` and `human_view`
   route is accepted by the strict path policy and maps back to the correct record ID;

2. every current registered source can be queried without losing any valid direct
   `used_by_records` route.

These are not frozen-count tests. They test the invariant against whatever valid current
registry/catalogue state the branch contains.

Exact code/test head:

`2e27a692aa4761ff6e25ff8c4ba3451956b4da9e`

Hosted:

`Validate Human Record integrity — run 156 / 35467203748 — SUCCESS`

The focused impact-routing suite therefore has **17 tests** at this point:
- 15 hostile/unit cases;
- 2 current-registry smoke tests.

Result:

~~~text
STRICT PATH / ROUTE HARDENING
!= CURRENT PUBLIC ROUTE BREAKAGE
~~~

within the scope exercised by the current catalogue and registered direct source routes.

This still does not establish:
- complete implicit dependency coverage;
- record-local source coverage;
- source-ancestry propagation completeness;
- multi-record fan-out behavior.



---

## 14. Framework recheck — malformed assertion source route

A bounded follow-up re-read tested malformed assertion evidence handling beyond the
earlier route/path repairs.

The predecessor helper at `d5621c7e701825bfd743b823aa1c97b352dec7cb` already checked:

~~~python
if not isinstance(evidence, dict):
    continue
source_ids = evidence.get("source_ids")
if not isinstance(source_ids, list) or source_id not in source_ids:
    continue
~~~

Therefore the earlier description of a string `source_ids` value creating an
assertion-derived false-positive route was **incorrect**. A non-list `source_ids` value
was silently skipped.

The actual earned repair is narrower:

~~~text
MALFORMED PRESENT EVIDENCE
-> MUST NOT BECOME APPARENT ABSENCE
-> FAIL LOUD
~~~

Current helper behaviour:
- present assertion `evidence` must be an object;
- present `evidence.source_ids` must be a list of non-empty strings;
- malformed containers/items raise a clear input error;
- missing evidence still means no assertion-derived route.

Regression coverage includes:
- string / null / mixed-type / blank-item `source_ids`;
- non-object assertion `evidence`.

Preserve:

~~~text
SILENT SKIP OF MALFORMED DATA != FALSE-POSITIVE ROUTE
MALFORMED EVIDENCE ROUTE != VALID DEPENDENCY
FAIL LOUD != INVENT ABSENCE
CORRECTION HISTORY != PERMISSION TO DRAMATISE THE PRIOR DEFECT
~~~

No helper code change is made by this documentation correction, and no new stored
dependency type is earned.
