import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import utils

EMAIL_FOR_LOGIN = "re765fvdfbd2ba@yandex.ru"
PASSWORD_FOR_LOGIN = "123456"


@pytest.mark.parametrize('url, button_for_click', [
    (locators.Url.menu_url, locators.Button.button_login_on_account),
    (locators.Url.menu_url, locators.Button.button_personal_account),
    (locators.Url.register_url, locators.Links.login_link),
    (locators.Url.login_url, locators.Links.restore_password)],
                         ids=['from_login_on_account', 'from_personal_account',
                              'from_registration', 'from_restore_password'])
def test_login(driver, url, button_for_click):
    driver.get(url)

    driver.find_element(By.XPATH, button_for_click).click()
    if button_for_click == locators.Links.restore_password:
        driver.find_element(By.XPATH, locators.Links.login_link).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.TAG_NAME, 'h2')))

    # login
    utils.login_to_account(driver)
