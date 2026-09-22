"""Document keys are validated before they reach a request URL (no server needed)."""

import pytest

from arangodol import ArangoDbPersister, validate_document_key


def _persister(key_fields=("first_name", "last_name"), separator="::"):
    # Bypass __init__ (which connects to a server); only key handling is tested.
    p = ArangoDbPersister.__new__(ArangoDbPersister)
    p._key_fields = key_fields
    p._key_fields_separator = separator
    return p


@pytest.mark.parametrize(
    "key", ["abc", "Robot::0a1b", "a-b_c:d.e@f(g)+h,i=j;k$l!m*n'o", "x" * 254]
)
def test_valid_keys_pass(key):
    assert validate_document_key(key) == key


@pytest.mark.parametrize(
    "key",
    ["", ".", "..", "a/b", "../other", "a%2Fb", "a b", "a?b", "a#b", "x" * 255, 42],
)
def test_invalid_keys_raise_key_error(key):
    with pytest.raises(KeyError):
        validate_document_key(key)


def test_make_key_validates_joined_key():
    p = _persister()
    assert p._make_key({"first_name": "a", "last_name": "b"}) == "a::b"
    with pytest.raises(KeyError):
        p._make_key({"first_name": "..", "last_name": "/x"})
