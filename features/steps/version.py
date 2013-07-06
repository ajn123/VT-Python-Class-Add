from behave import given, when, then
from Navigator import Navigator

nav = Navigator()


@given('I have Python {version} installed')
def impl(context, version):
    version = version.split(".")
    version = tuple(version)
    context.version = version  # Pack the Tuple Arguments


@when('I try to check my version')
def impl(context):
    context.actual = str(nav.checkVersion(*context.version))  # Unpack the Tuple Arguments


@then('I should see "{expected}" in my message')
def impl(context, expected):
    if (expected == "Nothing"):
        assert "" in context.actual
    else:
        assert expected in context.actual
