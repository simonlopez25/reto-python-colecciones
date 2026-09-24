import pytest
from catalog import *


@pytest.fixture
def sample_catalog():
    return [
        {
            "id": "1",
            "name": "Anillo de Oro",
            "category": "Joyería",
            "price": 150.0,
            "status": "disponible",
            "description": "Anillo de oro de 18k certificado",
        },
        {
            "id": "2",
            "name": "Reloj Vintage",
            "category": "Joyería",
            "price": 300.0,
            "status": "vendido",
            "description": "Reloj de usada",
        },
        {
            "id": "3",
            "name": "Silla Antigua",
            "category": "Muebles",
            "price": 80.0,
            "status": "disponible",
            "description": "Silla de madera usada",
        },
    ]


def test_add_piece_success(sample_catalog):
    result = add_piece(
        catalog=sample_catalog,
        piece_id=" 10 ",
        name=" Collar de Plata ",
        category=" Joyería ",
        price=120.0,
        status=" DISPONIBLE ",
        description=" Collar certificada en buen estado ",
    )
    assert result == {
        "id": "10",
        "name": "Collar de Plata",
        "category": "Joyería",
        "price": 120.0,
        "status": "disponible",
        "description": "Collar certificada en buen estado",
    }
    assert len(sample_catalog) == 4
    assert piece_exists(sample_catalog, "10") is True


def test_add_piece_duplicate_id(sample_catalog):
    with pytest.raises(ValueError, match="Ya existe una pieza con el ID '1'."):
        add_piece(
            catalog=sample_catalog,
            piece_id="1",
            name="Anillo Duplicado",
            category="Joyería",
            price=100.0,
            status="disponible",
            description="Descripción de prueba",
        )


def test_list_pieces(sample_catalog):
    names = list_pieces(sample_catalog)
    assert names == ["Anillo de Oro", "Reloj Vintage", "Silla Antigua"]


def test_find_piece_by_id_found(sample_catalog):
    piece = find_piece_by_id(sample_catalog, "2")
    assert piece is not None
    assert piece["name"] == "Reloj Vintage"


def test_find_piece_by_id_not_found(sample_catalog):
    piece = find_piece_by_id(sample_catalog, "999")
    assert piece is None


def test_piece_exists(sample_catalog):
    assert piece_exists(sample_catalog, "1") is True
    assert piece_exists(sample_catalog, "999") is False


def test_remove_piece_success(sample_catalog):
    result = remove_piece(sample_catalog, "1")
    assert result is True
    assert len(sample_catalog) == 2
    assert piece_exists(sample_catalog, "1") is False


def test_remove_piece_not_found(sample_catalog):
    result = remove_piece(sample_catalog, "999")
    assert result is False
    assert len(sample_catalog) == 3


def test_get_catalog_summary(sample_catalog):
    summary = get_catalog_summary(sample_catalog)
    assert summary == {"Joyería": 2, "Muebles": 1}


def test_get_pieces_by_category(sample_catalog):
    jewelry = get_pieces_by_category(sample_catalog, "JOYERÍA")
    assert jewelry == ["Anillo de Oro", "Reloj Vintage"]


def test_filter_by_status(sample_catalog):
    available = filter_by_status(sample_catalog, "disponible")
    assert len(available) == 2
    assert all(p["status"] == "disponible" for p in available)


def test_filter_by_min_price(sample_catalog):
    expensive = filter_by_min_price(sample_catalog, 100.0)
    assert len(expensive) == 2


def test_filter_by_min_price_invalid_type(sample_catalog):
    with pytest.raises(ValueError, match="El precio mínimo debe ser un valor numérico."):
        filter_by_min_price(sample_catalog, "100")


def test_get_average_price(sample_catalog):
    avg = get_average_price(sample_catalog)
    assert avg == round((150.0 + 300.0 + 80.0) / 3, 2)


def test_get_average_price_empty_catalog():
    assert get_average_price([]) == 0.0


def test_catalog_invalid_type():
    with pytest.raises(TypeError, match="El catálogo debe ser una lista."):
        list_pieces("no_es_una_lista")