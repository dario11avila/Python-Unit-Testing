# Python Unit Testing Demo

Este proyecto es una demostración de pruebas unitarias en Python usando `pytest`.

## Estructura del proyecto

- `operations.py`: Funciones matemáticas básicas (sumar, restar, multiplicar, dividir).
- `test_operations.py`: Pruebas unitarias para cada función de `operations.py`.
- `.github/workflows/python-tests.yml`: Workflow de GitHub Actions para ejecutar los tests automáticamente en cada push o pull request.

## Cómo ejecutar los tests localmente

1. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta los tests:

   ```bash
   pytest
   ```
3. (Opcional) Ejecuta los tests con cobertura y mostrando en terminal las líneas faltantes:

   ```bash
   pytest --cov=./ --cov-report=term-missing 
   ```

## Integración continua

Cada vez que se realiza un push o pull request a la rama `master`, GitHub Actions ejecuta automáticamente los tests definidos en `test_operations.py`.
