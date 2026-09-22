"""Skip the doctests that need a live ArangoDB server when none is reachable."""

import pytest
from _pytest.doctest import DoctestItem

from arangodol.tests._live_server import DB_URL, server_is_up

_LIVE_SERVER_DOCTESTS = {
    "arangodol.ArangoDbPersister",
    "arangodol.ArangoDbTupleKeyStore",
}


def pytest_collection_modifyitems(config, items):
    if server_is_up(DB_URL):
        return
    skip = pytest.mark.skip(reason=f"No ArangoDB server at {DB_URL}")
    for item in items:
        if isinstance(item, DoctestItem) and item.name in _LIVE_SERVER_DOCTESTS:
            item.add_marker(skip)
