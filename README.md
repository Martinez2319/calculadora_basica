# Calculadora básica

Calculadora en Python para sumar, restar, multiplicar y dividir desde la terminal o mediante una API HTTP. El proyecto permite practicar la automatización de pruebas con pytest y comprobar un despliegue en Docker con GitHub Actions.

## Inicio rápido

Necesitas Git y Python 3.12. Para usar la calculadora de consola basta con Python. Docker solo es necesario para ejecutar el contenedor.

```bash
git clone --branch resultado-aprendizaje-cd https://github.com/Martinez2319/calculadora_basica.git
cd calculadora_basica
python calculadora.py
```

Para calcular `2 + 3`, introduce `2`, luego `3` y selecciona la opción `1`. La consola muestra `Resultado: 5.0`.

## API y pruebas automatizadas

Desde la raíz del repositorio, crea el entorno virtual e instala las dependencias del proyecto y de pruebas.

```bash
python scripts/prepare_environment.py
```

**Windows (PowerShell)**

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ -v
.\.venv\Scripts\python.exe -m flask --app app run
```

**Linux y macOS**

```bash
.venv/bin/python -m pytest tests/ -v
.venv/bin/python -m flask --app app run
```

Con Flask en ejecución, abre [el ejemplo de suma](http://127.0.0.1:5000/calcular?op=sumar&a=2&b=3) en el navegador. La respuesta esperada es `{"resultado":5.0}`.

| Ruta | Comportamiento |
| --- | --- |
| `GET /` | Muestra el nombre de la aplicación y las operaciones disponibles. |
| `GET /health` | Devuelve `{"status":"ok"}` si la API responde. |
| `GET /calcular?op=sumar&a=2&b=3` | Calcula la operación solicitada. `op` admite `sumar`, `restar`, `multiplicar` y `dividir`. |

La API devuelve HTTP 400 cuando faltan parámetros, los operandos no son números finitos, la operación es desconocida, el resultado queda fuera de rango o se intenta dividir entre cero. La suite cubre las operaciones, la salud de la API y las entradas inválidas.

## Despliegue con Docker

Con Docker iniciado en modo de contenedores Linux y el puerto local 8080 libre, ejecuta:

```bash
python scripts/deploy.py practica1
```

El script construye la imagen `calculadora:practica1`, inicia el contenedor y comprueba su salud, las cuatro operaciones y el rechazo de la división entre cero. La API queda disponible en [http://127.0.0.1:8080](http://127.0.0.1:8080) mientras el contenedor siga activo. Para retirarlo y volver a usar la misma etiqueta, ejecuta:

```bash
docker rm -f calculadora-practica1
```

Un `push` a `resultado-aprendizaje-cd` activa el [flujo de GitHub Actions](.github/workflows/calculadora-cd.yml). El flujo ejecuta pytest, construye la imagen, prueba la API por HTTP y retira el contenedor temporal al finalizar. En la [ejecución verificada](https://github.com/Martinez2319/calculadora_basica/actions/runs/42249936247) pasaron las 15 pruebas y la comprobación HTTP.

## Estructura del proyecto

| Archivo o carpeta | Contenido |
| --- | --- |
| [`calculadora.py`](calculadora.py) | Operaciones aritméticas e interfaz de consola. |
| [`app.py`](app.py) | API Flask que reutiliza las operaciones. |
| [`tests/`](tests/) | Pruebas de la calculadora y de la API. |
| [`scripts/`](scripts/) | Preparación del entorno, despliegue y comprobación HTTP. |
| [`Dockerfile`](Dockerfile) | Construcción de la imagen y arranque con Gunicorn. |

## Soporte y contribuciones

El proyecto se mantiene en [Martinez2319/calculadora_basica](https://github.com/Martinez2319/calculadora_basica). Para reportar un problema, abre un [issue](https://github.com/Martinez2319/calculadora_basica/issues) con el comando, el resultado esperado y el error observado. Para proponer un cambio, ejecuta las pruebas y abre un pull request dirigido a `resultado-aprendizaje-cd`.

## Referencia de documentación

La estructura sigue las recomendaciones de GitHub para explicar el propósito de un proyecto, cómo empezar a usarlo, dónde pedir ayuda y cómo contribuir. [Guía de GitHub sobre archivos README](https://docs.github.com/es/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
