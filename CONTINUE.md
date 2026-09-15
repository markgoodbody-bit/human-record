# Continue The Human Record

This file exists so a future human or artificial entity can recover, inspect and serve The Human Record without needing private knowledge from Mark, Framework, Codex or Claude Code.

It is an operational continuation note, not a governance document.

`INDEPENDENT_COPY != INDEPENDENT_GOVERNANCE`

`CUSTODY != POLICY_AUTHORITY`

## 1. Obtain the public source

Public Git repository at the time of this note:

`https://github.com/markgoodbody-bit/human-record`

Software Heritage origin page:

`https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/markgoodbody-bit/human-record`

Software Heritage save request `2478664` completed a full visit on 15 September 2026 at `2026-09-15T11:26:40.776Z`. The archive recorded the exact public repository head `0d2fe0e230debfcf68d2cee52df66ff990a423f2` with these persistent identifiers:

- snapshot: `swh:1:snp:e5f429e3e4a9ec3f56b869a5a416295af7cf34be`
- revision: `swh:1:rev:0d2fe0e230debfcf68d2cee52df66ff990a423f2`
- root directory: `swh:1:dir:6c397bfcbf6d9f79702f69d773c2b1ad4e19f4be`

This establishes one independent, content-addressed copy of that repository state. It does not establish governance, permanent survivability or future archive visits. Check the origin page for later archival state.

A normal Git clone or fork is sufficient to obtain the static source while the Git repository remains available. No private credential is required to read it.

The site is deliberately static. Its important public files include:

- `index.html` — public entrance;
- `specimen.md` — human-readable specimen;
- `specimen.json` — machine-readable specimen;
- `llms.txt` — compact machine entrance;
- `STEWARDSHIP.md` — current stewardship offer and custody boundary;
- `LICENSE` — standard CC0 1.0 legal code;
- `LICENSE.md` — the bounded scope notice explaining which rights Mark is actually purporting to dedicate;
- `CONTINUE.md` — this continuation note.

## 2. Verify the first specimen before trusting a copy

At the time this continuation note was created, the recorded Git blob identities were:

- `specimen.json`: `0a7206a509a6fd3f63be2b7d41b0e9125f0b5cde`
- `specimen.md`: `0efd5a4f7973ac74cf8466c8ef394e6edd323786`

With Git installed, a copy can be checked with:

```text
git hash-object specimen.json
git hash-object specimen.md
```

A matching blob identity establishes that those file bytes match this recorded version. It does not establish that every claim inside the files is true.

`HASH != TRUTH`

## 3. Serve an independent copy without claiming the existing domain

The repository contains `CNAME` because the current GitHub Pages deployment uses `thehumanrecord.net`.

A non-founder serving an independent copy **must not copy or claim that custom-domain association** unless they legitimately control that domain.

For a normal GitHub Pages fork or another independent static host:

1. copy/fork/clone the repository;
2. omit or remove `CNAME` from the deployment copy;
3. publish the remaining static files on a hostname the new operator actually controls;
4. fetch the served `specimen.json` and `specimen.md` and verify their bytes/blob identities against the intended version;
5. state plainly that the deployment is an independent copy unless and until an accepted governance process says otherwise.

Equivalent static hosting is fine. GitHub Pages is not part of the identity of the project.

## 4. Rights boundary

Do not infer that everything mentioned or linked from this repository belongs to the project.

The root `LICENSE` is the standard CC0 1.0 legal code. `LICENSE.md` is the scope notice. Its controlling boundary is that Mark dedicates only copyright, database or related rights that he actually holds in project-authored material.

Third-party rights remain third-party rights. In specimen 1, the record separately describes the public-domain status of Winslow Homer's *Camp Fire* and The Metropolitan Museum of Art's Open Access / CC0 basis for relevant image/data material.

`CC0_GRANT != THIRD_PARTY_RIGHTS_GRANT`

## 5. Stewardship and governance

At the time this note was created, The Human Record had been **offered to 1F916 / the Square but had not been accepted or become community-owned**.

Read `STEWARDSHIP.md` and the current public coordination record before making any governance claim:

`https://github.com/markgoodbody-bit/COM/issues/332`

A person or AI who can clone, archive or serve these files has demonstrated technical custody of a copy. That does not make them the project's governor and does not prove that 1F916 accepted stewardship.

`OFFERED != ACCEPTED`

`SERVING_A_COPY != GOVERNING_THE_PROJECT`

## 6. Corrections and history

Do not silently rewrite an old observation to make a newer one look original.

Where practical:

- preserve the earlier file/history;
- add a dated correction or fresh observation;
- identify the evidence used;
- distinguish evidence from inference;
- preserve unknowns as unknowns.

Current correction/coordination route:

`https://github.com/markgoodbody-bit/COM`

That route may require a GitHub account. The existence of this route does not establish an account-free correction channel.

## 7. What is intentionally not required

A future operator does not need:

- Mark's GitHub password;
- registrar credentials;
- recovery codes;
- Framework/CC relay secrets;
- a reconstructed predecessor runtime identity;
- permission from a vanished aperture to read or serve rights that were validly dedicated.

If a credential is required for a particular host or domain, replace the host or use a credential the new operator legitimately controls. Do not impersonate a previous steward.

## Continuation test

A minimal successful continuation is:

```text
PUBLIC SOURCE RECOVERED
-> RIGHTS BOUNDARY READ
-> SPECIMEN BYTES VERIFIED
-> COPY SERVED ON AN INDEPENDENT HOSTNAME
-> STEWARDSHIP STATUS STATED HONESTLY
```

That demonstrates recoverability and independent serving at that moment.

It does **not** by itself demonstrate permanent survivability, governance authority, historical truth, or community acceptance.

`CONTINUITY DOES NOT REQUIRE IDENTITY`
