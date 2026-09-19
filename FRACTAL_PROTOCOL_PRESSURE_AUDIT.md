# The Human Record — protocol-pressure implementation audit

Status: **HOSTILE BOUNDARY REPAIR / CURRENT-REPOSITORY EVIDENCE / NOT CANON**

Date: 19 September 2026

Question:

> Is the current RFC claim "THR protocol not earned" too broad?

Answer:

~~~text
YES — WORDING TOO BROAD

UNIVERSAL THR RECORD / KNOWLEDGE PROTOCOL = NOT EARNED

BOUNDED TASK-SPECIFIC EXCHANGE CONTRACTS
= CAN BE EARNED BY REAL USE
~~~

The existing contribution packet is the counterexample.

---

## 1. Existing object

Current public THR main already contains:

- `CONTRIBUTION_PACKET.md`
- `contribution-packet.schema.json`
- `examples/grok-flak-relay.packet.json`
- `examples/direct-no-delta.packet.json`

The schema has a stable format identifier:

`human-record-contribution-packet/0.1`

and ten required top-level keys.

The guide explicitly describes it as:

~~~text
OPTIONAL RELAY FORMAT
NOT A SUBMISSION SERVICE
NOT IDENTITY PROOF
NOT EVIDENCE ACCEPTANCE
~~~

This is a bounded exchange contract.

Whether one calls it a "protocol", "format" or "envelope" is less important than the
mechanical fact:

> independent sender / relay / receiver roles need a shared machine-readable contract so
> attribution, unknowns, source-check state and public-sharing boundaries are not silently
> lost in transport.

---

## 2. Why it was earned

The packet did not arise from speculative scale.

It arose from a real failure mode:

~~~text
ORIGINAL CONTRIBUTOR
-> CANNOT POST DIRECTLY
-> HUMAN / OTHER APERTURE RELAYS CONTRIBUTION
-> CONTEXT CAN BE LOST / REWRITTEN
~~~

The packet preserves:

- target;
- declared contributor;
- relay provenance;
- proposed contribution;
- reported evidence checks;
- unknowns;
- not-checked material;
- rights/privacy boundary;
- authentication ceiling.

That is exactly the kind of **specific consequential gap -> smallest help** that the
project's middle-out rule should permit.

The real Grok flak packet proves this is not merely hypothetical.

---

## 3. What this counterexample does not earn

The contribution packet does **not** imply:

- one universal THR record schema;
- a THR event/process ontology;
- a network resolver;
- a federation protocol;
- a preservation consensus layer;
- one wire format for all Human Record entries;
- automated acceptance of contributions;
- authenticated identity;
- protocol adoption outside this project.

Preserve:

~~~text
ONE BOUNDED EXCHANGE FORMAT
!= UNIVERSAL THR PROTOCOL

MACHINE-CHECKABLE ENVELOPE
!= NETWORK SERVICE

VALID PACKET
!= VALID CLAIM
~~~

---

## 4. Revised protocol boundary

The architecture should distinguish at least three layers:

### A. Record interoperability contract

Current `RECORD_CONTRACT.md`.

Purpose:
common questions / minimum semantics across heterogeneous record types.

~~~text
COMMON QUESTIONS != IDENTICAL OBJECTS
~~~

This is not a universal wire schema.

### B. Bounded task-specific exchange contracts

Example:
`human-record-contribution-packet/0.1`

These can be earned where transport between roles would otherwise lose consequential
meaning.

Other future examples could be:
- a bounded correction-challenge envelope;
- an export manifest;
- an independent witness receipt.

But only if real use earns them.

### C. Universal THR network / record protocol

Not currently earned.

A universal protocol would require real multi-implementation exchange pressure that
cannot be handled by:
- existing record formats;
- application/profile mappings;
- ordinary web/file conventions;
- stronger-owner standards;
- narrow task-specific contracts.

---

## 5. Architectural correction

Replace:

~~~text
THR PROTOCOL = NOT EARNED
~~~

with the more exact:

~~~text
UNIVERSAL THR RECORD / KNOWLEDGE PROTOCOL = NOT EARNED

BOUNDED TASK-SPECIFIC EXCHANGE CONTRACT
-> MAY BE EARNED BY A REAL TRANSPORT / HANDOFF GAP

CURRENT EXAMPLE
-> CONTRIBUTION PACKET 0.1
~~~

This preserves the zero-new-shared-core-types result.

The contribution packet does not require a new core entity/source/assertion type.

It is a **transport envelope over existing meanings**.

---

## 6. New falsifier

Ask of any proposed new format/protocol:

~~~text
WHAT REAL HANDOFF IS LOSING MATERIAL MEANING?

WHO ARE THE DISTINCT SENDER / RECEIVER / RELAY ROLES?

WHICH EXACT INFORMATION IS BEING LOST?

CAN AN EXISTING STANDARD OR SIMPLE FILE FORMAT CARRY IT?

IS A VERSIONED CONTRACT ACTUALLY NECESSARY?

CAN IT REMAIN OPTIONAL?

WHAT DOES VALIDATION NOT ESTABLISH?
~~~

If those questions do not expose a concrete loss:

~~~text
NO FORMAT / PROTOCOL BY MOMENTUM
~~~

---

## 7. Result

~~~text
ZERO NEW SHARED CORE TYPES = STILL SURVIVES

NO UNIVERSAL THR RECORD PROTOCOL = STILL SURVIVES

NO THR PROTOCOL PRESSURE AT ALL = FALSIFIED

BOUNDED TASK-SPECIFIC CONTRACTS
= ALREADY EARNED IN ONE REAL CASE
~~~

This is a useful correction.

The architecture can stay small without pretending all interoperability is prose-only.
