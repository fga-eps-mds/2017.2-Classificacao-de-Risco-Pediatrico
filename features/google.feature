Feature: testing google

    Scenario: visit google and check
        When we visit google
        Then it should have a title "Google"