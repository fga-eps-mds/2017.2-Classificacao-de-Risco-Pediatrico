Feature: In order to make classifications

  Scenario Outline:
    Given I register an employee: <name_user>, <id_number_user> and <profile_number_user>
    Given I register a patient: <name_patient>, <id_number_patient> and <profile_number_patient>
    And I realize a classification: <id_number_patient>
    Then The classification must be updated

    Examples:
      | name_user            | id_number_user | profile_number_user | url_user            | name_patient    | id_number_patient | profile_number_patient | email_                       | password_         | url_   |
      | selenium-user-1      | 1              | 1                   | login               | selenium-user-3 | 1                 | 2                      | selenium-user-3-3@gmail.com  | selenium-user123  | home/  |
