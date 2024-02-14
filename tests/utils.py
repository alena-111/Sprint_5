import random
import string

from selenium.webdriver.common.by import By

import locators


def random_email():
    email_end = '@yandex.ru'
    email_start = ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=10))
    return email_start + email_end


def login_to_account(driver):
    EMAIL_FOR_LOGIN = "re765fvdfbd2ba@yandex.ru"
    PASSWORD_FOR_LOGIN = "123456"

    driver.find_element(By.XPATH, locators.Inputs.INPUT_EMAIL).send_keys(
        EMAIL_FOR_LOGIN)
    driver.find_element(By.NAME, locators.Inputs.INPUT_PASSWORD).send_keys(
        PASSWORD_FOR_LOGIN)
    driver.find_element(By.XPATH, locators.Button.BUTTON_LOGIN).click()
    assert driver.find_element(By.XPATH,
                               locators.Button.BUTTON_CREATE_ORDER).is_displayed()
