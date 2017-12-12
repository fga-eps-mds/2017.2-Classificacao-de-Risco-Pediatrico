from behave import step
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time



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

@step(u'I insert symptoms and classify {id_patient}')
def classify(context, id_patient):

     time.sleep(1)
     #context.browser.save_screenshot('screenie1.png')
     symptom = context.browser.find_element_by_css_selector(f'#risk_ranting{id_patient} input[name="febre"]')
     context.browser.execute_script("arguments[0].click();", symptom)
     classify_button = context.browser.find_element_by_id(f'submit{id_patient}')
     context.browser.execute_script("arguments[0].click();", classify_button)


@step(u'I click on save for {id_patient}')
def click_on_save(context, id_patient):
    time.sleep(2)
    #context.browser.save_screenshot('screenie2.png')
    save_button = context.browser.find_element_by_id(f'classification_save{id_patient}')
    context.browser.execute_script("arguments[0].click();", save_button)


@then(u'should update de classification of {id_patient}')
def check_classification(context, id_patient):

    odd_rows = context.browser.find_elements_by_css_selector("tr.odd")
    even_rows = context.browser.find_elements_by_css_selector("tr.even")
    rows = odd_rows + even_rows
    cells = []
    patient_classification = ''

    for row in rows:
        cells.append(row.find_elements_by_tag_name("td")[2].text)
        # leaving this here in case you want to check all classifications
        if row.find_elements_by_tag_name("td")[1].text == id_patient:
            patient_classification = row.find_elements_by_tag_name("td")[2].text

    print (cells)
    print(patient_classification)
    assert patient_classification != 'Não classificado'
