# Check source pins before publishing

Run `python tools/check_view_basis.py` with Python 3.10 or newer. It reads the catalogue and the six currently pinned working-tree source files, computes Git blob identities from their exact bytes and exits nonzero on missing, malformed or mismatched pins. An optional directory argument checks another checkout. No packages, network, server or credentials are required.

Run `python -m unittest discover -s tools -p "test_*.py"` for the bounded checker tests.

It also reads each human-view HTML file, requiring one `View basis:` paragraph whose source prefixes and record version (or format) match the catalogue. It checks source HTML text, not rendered visibility or the alignment date.

The check never updates a pin. After a mismatch, review the human summary against the changed record before updating its basis. A mismatch means freshness is unestablished, not that the summary is false. A match does not establish summary accuracy, truth, live deployment or the legitimacy of a manual pin update. It is not an automatic monitor or CI hook. A structural error stops the remaining checks; the printed count is the number actually checked, not a claim of exhaustive success.

The checkout's existing `.gitattributes` rule (`* text=auto eol=lf`) should be respected: this checks exact bytes, not line-ending-normalized equivalents. Source routes currently use the project's public HTTPS domain; a deliberate domain migration requires updating the checker as well as the catalogue.
