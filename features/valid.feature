Feature: Valid Course Information
    Background:
        Given I am logged in

    @valid
    Scenario: Incorrect CRN Length
        Given I enter in the CRN number "923"
        When my course info is checked
        Then I should see "Please Enter a CRN number that is 5 digits or enter a subject and course number"

    @valid
    Scenario: Correct CRN Length
        Given I enter in the CRN number "92083"
        When my course info is checked
        Then I should see no message




    Scenario: Enter Subject and Course Number
        Given I enter in the subject "CS" and the course number "3114"
        When I click the submit button
        Then I should see a list of classes.
        Given I enter in the CRN number "92083"
        When I click the submit button
        Then my class should show up
