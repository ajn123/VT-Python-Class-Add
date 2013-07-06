Feature: Valid Course Information
    Background:
        Given I am logged in

    @valid @human
    Scenario: Incorrect CRN Length
        Given I enter in the CRN number "923" and my course info is checked
        Then I will see "Please enter a CRN number that is 5 digits"

    @valid @human
    Scenario: Correct CRN Length
        Given I enter in the CRN number "92383" and my course info is checked
        Then I will see "Nothing"
