from behave import *
from main_program import *

major, minor, micro = "", "", ""
actual_message = ""
expected_message = ""

@given('I have Python {version} installed')
def impl(context, version):
    if version == "2.7.4":
        expected_message = None
    elif version == "2.9.9":
        expected_message = "Warning:"
    elif version == "3.0.1":
        expected_message = "Error:"

    version = version.split(".")
    version = tuple(version)
    global major, minor, micro
    major, minor, micro = version

@when('I try to check my version')
def impl(context):
    actual_message = checkVersion(major, minor, micro)

@then('I should see {expected}')
def impl(context, expected):
    try:
        assert expected_message in actual_message
    except AssertionError as e:
        e.args += ('Expected Message: ', expected_message, 'Actual Message: ', actual_message)
        raise


