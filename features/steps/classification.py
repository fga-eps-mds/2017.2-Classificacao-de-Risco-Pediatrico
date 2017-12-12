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

@step(u'I click in patient: {id_patient}')
def acess_patient(context, id_patient):
    context.browser.find_element_by_id(f'id_modal-{id_patient}').click()
    # context.browser.find_element_by_css_selector(f'#risk_ranting{id_patient} input[name="dispineia"]').click()
    #wait 1
    # wait = WebDriverWait(context.browser, 10)
    # element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'#risk_ranting{id_patient} input[name="dispineia"]')))

    # wait 2

    # try:
    #     element = WebDriverWait(context.browser, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, f'#risk_ranting{id_patient} input[name="dispineia"]'))
    # )
    # finally:
    #     print("Não funfou :'( ")
        # driver.quit()

@step(u'I click on Classificar')
def classify(context):
     # context.browser.implicitly_wait(12)
     # element = WebDriverWait(context.browser, 10).until(
     #     EC.presence_of_element_located((By.CSS_SELECTOR, f'#risk_ranting1 input[name="febre"]')))

     classify_button = context.browser.find_element_by_id('modal_id')
     context.browser.execute_script("arguments[0].click();", classify_button)

     # symptom.click()
     # context.browser.find_element_by_link_text('Classificar').click()
     #context.browser.find_element_by_css_selector(f'#risk_ranting{id_patient} input[name="febre"]').click()


@step(u'I click on save')
def click_on_save(context):
     save_button = context.browser.find_element_by_id('modal_id')
     context.browser.execute_script("arguments[0].click();", save_button)


@then(u'should update de classification')
def check_classification(context):
    odd_rows = context.browser.find_elements_by_css_selector("tr.odd")
    even_rows = context.browser.find_elements_by_css_selector("tr.even")
    rows = odd_rows + even_rows
    cells = []
    for row in rows:
        cells.append(row.find_elements_by_tag_name("td")[2].text)
        # leaving this here in case you want to check all classifications
        print (row.find_elements_by_tag_name("td")[2].text)

    # The line below asserts that at least one patient is not "Não Classificado"
    assert 'Atendimento Imediato' or \
           'Atendimento Hospitalar' or \
           'Atendimento Ambulatorial' in cells
