Feature: In order to make classifications

  Scenario Outline:
    Given I register an employee: <name>, <id_number> and <profile_number>
    Given I register patient: <name_patient>, <id_number_patient> and <profile_number_patient>and: <email> and <password>
    And I realize a classification: <id_number_patient>
    Then The classification must be updated

    Examples:
      | name            | id_number | profile_number | url            | name_patient    | id_number_patient | profile_number_patient | email                       | password         | url   |
      | selenium-user-1 | 1         | 1              | login          | selenium-user-3 | 1                 | 2                      | selenium-user-3-3@gmail.com | selenium-user123 | home/ |


