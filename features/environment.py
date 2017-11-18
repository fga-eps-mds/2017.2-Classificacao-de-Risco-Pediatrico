from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_all(context):
    context.browser = webdriver.Remote(
        desired_capabilities=DesiredCapabilities.CHROME,
        command_executor='http://selenium-hub:4444/wd/hub'
    )


def after_all(context):
    context.browser.quit()
