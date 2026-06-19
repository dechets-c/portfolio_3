import time

from app.core import security as sec


def test_password_hash_and_verify():
    pw = "super-secret-password"
    hashed = sec.get_password_hash(pw)
    assert sec.verify_password(pw, hashed)
    assert not sec.verify_password("bad-password", hashed)


def test_create_and_decode_access_token():
    # ensure SECRET_KEY is set for the security module
    sec.SECRET_KEY = "test-secret-for-unit-tests"
    data = {"sub": "alice@example.com"}
    token = sec.create_access_token(data)
    payload = sec.decode_access_token(token)
    assert payload.get("sub") == "alice@example.com"
    assert "exp" in payload
