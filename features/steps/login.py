from behave import given
from Navigator import Navigator
from getpass import getpass

nav = Navigator()


@given('I try to login with "{username}" as my username and "{password}" as my password, then I should not be able to log in')
def impl(context, username, password):
    assert nav.login(username, password) is False


@given('I try to login with my own username and password, then I should be able to log in')
def impl(context):
    username = getpass('PID: ')
    password = getpass()
    assert nav.login(username, password) is True
