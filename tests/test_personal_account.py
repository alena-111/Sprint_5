from selenium.webdriver.common.by import By

import locators
import utils


def test_personal_account(driver):
    driver.get(locators.Url.login_url)
    # login
    utils.login_to_account(driver)

    driver.find_element(By.XPATH,
                        locators.Button.button_personal_account).click()
    assert driver.find_element(By.XPATH,
                               locators.Links.button_profile).is_displayed()
