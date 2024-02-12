import pytest
from selenium.webdriver.common.by import By

import locators
import utils


@pytest.mark.parametrize('links', [locators.Links.constructor_link, 'svg'],
                         ids=['constructor', 'burger svg'])
def test_personal_account(driver, links):
    driver.get(locators.Url.login_url)
    # login
    utils.login_to_account(driver)
    driver.find_element(By.XPATH,
                        locators.Button.button_create_order).is_displayed()

    driver.find_element(By.XPATH,
                        locators.Button.button_personal_account).click()

    if links == 'svg':
        for element in driver.find_elements(By.TAG_NAME, links):
            if element.get_attribute('xmlns') == 'http://www.w3.org/2000/svg':
                element.click()
                break
    else:
        driver.find_element(By.XPATH, links).click()

    assert driver.find_element(By.XPATH,
                               locators.Button.button_create_order).is_displayed()
