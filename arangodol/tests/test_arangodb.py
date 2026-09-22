"""
How to run a test ArangoDB instance locally with a Docker container:

docker rm -f arangodb-instance && \
docker run -e ARANGO_ROOT_PASSWORD=somepassword -p 8529:8529 -d --name arangodb-instance arangodb && \
sleep 10 && \
pytest tests/test_arangodb.py
"""

import pytest

from arangodol import ArangoDbPersister
from arangodol import ArangoDbTupleKeyStore

from ._live_server import DB_PASSWORD, DB_URL, server_is_up
from .base_test import BasePersisterTest, BaseKeyTupleStoreTest

if not server_is_up(DB_URL):
    pytest.skip(f"No ArangoDB server at {DB_URL}", allow_module_level=True)


class TestArangoDbPersister(BasePersisterTest):
    db = ArangoDbPersister(
        url=DB_URL,
        password=DB_PASSWORD,
        key_fields=list(BasePersisterTest.key.keys()),
    )


class TestArangoDbTupleKeyStore(BaseKeyTupleStoreTest):
    db = ArangoDbTupleKeyStore(
        url=DB_URL,
        password=DB_PASSWORD,
        key_fields=BaseKeyTupleStoreTest.key_fields,
    )
