from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import utils


def test_personal_account(driver):
    driver.get(locators.Url.login_url)
    # login
    utils.login_to_account(driver)

    driver.find_element(By.XPATH,
                        locators.Button.button_personal_account).click()
    driver.find_element(By.XPATH, locators.Button.button_logout).is_displayed()
    driver.find_element(By.XPATH, locators.Button.button_logout).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.TAG_NAME, 'h2')))
    assert driver.find_element(By.XPATH,
                               locators.Button.button_login).is_displayed()
