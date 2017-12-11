from behave import step
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



# @step('I realize a classification: {id_number_patient}')
# def classification(context, id_number_patient):
#
#     # print(context.browser.current_url)
#     context.browser.find_element_by_id('id_modal-{id_number_patient}').click()
#
#     wait = WebDriverWait(context.browser, 10)
#     element = wait.until(EC.element_to_be_clickable((By.NAME, "dispineia")))
#
#
#     context.browser.find_element_by_name("dispineia").click()
#     context.browser.find_element_by_name("prostracao").click()
#
#     element = wait.until(EC.element_to_be_clickable((By.ID, "modal_id")))
#     context.browser.find_element_by_id('modal_id').click()#open second modal
#
#     element = wait.until(EC.element_to_be_clickable((By.ID, "classification_save")))
#     context.browser.find_element_by_id('classification_save').click()#confirm classification
#
#
#
# @step('The classification must be updated')
# def verification(context):
#     print (context.browser.current_url)
#     title = context.browser.title
#     assert 'CRP' in title

@when(u'I click in patient: {id_patient}')
def acess_patient(context, id_patient):
    context.browser.find_element_by_id(f'id_modal-{id_patient}').click()
    # context.browser.find_element_by_css_selector(f'#risk_ranting{id_patient} input[name="dispineia"]').click()
    #wait 1
    # wait = WebDriverWait(context.browser, 10)
    # element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'#risk_ranting{id_patient} input[name="dispineia"]')))

    # wait 2
    context.browser.implicitly_wait(3)
    context.browser.find_element_by_css_selector(f'#risk_ranting{id_patient} input[name="dispineia"]').click()

    # try:
    #     element = WebDriverWait(context.browser, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, f'#risk_ranting{id_patient} input[name="dispineia"]'))
    # )
    # finally:
    #     print("Não funfou :'( ")
        # driver.quit()

@when(u'In modal a chose the symptons')
def step_impl(context):
     print(context.browser.current_url)

#
# @then(u'Should update de classifications')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Should update de classifications')
