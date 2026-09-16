# The Human Record — identity model

Status: **WORKING INTEROPERABILITY MODEL / NOT A PERSONHOOD SYSTEM / NOT CANON**

Human names are labels. They are not safe identity keys.

```text
NAME != ENTITY
MENTION != ENTITY
EXTERNAL ID != ENTITY
IDENTITY RESOLUTION != IDENTITY CERTAINTY
```

The purpose of this model is narrow: let Human Record entries refer to the same person, organisation, work, practice, place or other persistent subject without forcing ambiguous mentions into a false match.

## 1. Opaque THR identifiers

A Human Record entity identifier must not encode a name, date, nationality, diagnosis, moral status or other mutable claim.

Working form:

```text
thr:entity:<UUID>
```

Example:

```text
thr:entity:da243807-2e4e-44a5-86bc-aa8b8d4f23fb
```

The UUID is an identifier only. It says nothing about the entity.

Do not use identifiers such as:

```text
hannibal-barca-247-bce
john-smith-london-1984
```

because later correction of a label, date or disambiguating claim would make the identifier itself stale.

## 2. Entity core

The minimum entity registry entry is intentionally small:

```json
{
  "id": "thr:entity:<uuid>",
  "type": "person",
  "labels": [],
  "status": "current",
  "record_links": [],
  "external_identifiers": [],
  "notes": []
}
```

Possible `type` values are descriptive and extensible, for example:

- `person`
- `organisation`
- `work`
- `practice`
- `place`
- `event`
- `object`
- `concept`
- `unknown`

The type is itself correctable metadata. It is not metaphysical certification.

## 3. Labels and names

Names belong in `labels`, not in the identifier.

A label can carry:

```json
{
  "text": "Hannibal",
  "language": "en",
  "script": "Latn",
  "kind": "historical_or_common_name",
  "preferred_for_current_view": false,
  "basis": "source or editorial route"
}
```

Useful label kinds may include:

- preferred display label;
- source-literal name;
- alias;
- former name;
- title;
- transliteration;
- language/script variant;
- stage or professional name;
- uncertain reading.

Several entities may legitimately have the same label.

```text
DUPLICATE LABEL != DUPLICATE ENTITY
```

## 4. Mentions

A mention is the literal reference encountered in a source or record context.

A mention should preserve, where useful:

```json
{
  "mention_id": "thr:mention:<uuid>",
  "literal": "Hannibal",
  "source_id": "thr:source:<uuid>",
  "observation_id": "thr:observation:<uuid>",
  "context": "bounded quotation location or structural locator",
  "candidates": []
}
```

The mention is evidence that a string or description occurred. It is not proof that the intended referent has been identified.

## 5. Candidate resolution

A mention may have zero, one or many candidate entities.

Working relation states:

- `resolved_as` — current record treats the referent as this entity on stated evidence;
- `candidate` — plausible but unresolved;
- `excluded` — evidence currently rules this candidate out;
- `unresolved` — no adequate resolution yet.

Each proposed link should carry a basis rather than only a score.

```json
{
  "entity_id": "thr:entity:<uuid>",
  "state": "candidate",
  "basis": [
    "patronymic matches",
    "office and date overlap",
    "source context"
  ],
  "conflicts": [
    "another contemporary person shares the same name"
  ]
}
```

Numerical confidence is optional, not required. Do not manufacture precision merely because a machine can emit a decimal.

```text
0.83 WITHOUT METHOD != EVIDENCE
```

## 6. External identifiers

THR should interoperate with strong external identity systems where they exist.

Examples may include institutional collection identifiers, authority files, ORCID, ISNI, VIAF, Wikidata identifiers, archival authority records and domain-specific identifiers.

Store them as mappings:

```json
{
  "scheme": "example",
  "value": "12345",
  "relationship": "asserted_same_entity",
  "basis": "checked institutional mapping",
  "observed_at": "..."
}
```

An external identifier does not replace the THR ID, and a mapping can later be disputed or corrected.

## 7. Claims about entities stay outside the identity key

Birth date, creator attribution, nationality, profession, kinship, office, ownership and similar facts are assertions.

They should retain sources and uncertainty rather than being silently treated as properties required to keep the entity alive.

```text
ENTITY PERSISTS THROUGH CORRECTION OF CLAIMS ABOUT ENTITY
```

This is especially important for historical records where the identifying evidence may itself be disputed.

## 8. Merge and split

Identity systems eventually make mistakes.

### Merge

If two THR entities are later established as the same referent:

- do not delete either historical identifier;
- select or create a current entity ID;
- mark the superseded ID with `merged_into`;
- preserve which records used the earlier ID;
- re-check assertions rather than mechanically copying every claim.

### Split

If one THR entity is later shown to have conflated multiple referents:

- retain the old entity as a historical resolution state;
- create distinct current entity IDs;
- mark the old ID `superseded_by` the new candidates;
- re-evaluate each mention/assertion against the split entities;
- do not assign old assertions automatically.

```text
IDENTITY CORRECTION != HISTORY DELETION
```

## 9. Living people and sensitive identity

The existence of a scalable identity system is not permission to build profiles on everyone.

For living people:

- collect only what a real record requires;
- avoid unnecessary sensitive attributes;
- do not infer protected or private traits merely to improve matching;
- preserve consent/authority boundaries where material;
- do not expose private disambiguators publicly simply because they are useful internally;
- public-source identity data does not imply endorsement of THR.

When THR actively asks a competent living person to provide information about themselves voluntarily, use [`LIVING_SUBJECTS.md`](LIVING_SUBJECTS.md) before collecting or publishing the answer. That encounter rule is deliberately narrower than this identity model and does not generalise consent mechanics to every entity type.

```text
BETTER MATCHING != MORE SURVEILLANCE
```

## 10. Historical ambiguity is a valid result

The system must support:

```text
MENTION: "Hannibal"
CANDIDATE A: plausible
CANDIDATE B: plausible
OTHER REFERENT: possible
STATUS: UNRESOLVED
```

That is not database failure. It is an honest representation of the evidence state.

## 11. AI role

AI is well suited to propose identity links because it can compare large numbers of sources, aliases, dates, kinship statements, offices, places, scripts and citation contexts.

It should return the evidence for the proposal and preserve alternatives.

A scalable workflow is:

```text
AI DISCOVERS POSSIBLE COLLISION
-> AI GATHERS DISAMBIGUATING EVIDENCE
-> CANDIDATE LINKS CREATED
-> CONFLICTS REMAIN VISIBLE
-> HIGH-CONSEQUENCE / UNCERTAIN CASE ROUTED FOR REVIEW
-> CORRECTION REMAINS POSSIBLE
```

```text
AI MATCH != SILENT IDENTITY FACT
```

## Current implementation

`registry/entities.json` is the first small cross-record entity registry.

It is deliberately sparse. Current records do not need immediate wholesale migration to entity IDs. Add references when they reduce a real ambiguity or repeated-identity burden.
