from selenium.webdriver.common.by import By

import locators
import utils


def test_personal_account(driver):
    driver.get(locators.Url.BASE_URL + locators.Url.LOGIN_URL)
    # login
    utils.login_to_account(driver)

    driver.find_element(By.XPATH,
                        locators.Button.BUTTON_PERSONAL_ACCOUNT).click()
    assert driver.find_element(By.XPATH,
                               locators.Links.BUTTON_PROFILE).is_displayed()
