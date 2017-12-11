Feature: In order to make a quantitative analisis
  I want to see the classifications chart

  Scenario Outline: See the classifications chart
    When I access register/user/
    And  fill information fields with data: <name>, <id_number> and <profile_number>
    And I click the submit button
    And I log into server with data: <email> and <password>
    And I click on Estatísticas
    And I click on Gráfico de Classificações
    Then it should redirect me to the <url> page

    Examples:
      | name            | id_number | profile_number | email                       | password         | url                    |
      | selenium-user-4 | 4         | 1              | selenium-user-4-4@gmail.com | selenium-user123 | classifications_chart/ |
