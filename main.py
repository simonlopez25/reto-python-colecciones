from catalog import (
    add_piece,
    filter_by_status,
    find_piece_by_id,
    get_average_price,
    list_pieces,
    remove_piece,
)


def display_menu() -> None:
    print("\n" + "=" * 40)
    print("      CATÁLOGO DE COLECCIONABLES")
    print("=" * 40)
    print("1. Agregar una pieza")
    print("2. Mostrar todas las piezas")
    print("3. Mostrar piezas disponibles")
    print("4. Mostrar el precio promedio")
    print("5. Buscar una pieza por identificador")
    print("6. Eliminar una pieza")
    print("7. Salir")
    print("=" * 40)


def handle_add_piece(catalog: list) -> None:
    print("\n--- AGREGAR NUEVA PIEZA ---")
    piece_id = input("ID de la pieza: ")
    name = input("Nombre de la pieza: ")
    category = input("Categoría: ")

    price_raw = input("Precio: ")
    try:
        price = float(price_raw)
    except ValueError:
        print(" Error: El precio debe ser un número válido.")
        return

    status = input("Estado (disponible, reservada, vendida): ")
    description = input("Descripción (debe incluir 'usada' o 'certificada'): ")

    try:
        new_piece = add_piece(piece_id, name, category, price, status, description)
        catalog.append(new_piece)
        print(f" ¡Pieza '{new_piece['name']}' agregada con éxito!")
    except ValueError as error:
        print(f" Error de validación: {error}")


def handle_list_pieces(catalog: list) -> None:
    print("\n--- LISTA DE PIEZAS ---")
    pieces = list_pieces(catalog)
    if not pieces:
        print("El catálogo está vacío.")
        return

    for position, piece_name in enumerate(pieces, start=1):
        print(f"{position}. {piece_name}")


def handle_list_available(catalog: list) -> None:
    print("\n--- PIEZAS DISPONIBLES ---")
    try:
        available = filter_by_status(catalog, "disponible")
        if not available:
            print("No hay piezas disponibles en este momento.")
            return

        for piece in available:
            print(f"- [{piece['id']}] {piece['name']} (${piece['price']:.2f})")
    except ValueError as error:
        print(f" Error: {error}")


def handle_average_price(catalog: list) -> None:
    print("\n--- PRECIO PROMEDIO ---")
    avg = get_average_price(catalog)
    print(f"El precio promedio del catálogo es: ${avg:.2f}")


def handle_find_piece(catalog: list) -> None:
    print("\n--- BUSCAR PIEZA ---")
    piece_id = input("Ingrese el ID a buscar: ")
    piece = find_piece_by_id(catalog, piece_id)

    if piece is None:
        print(f" No se encontró ninguna pieza con el ID '{piece_id}'.")
    else:
        print("\nDetalles de la pieza:")
        print(f"  ID:          {piece['id']}")
        print(f"  Nombre:      {piece['name']}")
        print(f"  Categoría:   {piece['category']}")
        print(f"  Precio:      ${piece['price']:.2f}")
        print(f"  Estado:      {piece['status']}")
        print(f"  Descripción: {piece['description']}")


def handle_remove_piece(catalog: list) -> None:
    print("\n--- ELIMINAR PIEZA ---")
    piece_id = input("Ingrese el ID de la pieza a eliminar: ")
    if remove_piece(catalog, piece_id):
        print(f" Pieza con ID '{piece_id}' eliminada correctamente.")
    else:
        print(f" No se pudo eliminar. No existe la pieza con ID '{piece_id}'.")


def main() -> None:
    catalog = []

    while True:
        display_menu()
        option = input("Seleccione una opción (1-7): ").strip()

        if option == "1":
            handle_add_piece(catalog)
        elif option == "2":
            handle_list_pieces(catalog)
        elif option == "3":
            handle_list_available(catalog)
        elif option == "4":
            handle_average_price(catalog)
        elif option == "5":
            handle_find_piece(catalog)
        elif option == "6":
            handle_remove_piece(catalog)
        elif option == "7":
            print("\n¡Gracias por utilizar el Catálogo de Coleccionables!")
            break
        else:
            print(" Opción no válida. Por favor, seleccione un número entre 1 y 7.")

if __name__ == "__main__": # me ayuda a siempre ejecutar primero la main, Python le asigna a __name__ el valor de "__main__".
    main()