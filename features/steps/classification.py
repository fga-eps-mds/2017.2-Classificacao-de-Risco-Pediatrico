from behave import step
from selenium.webdriver.support.ui import Select


@step(u'I register an employee: {name_user},'
' {id_number_user} and {profile_number_user}')
def register_user(context, name_user, id_number_user, profile_number_user):
    context.browser.find_element_by_name(
        "name").send_keys(name_user)

    Select(context.browser.find_element_by_id(
        'dropdown-profile')).select_by_value(profile_number_user)

    context.browser.find_element_by_name(
        "email").send_keys(f"{name_user}-{id_number_user}@gmail.com")

    context.browser.find_element_by_name(
        "password1").send_keys("selenium-user1234")

    context.browser.find_element_by_name(
        "password2").send_keys("selenium-user1234")

    context.browser.find_element_by_name(
        "id_user").send_keys(id_number_user)

    # dropdown state
    Select(context.browser.find_element_by_id(
        'dropdown-state')).select_by_value('DF')

    context.browser.find_element_by_name("city").send_keys("gama")
    context.browser.find_element_by_name("street").send_keys("alagados")
    context.browser.find_element_by_name("neighborhood").send_keys("UnB")
    context.browser.find_element_by_name("block").send_keys("----")
    context.browser.find_element_by_name("number").send_keys("10")
    context.browser.find_element_by_id('button-cadastrar').click()


@step('I register a patient: {name_patient}, {id_number_patient} and {profile_number_patient}')
def register_patient(context, name_patient, id_number_patient, profile_number_patient):
    print("teste")
    print(browser.current_url)
    context.browser.find_element_by_id('register-patient').click()
    Select(context.browser.find_element_by_id(
        'id_age_range')).select_by_value('0')
    context.browser.find_element_by_id('register-patient-button').click()


@step('I realize a classification: {id_number}')
def classification(context):
    context.browser.find_element_by_id('name_patient').click()
    context.browser.find_element_by_name('dispineia').click()
    context.browser.find_element_by_name('prostracao').click()

    context.browser.find_element_by_id('modal_id').click()

    context.browser.find_element_by_id('classification_save').click()


@step('The classification must be updated')
def verification(context):
    title = context.browser.title
    assert 'Welcome' in title
