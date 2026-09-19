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
