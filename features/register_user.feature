Feature: In order to use the system
  I want to register an employee

  Scenario Outline: Register a receptionist or an attendant
    When I access register/user/
    And fill information fields with data: <name>, <id_number> and <profile_number>
    And I click the submit button
    Then it should redirect me to the <url> page

    Examples:
      | name            | id_number | profile_number | url            |
      | selenium-user-1 | 1         | 1              | login          |
      | selenium-user-2 | 2         | 2              | login          |
      # it remains on the same page because has the same or invalid user data, then it fails to register
      | selenium-user-2 | 2         | 2              | register/user/ |
