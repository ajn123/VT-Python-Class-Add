from behave import *
from main_program import *
import sys

@given('I enter my username as "{username}" and my password as "{password}"')
def impl(context, username, password):
    assert login(username, password) is False

@given('I enter my own username and password')
def impl(context):
    username = getpass('PID: ')
    password = getpass()
    assert login(username, password) is True
