Feature: Ping
  Feature Description

  Scenario: 404
    When I query a nonexistent endpoint
    Then I get error code 404

  Scenario: Ping
    When I request a ping
    Then I get a pong back
