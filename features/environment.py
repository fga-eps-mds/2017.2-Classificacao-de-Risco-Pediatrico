import os

import django
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crp.settings')
django.setup()

from apps.users.models import Staff  # noqa


def before_all(context):
    context.browser = webdriver.Remote(
        desired_capabilities=DesiredCapabilities.CHROME,
        command_executor='http://selenium-hub:4444/wd/hub'
    )


def after_all(context):
    Staff.objects.filter(name="selenium-user-1").delete()
    Staff.objects.filter(name="selenium-user-2").delete()
    context.browser.quit()
