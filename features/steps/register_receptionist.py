from behave import when
from selenium.webdriver.support.ui import Select


@when('we acess the register page')
def get_login_page(context):
    context.browser.get('http://web:8000/register/user/')


@step('select the profile {profile}')
def select_profile(context, profile):
    if (profile.replace('"', '') == "receptionist"):
        Select(context.browser.find_element_by_id(
           'dropdown-profile')).select_by_value('1')

    elif (profile.replace('"', '') == "attendant"):
        Select(context.browser.find_element_by_id(
           'dropdown-profile')).select_by_value('2')


@step('fiel the information fields')
def fill_fields(context):

    context.browser.find_element_by_name(
       "name").send_keys("selenium-user")

    context.browser.find_element_by_name(
       "email").send_keys("selenium-user@gmail.com")

    context.browser.find_element_by_name(
       "password1").send_keys("selenium-user123")

    context.browser.find_element_by_name(
       "password2").send_keys("selenium-user123")

    context.browser.find_element_by_name(
      "id_user").send_keys("666")

    #dropdown state
    Select(context.browser.find_element_by_id(
      'dropdown-state')).select_by_value('DF')

    context.browser.find_element_by_name("city").send_keys("gama")
    context.browser.find_element_by_name("street").send_keys("alagados")
    context.browser.find_element_by_name("neighborhood").send_keys("UnB")
    context.browser.find_element_by_name("block").send_keys("----")
    context.browser.find_element_by_name("number").send_keys("10")


@when('i click the cadastrar button')
def click_button(context):
    context.browser.find_element_by_id('button-cadastrar').click()


@then('it should redirect me to the {url} page')
def is_redirected(context, url):
    print(context.browser.current_url)
    print("http://web:8000/" + url)
    assert context.browser.current_url == "http://web:8000/" + url.replace(
       '"', '')
