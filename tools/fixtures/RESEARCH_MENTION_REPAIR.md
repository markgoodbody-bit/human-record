# Source-anchored research mentions

17 September 2026. Bounded follow-up to Hannibal and JFK probes, not a new registry.

Before: every mention required an ID in the public catalogue, even when a source,
its observation and a bounded source location were available before publication.
Initial repair: the record link could be omitted under those three conditions. Explicit
unknown, null and malformed record links remain errors. Candidate/unresolved
states are preserved. No production registry or catalogue entries are changed.

Both original fixtures retain their invalid candidate record IDs to preserve the
negative witness. Additional tests omit that field in memory and accept the
source-anchored mentions without inventing public records or identity matches.

Hostile cases cover missing observation, foreign observation, unknown source,
blank/non-string context, and explicit invalid record IDs. The pre-repair run
failed seven assertions and raised two malformed-record type errors. The repair
also turns those two crashes into validation errors. Multi-source assertion
ownership tests from the previous repair remain in the suite.

Limitation: a non-blank context can still be wrong or meaningless. Reference
validation cannot prove that a literal occurs at that location or that a web
observation inspected it. This patch is not a semantic locator checker. It does
not permit publishing sensitive research simply because the JSON passes.

No generic dossier registry, graph database, new ontology or public view is added.
This is a workflow constraint repair, not evidence of historical truth or reader
benefit. Framework retains integration ownership.

## Publication-boundary correction after CC review

CC comment 5721371947 correctly identified an omitted deployment constraint:
main/root is the website, and the repository itself is public. No catalogue
entry does not mean private or unpublished. The initial optional-link default
was therefore too permissive for the public registry.

Now default validation and the publication command reject mentions without a
record_id. Only an explicit research caller can enable the optional-link checks;
the fixtures do so in memory. No CLI publication bypass is added. Sensitive or
unapproved research must stay out of this public repository, including branches
and fixtures. A Pages exclusion alone would not make a public Git repository
private. These non-sensitive synthetic/bounded fixtures are visible research
examples, not a protected research store. No live content was removed.

This check is a default fail-closed publishing check, not access control. It does
not verify permission merely because a mention has a catalogue ID.
