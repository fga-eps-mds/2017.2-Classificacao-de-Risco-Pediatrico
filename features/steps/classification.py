from behave import step
import time


@step(u'I click in patient: {id_patient}')
def acess_patient(context, id_patient):
    context.browser.find_element_by_id(f'id_modal-{id_patient}').click()


@step(u'I insert symptoms and classify {id_patient}')
def classify(context, id_patient):
    time.sleep(1)
    # context.browser.save_screenshot('screenie1.png')
    symptom = context.browser.find_element_by_css_selector(
        f'#risk_ranting{id_patient} input[name="febre"]')
    context.browser.execute_script("arguments[0].click();", symptom)
    symptom_2 = context.browser.find_element_by_css_selector(
        f'#risk_ranting{id_patient} input[name="dispineia"]')
    context.browser.execute_script("arguments[0].click();", symptom_2)
    classify_button = context.browser.find_element_by_id(f'submit{id_patient}')
    context.browser.execute_script("arguments[0].click();", classify_button)


@step(u'I click on save for {id_patient}')
def click_on_save(context, id_patient):
    time.sleep(2)
    # context.browser.save_screenshot('screenie2.png')
    save_button = context.browser.find_element_by_id(
        f'classification_save{id_patient}')
    context.browser.execute_script("arguments[0].click();", save_button)


@step(u'should update de classification of {id_patient}')
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
            patient_classification = row.find_elements_by_tag_name(
                "td")[2].text

    print(cells)
    print(patient_classification)
    assert patient_classification != 'Não classificado'
