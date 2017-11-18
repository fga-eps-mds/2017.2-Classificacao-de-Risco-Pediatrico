from behave import when, then


@when('we visit google')
def visit(context):
    context.browser.get('http://www.google.com')


@then('it should have a title "Google"')
def check_title(context):
    assert context.browser.title == "Google"
