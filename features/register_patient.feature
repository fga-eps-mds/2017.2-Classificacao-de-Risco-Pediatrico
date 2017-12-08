Feature: In order to make classifications
  I want to register a patient

  Scenario Outline: Register a patient
    When I access register/user/
    And  fill information fields with data: <name>, <id_number> and <profile_number>
    And I click the submit button
    And I log into server with data: <email> and <password>
    And I click in register patient
    And I fill patient form
    Then it should redirect me to the <url> page

    Examples:
      | name            | id_number | profile_number | email                       | password         | url   |
      | selenium-user-4 | 4         | 2              | selenium-user-4-4@gmail.com | selenium-user123 | home/ |
