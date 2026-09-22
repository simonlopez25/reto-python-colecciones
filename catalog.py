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