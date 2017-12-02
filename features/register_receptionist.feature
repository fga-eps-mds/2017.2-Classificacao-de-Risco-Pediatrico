Feature: In order to use the system
  I want to register a employee

  Scenario Outline: Register a receptionist or an attendant
    When we access register/user/
    And  fill information fields with data: <name> and <profile_number>
    And I click the submit button
    Then it should redirect me to the <url> page

    Examples:
      | name            | profile_number | url   |
      | selenium-user-1 | 1              | login |
      | selenium-user-2 | 2              | login |
