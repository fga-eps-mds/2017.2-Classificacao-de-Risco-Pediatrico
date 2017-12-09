from behave import step
from selenium.webdriver.support.ui import Select

@step('I click on Estatísticas')
def click_estatisticas(context):
    context.browser.find_element_by_id('stats').click()

@step('I click on Gráfico de Classificações')
def click_grafico_classificacoes(context):
    context.browser.find_element_by_id('classif_chart').click()
