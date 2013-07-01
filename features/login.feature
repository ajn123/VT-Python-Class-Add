Feature: Logging in

    @login @travis
    Scenario: Wrong Username and Password
        Given I enter my username as "fake_user" and my password as "fake_password"

    @login
    Scenario: Correct Username and Password
        Given I enter my own username and password
