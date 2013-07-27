from behave import given, when, then
from Navigator import Navigator
from getpass import getpass

nav = Navigator()
nav.clearBrowser() # We will need to clear "br" since br is using mechanize which is a module and can't be instantiated multiple times, only once


@given('I am logged in')
def impl(context):
    if (nav.logged_in is False):
        username = getpass('PID: ')
        password = getpass()
        nav.logged_in = nav.login(username, password)

    assert nav.logged_in is True


@given('I enter an incorrect CRN number "{entered_crn}" and my course info is checked')
def impl(context, entered_crn):
    context.response = nav.validCourseInfo(crn=entered_crn, subj="", crse="")
    context.expected_errors = ["Please enter a valid CRN"]  # We are expecting this error


@given('I enter a correct CRN number "{entered_crn}" and my course info is checked')
def impl(context, entered_crn):
    context.response = nav.validCourseInfo(crn=entered_crn, subj="", crse="")
    context.expected_errors = ""


@then('I will see "{error_message}"')
def impl(context, error_message):
    try:
        assert set(context.expected_errors) == set(context.response)  # Other wise compare expected_errors and response as sets since the order of the errors isn't important

    except AssertionError as e:
        if (error_message == "Nothing"):
            m = "Expected Errors: None ; Returned Errors: " + str(context.response)
            m = m.split(" ; ")
            m = tuple(m)
            e.args += (m)
        else:
            e.args += ('Expected Errors: ' , context.expected_errors , ' Returned Errors: ' , context.response)
        raise e







