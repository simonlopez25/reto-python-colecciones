from validations import (
    validate_description,
    validate_not_empty,
    validate_price,
    validate_status,
)


def add_piece(
        piece_id: str,
        name: str,
        category: str,
        price: float,
        status: str,
        description: str,
) -> dict:
    validate_not_empty(piece_id, "id")
    validate_not_empty(name, "name")
    validate_not_empty(category, "category")

    validate_price(price)
    validate_status(status)
    validate_description(description)

    return {
        "id": piece_id.strip(),
        "name": name.strip(),
        "category": category.strip(),
        "price": price,
        "status": status.strip().lower(),
        "description": description.strip(),
    }


def list_pieces(catalog: list) -> list:
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    return [piece["name"] for piece in catalog]


def find_piece_by_id(catalog: list, piece_id: str) -> dict | None:
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    clean_id = piece_id.strip()

    for piece in catalog:
        if piece["id"] == clean_id:
            return piece
    return None


def remove_piece(catalog: list, piece_id: str) -> bool:
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    try:
        piece = find_piece_by_id(catalog, piece_id)

        if piece is None:
            raise ValueError(f"No se encontró ninguna pieza con el ID '{piece_id}'.")
        catalog.remove(piece)
        return True
    except ValueError:
        return False


def get_catalog_summary(catalog: list) -> dict:
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    summary = {}
    for piece in catalog:
        category = piece["category"]
        summary[category] = summary.get(category, 0) + 1  # suma de 1 los productos que compartan las misma categoria
    return summary


def get_pieces_by_category(catalog: list, category: str) -> list:
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    clean_category = category.strip().lower()
    return [
        piece["name"]
        for piece in catalog
        if piece["category"].lower() == clean_category
    ]


def piece_exists(catalog: list, piece_id: str) -> bool:
    return find_piece_by_id(catalog, piece_id) is not None


def filter_by_status(catalog: list, status: str) -> list:
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")
    validate_status(status)
    clean_status = status.strip().lower()

    return [piece for piece in catalog if piece["status"] == clean_status]


def filter_by_min_price(catalog: list, min_price: float) -> list:
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    if not isinstance(min_price, (int, float)) or isinstance(min_price, bool):
        raise ValueError("El precio mínimo debe ser un valor numérico.")

    return [piece for piece in catalog if piece["price"] > min_price]


def get_average_price(catalog: list) -> float:
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")

    if not catalog:
        return 0.0

    total_price = sum(piece["price"] for piece in catalog)
    return round(total_price / len(catalog), 2)
