from main import *

def test_display_menu(capsys):
    display_menu()
    captured = capsys.readouterr()
    assert "CATÁLOGO DE COLECCIONABLES" in captured.out
    assert "1. Agregar una pieza" in captured.out
    assert "7. Salir" in captured.out


def test_handle_add_piece_success(monkeypatch, capsys):
    catalog = []
    inputs = iter([
        "10",
        "Jarra Antigua",
        "Cerámica",
        "50.0",
        "disponible",
        "Pieza usada en buen estado",
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    handle_add_piece(catalog)

    captured = capsys.readouterr()
    assert "agregada con éxito" in captured.out
    assert len(catalog) == 1
    assert catalog[0]["name"] == "Jarra Antigua"


def test_handle_list_pieces_empty(capsys):
    catalog = []
    handle_list_pieces(catalog)
    captured = capsys.readouterr()
    assert "El catálogo está vacío." in captured.out


def test_handle_list_pieces_with_items(capsys):
    catalog = [{"name": "Reloj Vintage"}, {"name": "Cuadro Antiguo"}]
    handle_list_pieces(catalog)
    captured = capsys.readouterr()
    assert "1. Reloj Vintage" in captured.out
    assert "2. Cuadro Antiguo" in captured.out


def test_main_exit_option(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "7")

    main()

    captured = capsys.readouterr()
    assert "¡Gracias por utilizar el Catálogo de Coleccionables!" in captured.out
