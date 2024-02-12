from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import utils

EMAIL_FOR_LOGIN = "re765fvdfbd2ba@yandex.ru"
PASSWORD_FOR_LOGIN = "123456"


def test_transition_to_sections(driver):
    driver.get(locators.Url.login_url)
    # login
    utils.login_to_account(driver)

    # Соусы
    driver.find_element(By.XPATH, locators.MenuButtons.sauces).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH,
                                                           locators.MenuButtons.sauce_with_spikes)))
    assert driver.find_element(By.XPATH,
                               locators.MenuButtons.sauce_with_spikes).is_displayed()

    # Начинки
    element_blue_cheese = driver.find_element(By.XPATH,
                                              locators.MenuButtons.blue_cheese)
    driver.execute_script("arguments[0].scrollIntoView();",
                          element_blue_cheese)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH,
                                                           locators.MenuButtons.blue_cheese)))
    assert driver.find_element(By.XPATH,
                               locators.MenuButtons.blue_cheese).is_displayed()

    # Булки
    driver.find_element(By.XPATH, locators.MenuButtons.buns).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH,
                                                           locators.MenuButtons.buns_200i)))
    assert driver.find_element(By.XPATH,
                               locators.MenuButtons.buns_200i).is_displayed()
