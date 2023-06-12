Feature: Generate Vehicle Descriptions
  As a vehicle description service user
  I want to generate descriptions for vehicles
  So that I can provide comprehensive information to customers.

  Scenario: Generate Description for Known Vehicle
    Given details about a specific vehicle are available
    And the AI description generator is functional
    When the user requests a description for this vehicle
    Then the Description Service provides a description for that vehicle
