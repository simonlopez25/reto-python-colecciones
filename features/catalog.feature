# language: en
Feature: Piece catalog management

  # Test: test_add_piece_success
  Scenario: Add a new valid piece to the catalog
    Given a sample catalog with 3 pieces exists
    When a piece with ID "10" and valid data is added
    Then the piece is registered successfully and the catalog now has 4 pieces

  # Test: test_add_piece_duplicate_id
  Scenario: Reject piece with duplicate ID
    Given a sample catalog with 3 pieces exists
    When attempting to add a piece with ID "1"
    Then the system returns the error "Ya existe una pieza con el ID '1'."

  # Test: test_list_pieces
  Scenario: List the names of all pieces
    Given a sample catalog with 3 pieces exists
    When requesting the list of pieces
    Then the system returns the names ["Anillo de Oro", "Reloj Vintage", "Silla Antigua"]

  # Test: test_find_piece_by_id_found
  Scenario: Find a piece by an existing ID
    Given a sample catalog with 3 pieces exists
    When searching for the piece with ID "2"
    Then the system returns the piece "Reloj Vintage"

  # Test: test_find_piece_by_id_not_found
  Scenario: Find a piece by a non-existent ID
    Given a sample catalog with 3 pieces exists
    When searching for the piece with ID "999"
    Then the system returns no piece

  # Test: test_piece_exists
  Scenario: Verify if a piece exists
    Given a sample catalog with 3 pieces exists
    When checking if ID "1" exists
    Then the system confirms that the piece exists

  # Test: test_remove_piece_success
  Scenario: Remove an existing piece from the catalog
    Given a sample catalog with 3 pieces exists
    When removing the piece with ID "1"
    Then the removal is successful and the catalog now has 2 pieces

  # Test: test_remove_piece_not_found
  Scenario: Attempt to remove a non-existent piece
    Given a sample catalog with 3 pieces exists
    When attempting to remove the piece with ID "999"
    Then the system returns False and keeps all 3 pieces

  # Test: test_get_catalog_summary
  Scenario: Get catalog summary by category
    Given a sample catalog with 3 pieces exists
    When calculating the category summary
    Then the system returns 2 pieces in "Joyería" and 1 in "Muebles"

  # Test: test_get_pieces_by_category
  Scenario: Filter pieces by category
    Given a sample catalog with 3 pieces exists
    When filtering pieces by the category "JOYERÍA"
    Then the system returns ["Anillo de Oro", "Reloj Vintage"]

  # Test: test_filter_by_status
  Scenario: Filter pieces by status
    Given a sample catalog with 3 pieces exists
    When filtering pieces by status "disponible"
    Then the system returns 2 available pieces

  # Test: test_filter_by_min_price
  Scenario: Filter pieces by minimum price
    Given a sample catalog with 3 pieces exists
    When filtering pieces with a minimum price of 100.0
    Then the system returns 2 pieces

  # Test: test_filter_by_min_price_invalid_type
  Scenario: Reject non-numeric data type when filtering by minimum price
    Given a sample catalog with 3 pieces exists
    When attempting to filter by minimum price with text "100"
    Then the system returns the error "El precio mínimo debe ser un valor numérico."

  # Test: test_get_average_price
  Scenario: Calculate the average price of pieces
    Given a sample catalog with 3 pieces exists
    When calculating the average price
    Then the average result matches the expected value based on registered prices

  # Test: test_get_average_price_empty_catalog
  Scenario: Calculate average price on an empty catalog
    Given an empty piece catalog
    When calculating the average price
    Then the system returns 0.0

  # Test: test_catalog_invalid_type
  Scenario: Validate catalog structured data type
    Given an invalid catalog value "no_es_una_lista"
    When requesting to list pieces
    Then the system returns the error "El catálogo debe ser una lista."