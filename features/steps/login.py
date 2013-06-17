from behave import *
from main_program import *

@given('I enter my username as "{username}" and my password as "{password}"')
def impl(context, username, password):
    assert login(username, password) is False