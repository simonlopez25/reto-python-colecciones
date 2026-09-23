<div align="center">

# 🏆 Catálogo de Coleccionables

### _Reto Python — Colecciones Nativas_
<br/>

[![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Version](https://img.shields.io/badge/Versión-0.1.0-6366f1?style=for-the-badge&logoColor=white)](https://github.com/simonlopez25/reto-python-colecciones)
[![Estado](https://img.shields.io/badge/Estado-Completado_✅-22c55e?style=for-the-badge&logoColor=white)](#)

[![Dependencias](https://img.shields.io/badge/Sin_Dependencias-100%25_Python_Puro-f59e0b?style=for-the-badge&logo=python&logoColor=white)](#)
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
├── 🧠  main.py           →  Interfaz de usuario / menú interactivo
├── 📦  catalog.py        →  Lógica del catálogo (el corazón del sistema)
├── 🛡️   validations.py   →  Validaciones de datos robustas
└── ⚙️   pyproject.toml   →  Configuración del proyecto (uv)
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

# 2. Sincroniza el entorno virtual con uv
uv sync

# 3. Ejecuta el programa
uv run python main.py
```

---

## 🎮 Funcionalidades — Menú de Opciones

Al iniciar el programa verás este menú:

```
╔══════════════════════════════════════╗
║      CATÁLOGO DE COLECCIONABLES      ║
╠══════════════════════════════════════╣
║  1. Agregar una pieza                ║
║  2. Mostrar todas las piezas         ║
║  3. Mostrar piezas disponibles       ║
║  4. Mostrar el precio promedio       ║
║  5. Buscar una pieza por ID          ║
║  6. Eliminar una pieza               ║
║  7. Salir                            ║
╚══════════════════════════════════════╝
```

| # | Función en `main.py` | Descripción |
|:-:|----------------------|-------------|
| 1️⃣ | `handle_add_piece()` | Solicita los datos y agrega la pieza al catálogo |
| 2️⃣ | `handle_list_pieces()` | Lista todos los nombres de las piezas registradas |
| 3️⃣ | `handle_list_available()` | Muestra solo las piezas **disponibles** con su precio |
| 4️⃣ | `handle_average_price()` | Calcula y muestra el precio promedio del catálogo |
| 5️⃣ | `handle_find_piece()` | Busca una pieza por ID y muestra todos sus detalles |
| 6️⃣ | `handle_remove_piece()` | Elimina una pieza del catálogo por su ID |
| 7️⃣ | `main()` → salida | Cierra el programa con mensaje de despedida |

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

| Función | Colección usada | ¿Qué hace? |
|---------|:--------------:|------------|
| `add_piece(...)` | `dict` | Crea y devuelve un dict validado de la pieza |
| `list_pieces(catalog)` | `list` | Devuelve lista con los nombres de todas las piezas |
| `find_piece_by_id(catalog, id)` | `list` | Busca pieza por ID, retorna `None` si no existe |
| `remove_piece(catalog, id)` | `list` | Elimina la pieza del catálogo, retorna `bool` |
| `get_catalog_summary(catalog)` | `dict` | Agrupa y cuenta piezas por categoría |
| `get_pieces_by_category(...)` | `list` | Filtra piezas por categoría (list comprehension) |
| `piece_exists(catalog, id)` | `set` | Retorna `True/False` si la pieza existe |
| `filter_by_status(catalog, status)` | `list` | Filtra piezas por estado |
| `filter_by_min_price(catalog, p)` | `list` | Filtra piezas con precio mayor al mínimo |
| `get_average_price(catalog)` | `list` | Calcula el precio promedio del catálogo |

> 💡 **Colecciones de Python usadas:** `list`, `dict`, `set` — ¡el reto se llama colecciones por algo! 🐍

---

## 🛡️ `validations.py` — El Guardián de Datos

Nada entra al catálogo sin pasar por este filtro. Las validaciones lanzan `ValueError` con mensajes claros.

```python
# Estados permitidos (set para búsqueda O(1))
allowed_statuses = {"disponible", "reservado", "vendida"}

# Palabras clave requeridas en la descripción
required_keywords = {"usada", "certificada"}
```

| Función | ¿Qué valida? |
|---------|-------------|
| `validate_not_empty(value, field)` | Que el campo no sea vacío ni solo espacios |
| `validate_price(price)` | Que el precio sea un número válido y mayor a `0` |
| `validate_status(status)` | Que el estado sea uno de los tres permitidos |
| `validate_description(description)` | Que incluya `'usada'` o `'certificada'` |

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
       └───────────────┴───────────────┘
                        │
                        ▼
              ┌─────────────────┐
              │ validations.py  │  ← Guardián de datos
              └────────┬────────┘
                       │
                        ▼
              ┌─────────────────┐
              │ catalog: list   │  ← [{"id":..., "name":..., ...}]
              │    de dicts     │
              └─────────────────┘
```

---

## 💡 Decisiones de Diseño

| Decisión | Razón |
|----------|-------|
| **Sin clases / Sin OOP** | El reto apunta al uso de colecciones nativas (`list`, `dict`, `set`) |
| **Separación de responsabilidades** | `main.py` → UI · `catalog.py` → lógica · `validations.py` → datos |
| **Funciones puras** | Sin efectos secundarios inesperados; reciben y devuelven datos |
| **`set` para validaciones** | Búsqueda en O(1) en vez de O(n) con `list` |
| **`__name__ == "__main__"`** | `main()` solo se ejecuta como punto de entrada, no al importar |

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
