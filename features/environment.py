import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crp.settings')
import django
django.setup()
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from apps.users.models import Staff


def before_all(context):
    context.browser = webdriver.Remote(
        desired_capabilities=DesiredCapabilities.CHROME,
        command_executor='http://selenium-hub:4444/wd/hub'
    )


def after_all(context):
    Staff.objects.filter(name="selenium-user").delete()
    context.browser.quit()
