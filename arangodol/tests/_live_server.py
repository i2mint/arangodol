"""Detect whether the local ArangoDB test server is reachable (for skipping live tests)."""

import socket
from urllib.parse import urlparse

DB_URL = "http://127.0.0.1:8529"
DB_PASSWORD = "somepassword"
_CONNECT_TIMEOUT_S = 1


def server_is_up(url=DB_URL, *, timeout=_CONNECT_TIMEOUT_S):
    parsed = urlparse(url)
    try:
        with socket.create_connection((parsed.hostname, parsed.port), timeout=timeout):
            return True
    except OSError:
        return False
