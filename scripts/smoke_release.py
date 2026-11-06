import json, sys, time
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
base = sys.argv[1].rstrip("/")
for attempt in range(30):
    try:
        with urlopen(base + "/health", timeout=3) as response:
            assert response.status == 200
            assert json.load(response) == {"status": "ok"}
        break
    except (URLError, AssertionError):
        if attempt == 29:
            raise
        time.sleep(2)
cases = [("sumar", 2, 3, 5), ("restar", 5, 2, 3),
         ("multiplicar", 4, 3, 12), ("dividir", 10, 2, 5)]
for op, a, b, expected in cases:
    started = time.perf_counter()
    with urlopen(f"{base}/calcular?op={op}&a={a}&b={b}", timeout=5) as r:
        result = json.load(r)
        assert r.status == 200 and result["resultado"] == expected
    print(op, result, "ms=", round((time.perf_counter()-started)*1000, 2))
try:
    urlopen(base + "/calcular?op=dividir&a=1&b=0", timeout=5)
    raise AssertionError("Se esperaba HTTP 400")
except HTTPError as error:
    assert error.code == 400
print("RELEASE_OK: salud, cuatro operaciones y division por cero")
