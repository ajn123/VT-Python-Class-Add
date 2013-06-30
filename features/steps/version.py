from behave import *
from main_program import *

@given('I have Python {version} installed')
def impl(context, version):
    version = version.split(".")
    version = tuple(version)
    major, minor, micro = version

@when('I try to run the program')
def impl(context):
    checkVersion()

@then('I should see {message}')
def impl(context, message):
    print message
