Feature: In order to use the system
    I want to register a employee
    I want to registe a receptionist

    Scenario: Register a receptionist
        When we are at register page
        When information fiels are filled
        And i click the cadastrar button
        Then it should redirect me to the "login" page
