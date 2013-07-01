from behave import *
import main_program

entered_crn, entered_term, entered_year, entered_subj, entered_crse = "", "09", "2013", "", ""

@given('I am logged in')
def impl(context):
    username = getpass('PID: ')
    password = getpass()
    assert main_program.login(username, password) is True

@given('I enter in the CRN number "{crn}"')
def impl(context, crn):
    entered_crn = crn

@when('my course info is checked')
def impl(context):
    main_program.checkCourseInfo(entered_crn, entered_term, entered_year, entered_subj, entered_crse)

@when('I should see "{message}')
def impl(context, message):
    print "ok"
