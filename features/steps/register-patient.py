from behave import step
from selenium.webdriver.support.ui import Select


@step('I click in register patient')
def click_register_patient(context):
    context.browser.find_element_by_id('register-patient').click()


@step('I fill patient form')
def fill_patient_form(context):
    Select(context.browser.find_element_by_id(
        'id_age_range')).select_by_value('1')
    context.browser.find_element_by_id('register-patient-button').click()
