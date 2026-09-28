# language: en
Feature: Main menu user interface and console flow

  # Test: test_display_menu
  Scenario: Display main menu options
    Given the user starts the application
    When the main menu is displayed
    Then the console should show the title "CATÁLOGO DE COLECCIONABLES" and the options "1. Agregar una pieza" and "7. Salir"

  # Test: test_main_exit_option
  Scenario: Select system exit option
    Given the application is at the main menu
    When the user enters the option "7"
    Then the system terminates execution and shows the message "¡Gracias por utilizar el Catálogo de Coleccionables!"

  # Test: test_handle_add_piece_success
  Scenario: Add a piece interactively via console
    Given an empty piece catalog
    When the user sequentially enters valid inputs "10", "Jarra Antigua", "Cerámica", "50.0", "disponible", and "Pieza usada en buen estado"
    Then the system shows the confirmation "agregada con éxito" and stores the piece in the catalog

  # Test: test_handle_list_pieces_empty
  Scenario: Attempt to list pieces in an empty catalog
    Given an empty piece catalog
    When the user requests to list the catalog pieces
    Then the console shows the message "El catálogo está vacío."

  # Test: test_handle_list_pieces_with_items
  Scenario: List registered pieces correctly
    Given a catalog containing the pieces "Reloj Vintage" and "Cuadro Antiguo"
    When the user requests to view the list of pieces
    Then the console displays in numbered format "1. Reloj Vintage" and "2. Cuadro Antiguo"