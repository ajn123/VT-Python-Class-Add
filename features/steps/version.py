from behave import given, when, then
from Navigator import Navigator

nav = Navigator()


@given('I have Python {version} installed')
def impl(context, version):
    version = version.split(".")  # Create a list from the string
    context.version = version  # Save the list


@when('I try to check my version')
def impl(context):
    context.actual = str(nav.checkVersion(*context.version))  # Unpack the list arguments


@then('I should see "{expected}" in my message')
def impl(context, expected):
    if (expected == "Nothing"):
        assert "" in context.actual  # We aren't expecting anything
    else:
        assert expected in context.actual
