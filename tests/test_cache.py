from src.widgets.cache import get, put


def test_put_then_get():
    put("k", 1)
    assert get("k") == 1
