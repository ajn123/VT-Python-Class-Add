from behave import given, when, then
from main_program import Navigator
from getpass import getpass

nav = Navigator()

entered_crn, entered_term, entered_year, entered_subj, entered_crse = "", "09", "2013", "", ""

@given('I am logged in')
def impl(context):
    if (if nav.logged_in is False):
        username = getpass('PID: ')
        password = getpass()
        nav.logged_in = nav.login(username, password)

    assert nav.logged_in is True


@given('I enter in the CRN number "{entered_crn}" and my course info is checked')
def impl(context, entered_crn):
    context.response = nav.validCourseInfo(crn=entered_crn)


@then('I will see "{message}"')
def impl(context, message):
    if message == "Nothing":
        assert context.response is True
    else:
        assert message == context.response
