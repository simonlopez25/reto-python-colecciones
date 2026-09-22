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
