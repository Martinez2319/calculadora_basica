# Calculadora básica

Práctica de Python para sumar, restar, multiplicar y dividir desde la consola. Incluye cinco pruebas con pytest.

## Ejecutar

Con Python 3, desde la carpeta del repositorio:

```sh
python calculadora.py
```

Introduce dos números y selecciona una operación. La división entre cero muestra un mensaje de error.

## Usar las funciones

```python
from calculadora import add, sub, mul, div

print(add(2, 3))  # 5
print(div(10, 2))  # 5.0
```

## Pruebas

```sh
python -m pip install pytest
python -m pytest -v
```

Las pruebas están en [tests/test_calculadora.py](tests/test_calculadora.py). Cubren las cuatro operaciones y el rechazo de la división entre cero.

## Qué practico

Funciones, entrada por consola, manejo de excepciones y pruebas automatizadas. La validación de texto no numérico en la entrada de consola queda como posible mejora.
