from behave import *

@given('I enter my username as "{username}" and my password as "{password}"')
def impl(context, username, password):
    import main_program
    x = raw_input('co   ')
    assert main_program.login(username, password) is False