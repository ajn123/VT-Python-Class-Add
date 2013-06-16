Feature: Searching Classes
    Background:
        Given I am logged in

    Scenario: Enter CRN Number
        Given I enter in the CRN number "92083"
        When I click the submit button
        Then my class should show up

    Scenario: Enter Subject and Course Number
        Given I enter in the subject "CS" and the course number "3114"
        When I click the submit button
        Then I should see a list of classes.
        Given I enter in the CRN number "92083"
        When I click the submit button
        Then my class should show up