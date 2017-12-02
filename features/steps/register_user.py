from behave import step
from selenium.webdriver.support.ui import Select


@step('fill information fields with data: {name} and {profile_number}')
def fill_fields(context, name, profile_number):
    context.browser.find_element_by_name(
        "name").send_keys(name)

    Select(context.browser.find_element_by_id(
        'dropdown-profile')).select_by_value(profile_number)

    context.browser.find_element_by_name(
        "email").send_keys(f"{name}-{profile_number}@gmail.com")

    context.browser.find_element_by_name(
        "password1").send_keys("selenium-user123")

    context.browser.find_element_by_name(
        "password2").send_keys("selenium-user123")

    context.browser.find_element_by_name(
        "id_user").send_keys(profile_number)

    # dropdown state
    Select(context.browser.find_element_by_id(
        'dropdown-state')).select_by_value('DF')

    context.browser.find_element_by_name("city").send_keys("gama")
    context.browser.find_element_by_name("street").send_keys("alagados")
    context.browser.find_element_by_name("neighborhood").send_keys("UnB")
    context.browser.find_element_by_name("block").send_keys("----")
    context.browser.find_element_by_name("number").send_keys("10")


@step('I click the submit button')
def click_button(context):
    context.browser.find_element_by_id('button-cadastrar').click()
