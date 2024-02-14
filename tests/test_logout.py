from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import utils


def test_personal_account(driver):
    driver.get(locators.Url.BASE_URL + locators.Url.LOGIN_URL)
    # login
    utils.login_to_account(driver)

    driver.find_element(By.XPATH,
                        locators.Button.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(By.XPATH, locators.Button.BUTTON_LOGOUT).is_displayed()
    driver.find_element(By.XPATH, locators.Button.BUTTON_LOGOUT).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.TAG_NAME, 'h2')))
    assert driver.find_element(By.XPATH,
                               locators.Button.BUTTON_LOGIN).is_displayed()
