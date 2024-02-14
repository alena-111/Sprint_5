from selenium.webdriver.common.by import By

import locators
import utils


def test_personal_account_constructor(driver):
    driver.get(locators.Url.BASE_URL + locators.Url.LOGIN_URL)
    # login
    utils.login_to_account(driver)
    driver.find_element(By.XPATH,
                        locators.Button.BUTTON_CREATE_ORDER).is_displayed()

    driver.find_element(By.XPATH,
                        locators.Button.BUTTON_PERSONAL_ACCOUNT).click()

    driver.find_element(By.XPATH, locators.Links.CONSTRUCTOR_LINK).click()

    assert driver.find_element(By.XPATH,
                               locators.Button.BUTTON_CREATE_ORDER).is_displayed()


def test_personal_account_burger(driver):
    driver.get(locators.Url.BASE_URL + locators.Url.LOGIN_URL)
    # login
    utils.login_to_account(driver)
    driver.find_element(By.XPATH,
                        locators.Button.BUTTON_CREATE_ORDER).is_displayed()

    driver.find_element(By.XPATH,
                        locators.Button.BUTTON_PERSONAL_ACCOUNT).click()

    for element in driver.find_elements(By.TAG_NAME, 'svg'):
        if element.get_attribute(
                'xmlns') == 'http://www.w3.org/2000/svg':
            element.click()
            break

    assert driver.find_element(By.XPATH,
                               locators.Button.BUTTON_CREATE_ORDER).is_displayed()
