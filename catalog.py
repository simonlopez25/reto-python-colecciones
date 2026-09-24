from validations import *

def _validate_catalog(catalog: list):
    if not isinstance(catalog, list):
        raise TypeError("El catálogo debe ser una lista.")


def add_piece(
        catalog: list,
        piece_id: str,
        name: str,
        category: str,
        price: float,
        status: str,
        description: str,
) -> dict:
    _validate_catalog(catalog)

    validate_not_empty(piece_id, "id")
    validate_not_empty(name, "name")
    validate_not_empty(category, "category")

    validate_price(price)
    validate_status(status)
    validate_description(description)

    clean_id = piece_id.strip()

    if piece_exists(catalog, clean_id):
        raise ValueError(f"Ya existe una pieza con el ID '{clean_id}'.")

    new_piece = {
        "id": clean_id,
        "name": name.strip(),
        "category": category.strip(),
        "price": float(price),
        "status": status.strip().lower(),
        "description": description.strip(),
    }

    catalog.append(new_piece)
    return new_piece


def list_pieces(catalog: list) -> list:
    _validate_catalog(catalog)
    return [piece["name"] for piece in catalog]


def find_piece_by_id(catalog: list, piece_id: str) -> dict | None:
    _validate_catalog(catalog)
    clean_id = str(piece_id).strip()

    for piece in catalog:
        if piece["id"] == clean_id:
            return piece
    return None


def remove_piece(catalog: list, piece_id: str) -> bool:
    _validate_catalog(catalog)
    try:
        piece = find_piece_by_id(catalog, piece_id)

        if piece is None:
            raise ValueError(f"No se encontró ninguna pieza con el ID '{piece_id}'.")
        catalog.remove(piece)
        return True
    except ValueError:
        return False


def get_catalog_summary(catalog: list) -> dict:
    _validate_catalog(catalog)
    summary = {}
    for piece in catalog:
        category = piece["category"]
        summary[category] = summary.get(category, 0) + 1
    return summary


def get_pieces_by_category(catalog: list, category: str) -> list:
    _validate_catalog(catalog)
    clean_category = category.strip().lower()
    return [
        piece["name"]
        for piece in catalog
        if piece["category"].strip().lower() == clean_category
    ]


def piece_exists(catalog: list, piece_id: str) -> bool:
    return find_piece_by_id(catalog, piece_id) is not None


def filter_by_status(catalog: list, status: str) -> list:
    _validate_catalog(catalog)
    validate_status(status)
    clean_status = status.strip().lower()

    return [piece for piece in catalog if piece["status"] == clean_status]


def filter_by_min_price(catalog: list, min_price: float) -> list:
    _validate_catalog(catalog)

    if not isinstance(min_price, (int, float)) or isinstance(min_price, bool):
        raise ValueError("El precio mínimo debe ser un valor numérico.")

    return [piece for piece in catalog if piece["price"] >= min_price]


def get_average_price(catalog: list) -> float:
    _validate_catalog(catalog)

    if not catalog:
        return 0.0

    total_price = sum(piece["price"] for piece in catalog)
    return round(total_price / len(catalog), 2)
