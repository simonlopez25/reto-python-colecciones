# language: en
Feature: Product input data validation

  # Test: test_validate_not_empty_success
  Scenario: Register a valid name
    Given the name "Anillo" is entered
    When the product name is validated
    Then the registration is successful

  # Test: test_validate_not_empty_invalid
  Scenario: Reject empty name
    Given an empty text is entered for the name
    When the product name is validated
    Then the system returns the error "El campo 'nombre' no puede estar vacío."


  # Test: test_validate_price_success
  Scenario: Register a positive price
    Given the price 150.0 is entered
    When the product price is validated
    Then the registration is successful

  # Test: test_validate_price_negative_or_zero
  Scenario: Reject price less than or equal to zero
    Given the price -50.0 is entered
    When the product price is validated
    Then the system returns the error "El precio debe ser mayor que 0"

  # Test: test_validate_price_invalid_type
  Scenario: Reject non-numeric price
    Given the price "100" is entered
    When the product price is validated
    Then the system returns the error "El precio debe ser un valor numérico."


  # Test: test_validate_status_success
  Scenario: Allow valid status
    Given the status "disponible" is assigned
    When the product status is validated
    Then the registration is successful

  # Test: test_validate_status_invalid
  Scenario: Reject invalid status
    Given the status "nuevo" is assigned
    When the product status is validated
    Then the system returns the error "no válido. Estados permitidos:"


  # Test: test_validate_description_success
  Scenario: Register description with keyword
    Given the description "Pieza usada en buen estado" is entered
    When the product description is validated
    Then the registration is successful

  # Test: test_validate_description_missing_keywords
  Scenario: Reject description without keyword
    Given the description "Pieza en excelente estado sin más detalles" is entered
    When the product description is validated
    Then the system returns the error "La descripción debe incluir las palabras 'usada' o 'certificada'."