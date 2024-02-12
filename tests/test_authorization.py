from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import utils


def test_successful_registration(driver):
    driver.get(locators.Url.register_url)
    driver.find_element(By.NAME, locators.Inputs.input_name).send_keys("Иван")
    driver.find_element(By.XPATH, locators.Inputs.input_login).send_keys(
        utils.random_email())
    driver.find_element(By.NAME, locators.Inputs.input_password).send_keys(
        "123456")
    driver.find_element(By.XPATH, locators.Button.button_registration).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.TAG_NAME, 'h2')))
    assert driver.find_element(By.XPATH,
                               locators.Button.button_login).is_displayed()


def test_fail_registration_with_incorrect_password(driver):
    driver.get(locators.Url.register_url)
    driver.find_element(By.NAME, locators.Inputs.input_name).send_keys("Иван")
    driver.find_element(By.XPATH, locators.Inputs.input_login).send_keys(
        "re765fvdfbd2ba@yandex.ru")
    driver.find_element(By.NAME, locators.Inputs.input_password).send_keys("12")
    driver.find_element(By.XPATH, locators.Button.button_registration).click()
    assert driver.find_element(By.XPATH,
                               locators.Inputs.password_input_error).is_displayed()
