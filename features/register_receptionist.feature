Feature: In order to use the system
    I want to register a employee

    Scenario: Register a receptionist
        When we acess the register page
        And select the profile "receptionist"
        And  fiel the information fields
        When i click the cadastrar button
        Then it should redirect me to the "login" page

    # Scenario: Register a attendant
    #     When we acess the register page
    #     And select the profile "attendant"
    #     And  fiel the information fields
    #     When i click the cadastrar button
    #     Then it should redirect me to the "login" page
