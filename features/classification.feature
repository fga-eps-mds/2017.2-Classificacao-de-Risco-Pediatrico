Feature: In order to make classifications

  Scenario Outline:
    When I access register/user/
    Given I register an employee: <name>, <id_number> and <profile_number_user>
    And I log into server with data: <email> and <password>
    Then it should redirect me to the <url> page
    Given I register a patient: <name_patient>, <id_number_patient> and <profile_number_patient>
    Then it should redirect me to the <url> page
    And I realize a classification: <id_number_patient>
    Then The classification must be updated

    Examples:
      | name                 | id_number      | profile_number_user | url_user            | name_patient    | id_number_patient | profile_number_patient | email                       | password         | url   |
      | selenium-user-3      | 3              | 2                   | login               | selenium-user-3 | 3                 | 2                      | selenium-user-3-3@gmail.com | selenium-user123 | home/ |
