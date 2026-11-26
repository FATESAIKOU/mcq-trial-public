"""Tiny in-memory cache helper (synthetic)."""

_STORE: dict[str, object] = {}


def put(key: str, value: object) -> None:
    _STORE[key] = value


def get(key: str, default: object = None) -> object:
    return _STORE.get(key, default)
