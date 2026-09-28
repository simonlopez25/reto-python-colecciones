<div align="center">

# 🏆 Catálogo de Coleccionables

### _Reto Python — Colecciones Nativas_
<br/>

[![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Version](https://img.shields.io/badge/Versión-0.1.0-6366f1?style=for-the-badge&logoColor=white)](https://github.com/simonlopez25/reto-python-colecciones)
[![Tests](https://img.shields.io/badge/Tests-46%20Passed-22c55e?style=for-the-badge&logo=pytest&logoColor=white)](#-pruebas-automatizadas-con-pytest)
[![Pytest](https://img.shields.io/badge/Pytest-9.1.1-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)
[![BDD](https://img.shields.io/badge/BDD-30%20Escenarios-596127?style=for-the-badge&logo=cucumber&logoColor=white)](#-especificaciones-de-comportamiento-gherkin--bdd)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-ec4899?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](#)

<br/>

> 💬 *"De coleccionista a desarrollador — la colección más valiosa es el código limpio."*

</div>

---

## 🎯 ¿Qué es esto?

Sistema de gestión de **catálogo de coleccionables** por consola, construido **100% en Python puro**. Sin frameworks, sin magia externa — solo colecciones nativas de Python haciendo su trabajo.

¿Tienes figuras raras? ¿Cómics de edición limitada? ¿Monedas antiguas? Con este sistema puedes **agregar, buscar, filtrar y eliminar** tus piezas como un profesional. 🕹️

---

## 🗂️ Estructura del Proyecto

```
reto-python-colecciones/
│
├── 🧠  main.py               →  Interfaz de usuario / menú interactivo
├── 📦  catalog.py            →  Lógica del catálogo (el corazón del sistema)
├── 🛡️   validations.py       →  Validaciones de datos robustas
├── 🧪  test/                 →  Suite de pruebas automatizadas con pytest
│   ├── test_catalog.py       →  Pruebas de lógica y operaciones del catálogo
│   ├── test_main.py          →  Pruebas de la interfaz de consola y menús
│   └── test_validations.py   →  Pruebas de validaciones y casos límite
├── 🥒  features/             →  Especificaciones de comportamiento en Gherkin (BDD)
│   ├── catalog.feature       →  Escenarios del catálogo (16 escenarios)
│   ├── main.feature          →  Escenarios del menú de consola (5 escenarios)
│   └── validations.feature   →  Escenarios de validaciones (9 escenarios)
├── ⚙️   pyproject.toml       →  Configuración del proyecto y dependencias (uv + pytest)
├── 🔒  uv.lock               →  Versiones exactas del entorno de desarrollo
└── 🚫  .gitignore            →  Exclusiones de .venv, __pycache__ y cachés
```

> Arquitectura modular: cada archivo tiene **una sola responsabilidad**. Así de limpio.

---

## 🚀 Instalación y Ejecución

### Prerequisitos
- 🐍 Python `>= 3.14`
- ⚡ [`uv`](https://docs.astral.sh/uv/) — gestor de paquetes moderno y rapidísimo

### Pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/simonlopez25/reto-python-colecciones.git
cd reto-python-colecciones

# 2. Sincroniza el entorno virtual con uv (incluye dependencias de desarrollo)
uv sync

# 3. Ejecuta el programa
uv run python main.py

# 4. Ejecuta la suite de pruebas
uv run pytest
```

---

## 🎮 Funcionalidades — Menú de Opciones

Al iniciar el programa verás este menú:

```
========================================
      CATÁLOGO DE COLECCIONABLES
========================================
1. Agregar una pieza
2. Mostrar todas las piezas
3. Mostrar piezas disponibles
4. Mostrar el precio promedio
5. Buscar una pieza por identificador
6. Eliminar una pieza
7. Salir
========================================
Seleccione una opción (1-7): 
```

| # | Opción del menú | Función en `main.py` | Descripción |
|:-:|-----------------|----------------------|-------------|
| 1️⃣ | Agregar una pieza | `handle_add_piece()` | Solicita los datos y agrega la pieza al catálogo (repite hasta que la validación pase) |
| 2️⃣ | Mostrar todas las piezas | `handle_list_pieces()` | Lista los nombres de las piezas registradas con numeración desde 1 |
| 3️⃣ | Mostrar piezas disponibles | `handle_list_available()` | Muestra solo las piezas **disponibles** con su precio |
| 4️⃣ | Mostrar el precio promedio | `handle_average_price()` | Calcula y muestra el precio promedio del catálogo |
| 5️⃣ | Buscar una pieza por ID | `handle_find_piece()` | Busca por ID y muestra todos sus detalles, o avisa si no existe |
| 6️⃣ | Eliminar una pieza | `handle_remove_piece()` | Elimina una pieza por su ID e informa si tuvo éxito |
| 7️⃣ | Salir | `main()` → `break` | Cierra el programa con mensaje de despedida |

> ℹ️ Cualquier otra entrada muestra `Opción no válida. Por favor, seleccione un número entre 1 y 7.` y el menú se vuelve a dibujar.

> ⚠️ **El catálogo vive en memoria.** Al cerrar el programa se pierde todo: no hay base de datos ni persistencia en archivo. Es una decisión consciente para mantener el reto enfocado en las colecciones nativas.

---

## 📦 `catalog.py` — El Cerebro del Sistema

Todas las operaciones viven aquí. El catálogo es una `list` de `dict`s con esta estructura:

```python
{
    "id":          "P001",
    "name":        "Figura Goku SSJ4",
    "category":    "Figuras",
    "price":       149.99,
    "status":      "disponible",
    "description": "Pieza certificada, edición limitada 2002"
}
```

### Funciones implementadas

| Función | Colección usada | ¿Qué hace? | ¿En el menú? |
|---------|:--------------:|-------------|:------------:|
| `add_piece(...)` | `dict` | Crea, valida y agrega una pieza; devuelve el `dict` resultante | 1️⃣ |
| `list_pieces(catalog)` | `list` | Devuelve lista con los nombres de todas las piezas | 2️⃣ |
| `filter_by_status(catalog, status)` | `list` | Filtra piezas por estado, validando contra los permitidos | 3️⃣ |
| `get_average_price(catalog)` | `list` | Calcula el precio promedio; devuelve `0.0` si el catálogo está vacío | 4️⃣ |
| `find_piece_by_id(catalog, id)` | `list` | Busca pieza por ID con recorrido lineal; retorna `None` si no existe | 5️⃣ |
| `remove_piece(catalog, id)` | `list` | Elimina la pieza del catálogo, retorna `bool` sin lanzar excepciones | 6️⃣ |
| `get_catalog_summary(catalog)` | `dict` | Agrupa y cuenta piezas por categoría | — |
| `get_pieces_by_category(catalog, cat)` | `list` | Filtra por categoría, insensible a mayúsculas (list comprehension) | — |
| `filter_by_min_price(catalog, p)` | `list` | Filtra piezas con precio mayor o igual al mínimo | — |
| `piece_exists(catalog, id)` | `list` | Retorna `True/False` delegando en `find_piece_by_id()` | — |

> 💡 **Colecciones de Python usadas:** `list` y `dict` para almacenar y manipular el catálogo, `set` en las validaciones — ¡el reto se llama colecciones por algo! 🐍

### 🔍 Funciones que existen pero no están en el menú

`get_catalog_summary()`, `get_pieces_by_category()`, `filter_by_min_price()` y `piece_exists()` están implementadas y cubiertas por pruebas, pero **ningún handler de `main.py` las expone todavía**. Son parte de la API pública de `catalog.py`: sirven como base para las opciones 7, 8, 9 y 10 del menú, o como puntos de extensión para quien reutilice el módulo.

> ℹ️ `piece_exists()` delega en `find_piece_by_id()`, por lo que su costo es **O(n)**, no O(1). El `O(1)` real del proyecto viene de los `set` de `validations.py`.

---

## 🛡️ `validations.py` — El Guardián de Datos

Nada entra al catálogo sin pasar por este filtro. Las validaciones lanzan `ValueError` con mensajes claros.

```python
# Estados permitidos (set para búsqueda O(1))
allowed_statuses = {"disponible", "reservado", "reservada", "vendida"}

# Palabras clave requeridas en la descripción
required_keywords = {"usada", "certificada"}
```

| Función | ¿Qué valida? | Error que lanza |
|---------|---------------|-----------------|
| `validate_not_empty(value, field_name)` | Que el campo sea `str` y no esté vacío ni solo espacios | `ValueError` |
| `validate_price(price)` | Que sea `int`/`float` (rechaza `bool`) y mayor a `0` | `ValueError` |
| `validate_status(status)` | Que normalizado (`strip` + `lower`) esté en `allowed_statuses` | `ValueError` |
| `validate_description(description)` | Que no esté vacía e incluya `'usada'` o `'certificada'` | `ValueError` |

> ⚠️ **Pendiente de unificar:** `allowed_statuses` acepta cuatro valores, incluyendo tanto `"reservado"` como `"reservada"`, pero el prompt de `main.py:34` solo anuncia tres (`disponible, reservada, vendida`). Conviene decidir la forma canónica y alinear las tres fuentes: el `set`, el prompt del menú y las specs de `features/`.

---

## 🧪 Pruebas Automatizadas con Pytest

El proyecto cuenta con una suite completa de **46 pruebas unitarias y funcionales** implementadas con [`pytest`](https://docs.pytest.org/), garantizando la integridad de las operaciones, la robustez de las validaciones y el correcto comportamiento de la interfaz de consola interactiva.

```
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: reto-python-colecciones
configfile: pyproject.toml
testpaths: test
collected 46 items

test\test_catalog.py ................                                    [ 34%]
test\test_main.py .....                                                  [ 45%]
test\test_validations.py .........................                       [100%]

============================= 46 passed in 0.14s ==============================
```

### 📋 Cobertura de las Pruebas

| Archivo de Prueba | Tests | ¿Qué verifica? | Herramientas clave |
|-------------------|:-----:|----------------|--------------------|
| `test/test_catalog.py` | 16 | • Adición de piezas con datos limpios (`strip`) y detección de IDs duplicados.<br/>• Búsqueda por ID existente / inexistente (`None`).<br/>• Eliminación de piezas y retorno de estado booleano.<br/>• Resumen y conteo de piezas agrupadas por categoría (`dict`).<br/>• Filtrado por categoría insensible a mayúsculas/minúsculas.<br/>• Filtrado por estado y por precio mínimo.<br/>• Cálculo de precio promedio y manejo de catálogo vacío.<br/>• Validación estricta de tipos de entrada (`TypeError`, `ValueError`). | `@pytest.fixture`, `pytest.raises` |
| `test/test_validations.py` | 25 | • Campos no vacíos (`validate_not_empty`): cadenas vacías, espacios en blanco, `None`, tipos no-string.<br/>• Precios válidos (`validate_price`): números positivos, rechazo de `<= 0`, booleanos y tipos no numéricos.<br/>• Estados permitidos (`validate_status`): normalización (`strip`, `lower`) y rechazo de estados inválidos.<br/>• Descripciones (`validate_description`): presencia obligatoria de `"usada"` o `"certificada"`. | `@pytest.mark.parametrize`, `pytest.raises` |
| `test/test_main.py` | 5 | • Renderizado visual del menú de consola principal.<br/>• Flujo interactivo completo de agregar pieza (`handle_add_piece`).<br/>• Listado de piezas con catálogo vacío vs. con elementos.<br/>• Salida limpia del programa mediante la opción 7. | `monkeypatch` (mock de `input`), `capsys` (inspección de `stdout`) |

### ⚡ Comandos para Ejecutar las Pruebas

```bash
# Ejecutar toda la suite de pruebas
uv run pytest

# Ejecutar con salida detallada (verbose)
uv run pytest -v

# Ejecutar un módulo de pruebas específico
uv run pytest test/test_catalog.py
uv run pytest test/test_validations.py
uv run pytest test/test_main.py

# Ejecutar pruebas que coincidan con un nombre o patrón
uv run pytest -k "average"
```

---

## 🥒 Especificaciones de Comportamiento (Gherkin / BDD)

Cada prueba nace primero como un **escenario de negocio legible**, escrito en Gherkin dentro de `features/`. Cada escenario declara explícitamente a qué test de `pytest` corresponde, así que la especificación y la verificación nunca se separan.

```gherkin
# features/catalog.feature
Feature: Piece catalog management

  # Test: test_add_piece_duplicate_id
  Scenario: Reject piece with duplicate ID
    Given a sample catalog with 3 pieces exists
    When attempting to add a piece with ID "1"
    Then the system returns the error "Ya existe una pieza con el ID '1'."
```

### Escenarios por archivo

| Archivo | Escenarios | Cubre |
|---------|:----------:|-------|
| `features/catalog.feature` | 16 | Alta, duplicados, búsqueda, existencia, eliminación, resumen por categoría, filtros por categoría/estado/precio, precio promedio y catálogo vacío |
| `features/validations.feature` | 9 | Casos válidos e inválidos de nombre, precio, estado y descripción, con el mensaje de error exacto esperado |
| `features/main.feature` | 5 | Renderizado del menú, salida por opción 7, alta interactiva y listado con y sin piezas |
| **Total** | **30** | |

### Cómo se relacionan con `pytest`

- El comentario `# Test: <nombre>` es el **enlace explícito** entre el escenario y su test.
- Los archivos `.feature` son **especificación ejecutable por personas, no por máquina**: el proyecto **no** instala `pytest-bdd`, así que `uv run pytest` solo corre los tests de `test/`, nunca los `.feature`.
- Valor real: al leer `features/validations.feature` se entiende el contrato esperado de cada validación sin abrir ningún `.py`; y al abrir el test se sabe qué requisito satisface.
- Si se quisiera ejecutarlos, bastaría añadir `pytest-bdd` al grupo `dev` y una función `step` por línea de Given/When/Then.

---

## 📐 Convenciones de Calidad

### Guardia de tipos del catálogo

Todas las funciones públicas de `catalog.py` pasan primero por `_validate_catalog()`:

```python
def _validate_catalog(catalog: list):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
```

Se lanza `TypeError` (no `ValueError`) porque el error es de **tipo**, no de valor. Esto obliga al cliente a tratar las condiciones de uso incorrecto y los datos inválidos por separado.

### Errores: `ValueError` vs. retorno

| Situación | Estrategia | Ejemplo |
|-----------|-----------|---------|
| La entrada del usuario es inválida | Lanzar `ValueError` con mensaje accionable | `add_piece()` con ID duplicado |
| La consulta no encuentra nada | Retornar `None` | `find_piece_by_id()` |
| La operación es idempotente y su resultado es binario | Retornar `bool` | `remove_piece()` captura internamente el `ValueError` y devuelve `False` |

> 💡 `remove_piece()` en `catalog.py:61` es el ejemplo canónico: lanza un `ValueError` con detalle y lo captura en su propio `except ValueError` para devolver `False`, de modo que el menú nunca recibe una excepción.

---

## 🧩 Conceptos de Python Aplicados

<details>
<summary><strong>🔍 Ver fragmentos de código clave</strong></summary>

<br/>

**✅ List Comprehensions — elegancia en una línea**
```python
nombres = [piece["name"] for piece in catalog]
```

**✅ Dict como estructura de datos principal**
```python
pieza = {"id": "001", "name": "Pokémon Card", "price": 45.0}
```

**✅ Set para validaciones eficientes O(1)**
```python
allowed_statuses = {"disponible", "reservado", "vendida"}
```

**✅ Type hints para código legible y documentado**
```python
def find_piece_by_id(catalog: list, piece_id: str) -> dict | None:
```

**✅ Manejo de errores con try/except**
```python
try:
    new_piece = add_piece(...)
except ValueError as error:
    print(f"Error: {error}")
```

**✅ Función `sum()` con generador para el promedio**
```python
total = sum(piece["price"] for piece in catalog)
```

**✅ `enumerate()` para listar con índice desde 1**
```python
for i, name in enumerate(pieces, start=1):
    print(f"{i}. {name}")
```

**✅ Fixtures de Pytest — datos de prueba limpios y reutilizables**
```python
@pytest.fixture
def sample_catalog():
    return [
        {"id": "1", "name": "Anillo de Oro", "category": "Joyería", "price": 150.0, "status": "disponible", "description": "Anillo certificado"},
    ]
```

**✅ Parametrización de tests (`@pytest.mark.parametrize`) — cobertura exhaustiva sin repetir código**
```python
@pytest.mark.parametrize("invalid_value", ["", "   ", None, 123])
def test_validate_not_empty_invalid(invalid_value):
    with pytest.raises(ValueError, match="El campo 'nombre' no puede estar vacío."):
        validate_not_empty(invalid_value, "nombre")
```

**✅ Simulación de I/O (`monkeypatch`) y captura de salida (`capsys`) para la consola**
```python
def test_main_exit_option(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "7")
    main()
    captured = capsys.readouterr()
    assert "¡Gracias por utilizar el Catálogo de Coleccionables!" in captured.out
```

**✅ `__name__ == "__main__"` — control del punto de entrada**
```python
if __name__ == "__main__":
    main()
```

</details>

---

## 🔄 Flujo de Datos

```
                     👤 Usuario
                         │
                         ▼
               ┌─────────────────┐
               │    main.py      │  ← Menú interactivo + handlers
               └────────┬────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   add_piece()    list_pieces()   filter_by_status()
   find_piece()   remove_piece()  get_average_price()
        │               │               │
        └───────┬───────┴───────────────┘
                │
                ▼
       ┌──────────────────┐
       │ _validate_catalog│  ← TypeError si no es list
       └────────┬─────────┘
                │
                ▼
       ┌──────────────────┐
       │  validations.py  │  ← Guardián de datos (ValueError)
       └────────┬─────────┘
                │
                ▼
       ┌──────────────────┐
       │ catalog: list    │  ← [{"id":..., "name":..., ...}]
       │    de dicts      │
       └──────────────────┘
```

> 🔁 En paralelo, `test/` verifica este flujo y `features/` lo especifica: 30 escenarios Gherkin enlazados uno a uno con los tests que los cubren.

---

## 💡 Decisiones de Diseño

| Decisión | Razón |
|----------|-------|
| **Sin clases / Sin OOP** | El reto apunta al uso de colecciones nativas (`list`, `dict`, `set`) |
| **Separación de responsabilidades** | `main.py` → UI · `catalog.py` → lógica · `validations.py` → datos |
| **Funciones puras** | Sin efectos secundarios inesperados; reciben y devuelven datos |
| **`set` para validaciones** | Búsqueda en O(1) en vez de O(n) con `list` |
| **`TypeError` para tipos, `ValueError` para contenido** | Distingue el error de uso del API del error de dato inválido |
| **Búsqueda lineal, sin índices** | El catálogo es pequeño; evita la complejidad de un índice que habría que mantener al agregar y eliminar |
| **Catálogo en memoria** | Evita dependencias externas; el alcance del reto son las colecciones, no la persistencia |
| **Especificación antes que test** | `features/` documenta el comportamiento esperado en lenguaje de negocio, enlazado a cada test |
| **`__name__ == "__main__"`** | `main()` solo se ejecuta como punto de entrada, no al importar |
| **Testing automatizado (`pytest`)** | Suite completa de 46 pruebas para garantizar fiabilidad y prevenir regresiones |
| **Dependencias de desarrollo aisladas** | `pytest` vive en `[dependency-groups] dev`, así que `uv sync --no-dev` instala un runtime con cero dependencias |

---

## 🧭 Deuda técnica conocida

Pequeños pendientes detectados al revisar el código, gathering para futuras iteraciones:

| # | Pendiente | Dónde | Impacto |
|:-:|-----------|-------|---------|
| 1 | Los estados están desalineados en tres sitios: `allowed_statuses` acepta `reservado` y `reservada`, el prompt solo anuncia tres, y la fixture de `test_catalog.py:21` usa `"vendido"`, un valor que **`validate_status()` rechazaría** | `validations.py:1`, `main.py:34`, `test/test_catalog.py:21` | Alto: la fixture contiene datos que el sistema no permitiría crear |
| 2 | Cuatro funciones probadas no están expuestas en el menú | `main.py` | Funcionalidad oculta |
| 3 | `handle_list_available()` captura un `ValueError` que nunca puede ocurrir con el literal `"disponible"` | `main.py:57-68` | Código muerto |
| 4 | `from catalog import *` / `from validations import *` sin `__all__` | `main.py:1`, `catalog.py:1` | Import implícito, herramientas no detectan dependencias |
| 5 | `remove_piece()` lanza y captura su propio `ValueError` para devolver `False` | `catalog.py:61-71` | Sobrecarga; un `if` directo sería más claro |
| 6 | `.pyc` de `__pycache__` estaban versionados en el repo | `.gitignore` | Ruido en el historial |

---

<div align="center">

## 👨‍💻 Autor

**Simón López**

🐍 Aprendiendo Python con disciplina y colecciones bien ordenadas

[![GitHub](https://img.shields.io/badge/GitHub-simonlopez25-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/simonlopez25)

<br/>

*Hecho con 🐍 Python puro · mucho ☕ café · y amor por las colecciones*

---

⭐ **Si te gustó este proyecto, dale una estrella al repo** ⭐

</div>
