Feature: Logging in

    @login @travis
    Scenario: Wrong Username and Password
        Given I try to login with "user123" as my username and "pass123" as my password, then I should not be able to log in

    @login @human
    Scenario: Correct Username and Password
        Given I try to login with my own username and password, then I should be able to log in
