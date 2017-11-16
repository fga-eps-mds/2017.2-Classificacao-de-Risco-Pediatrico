from behave import given, when, then


@when('we visit google')
def step(context):
    context.browser.get('http://www.google.com')


@then('it should have a title "Google"')
def step(context):
    assert context.browser.title == "Google"
