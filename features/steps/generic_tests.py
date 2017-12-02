from behave import when, then


@when('we access {page}')
def get_page(context, page):
    print(f'http://web:8000/{page}')
    context.browser.get(f'http://web:8000/{page}')


@then('it should redirect me to the {url} page')
def redirect_page(context, url):
    assert context.browser.current_url == "http://web:8000/" + url
