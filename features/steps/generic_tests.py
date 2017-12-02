from behave import when, then, step


@when('I access {page}')
def get_page(context, page):
    context.browser.get(f'http://web:8000/{page}')


@step('I log into server with data: {email} and {password}')
def login_into_server(context, email, password):
    context.browser.find_element_by_name(
        "username").send_keys(email)
    context.browser.find_element_by_name(
        "password").send_keys(password)
    context.browser.find_element_by_id('login-button').click()


@then('it should redirect me to the {url} page')
def redirect_page(context, url):
    assert context.browser.current_url == "http://web:8000/" + url
