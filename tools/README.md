# Check source pins before publishing

Run `python tools/check_view_basis.py` with Python 3.10 or newer. It reads the catalogue and the six currently pinned working-tree source files, computes Git blob identities from their exact bytes and exits nonzero on missing, malformed or mismatched pins. An optional directory argument checks another checkout. No packages, network, server or credentials are required.

Run `python -m unittest discover -s tools -p "test_*.py"` for the bounded checker tests.

The check never updates a pin. After a mismatch, review the human summary against the changed record before updating its basis. A mismatch means freshness is unestablished, not that the summary is false. A match does not establish summary accuracy, truth, displayed HTML label consistency, live deployment or the legitimacy of a manual pin update. It is not an automatic monitor or CI hook.

The checkout's existing LF rules should be respected: this checks exact bytes, not line-ending-normalized equivalents. Source routes currently use the project's public HTTPS domain; a deliberate domain migration requires updating the checker as well as the catalogue.
