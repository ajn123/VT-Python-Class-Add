from behave import *
import main_program

@given('Given I am logged in')
def impl(context, username, password):
    assert main_program.login(username, password) is False


@given('I enter in the CRN "{crn}" and TERM "{term}" and YEAR "{year}"')
def impl(context, crn, term, year):
    findByCRN(crn, term, year)