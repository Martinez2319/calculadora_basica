import pytest
from app import app

@pytest.mark.parametrize("op,a,b,expected", [
    ("sumar", 2, 3, 5), ("restar", 5, 2, 3),
    ("multiplicar", 4, 3, 12), ("dividir", 10, 2, 5)])
def test_operations(op, a, b, expected):
    response = app.test_client().get(
        "/calcular", query_string={"op": op, "a": a, "b": b})
    assert response.status_code == 200
    assert response.json["resultado"] == expected

@pytest.mark.parametrize("query", [
    "op=dividir&a=1&b=0", "op=sumar&a=x&b=2",
    "op=otra&a=1&b=2", "op=sumar&a=nan&b=2", "op=sumar"])
def test_invalid_input(query):
    assert app.test_client().get("/calcular?" + query).status_code == 400

def test_health():
    assert app.test_client().get("/health").json == {"status": "ok"}
