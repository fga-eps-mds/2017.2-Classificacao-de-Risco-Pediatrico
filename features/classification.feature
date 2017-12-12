Feature: In order to make classifications

  Scenario Outline: Do classification
    #create a patient
    When I access register/user/
    And  fill information fields with data: <name>, <id_number> and <profile_number>
    And I click the submit button
    And I log into server with data: <email> and <password>
    And I click in register patient
    And I fill patient form
    Then it should redirect me to the <url> page
    When I click in patient: <id_patient>
    And I insert symptoms and classify <id_patient>
    And I click on save for <id_patient>
    Then should update de classification of <id_patient>

    Examples:
      | name            | id_number | profile_number | email                       | password         | url   | id_patient |
      | selenium-user-3 | 3         | 2              | selenium-user-3-3@gmail.com | selenium-user123 | home/ | 1          |
