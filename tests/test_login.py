import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import utils

EMAIL_FOR_LOGIN = "re765fvdfbd2ba@yandex.ru"
PASSWORD_FOR_LOGIN = "123456"


@pytest.mark.parametrize('url, button_for_click', [
    ('', locators.Button.BUTTON_LOGIN_ON_ACCOUNT),
    ('', locators.Button.BUTTON_PERSONAL_ACCOUNT),
    (locators.Url.REGISTER_URL, locators.Links.LOGIN_LINK),
    (locators.Url.LOGIN_URL, locators.Links.RESTORE_PASSWORD)],
                         ids=['from_login_on_account', 'from_personal_account',
                              'from_registration', 'from_restore_password'])
def test_login(driver, url, button_for_click):
    driver.get(locators.Url.BASE_URL + url)

    driver.find_element(By.XPATH, button_for_click).click()
    if button_for_click == locators.Links.RESTORE_PASSWORD:
        driver.find_element(By.XPATH, locators.Links.LOGIN_LINK).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.TAG_NAME, 'h2')))

    # login
    utils.login_to_account(driver)
    assert driver.find_element(By.XPATH,
                               locators.Button.BUTTON_CREATE_ORDER).is_displayed()
