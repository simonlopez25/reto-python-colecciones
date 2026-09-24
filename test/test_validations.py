import pytest
from validations import *


def test_validate_not_empty_success():
    validate_not_empty("Anillo", "nombre")


# @pytest.mark.parametrize se utiliza para ejecutar la misma función de prueba múltiples veces utilizando diferentes conjuntos de datos de entrada, sin necesidad de duplicar código o escribir varios bucles for dentro de un mismo test.
@pytest.mark.parametrize("invalid_value", ["", "   ", None, 123])
def test_validate_not_empty_invalid(invalid_value):
    with pytest.raises(ValueError, match="El campo 'nombre' no puede estar vacío."):
        validate_not_empty(invalid_value, "nombre")


def test_validate_price_success():
    validate_price(150.0)
    validate_price(10)


@pytest.mark.parametrize("invalid_price", [0, -50.0, -1])
def test_validate_price_negative_or_zero(invalid_price):
    with pytest.raises(ValueError, match="El precio debe ser mayor que 0"):
        validate_price(invalid_price)


@pytest.mark.parametrize("invalid_type", ["100", True, False, [10]])
def test_validate_price_invalid_type(invalid_type):
    with pytest.raises(ValueError, match="El precio debe ser un valor numérico."):
        validate_price(invalid_type)


@pytest.mark.parametrize("status", ["disponible", "reservado", "reservada", "vendida", " DISPONIBLE "])
def test_validate_status_success(status):
    validate_status(status)


@pytest.mark.parametrize("invalid_status", ["nuevo", "en stock", "vendido_mal"])
def test_validate_status_invalid(invalid_status):
    with pytest.raises(ValueError, match="no válido. Estados permitidos:"):
        validate_status(invalid_status)


@pytest.mark.parametrize("desc", [
    "Pieza usada en buen estado",
    "Joya certificada por experto",
    " USADA Y CERTIFICADA ",
])
def test_validate_description_success(desc):
    validate_description(desc)


def test_validate_description_missing_keywords():
    with pytest.raises(ValueError, match="La descripción debe incluir las palabras 'usada' o 'certificada'."):
        validate_description("Pieza en excelente estado sin más detalles")
