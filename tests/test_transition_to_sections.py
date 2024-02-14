import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import utils

EMAIL_FOR_LOGIN = "re765fvdfbd2ba@yandex.ru"
PASSWORD_FOR_LOGIN = "123456"


def test_transition_to_sections_sauces(driver):
    driver.get(locators.Url.BASE_URL + locators.Url.LOGIN_URL)
    # login
    utils.login_to_account(driver)

    # Соусы
    driver.find_element(By.XPATH, locators.MenuButtons.SAUCES).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH,
                                                           locators.MenuButtons.SAUCE_WITH_SPIKES)))
    assert driver.find_element(By.XPATH,
                               locators.MenuButtons.SAUCE_WITH_SPIKES).is_displayed()
    assert driver.find_element(By.XPATH,
                               locators.MenuButtons.ACTIVE_SAUCES).is_displayed()


def test_transition_to_sections_filling(driver):
    driver.get(locators.Url.BASE_URL + locators.Url.LOGIN_URL)
    # login
    utils.login_to_account(driver)

    # Начинки
    element_blue_cheese = driver.find_element(By.XPATH,
                                              locators.MenuButtons.BLUE_CHEESE)
    driver.execute_script("arguments[0].scrollIntoView();",
                          element_blue_cheese)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH,
                                                           locators.MenuButtons.BLUE_CHEESE)))
    assert driver.find_element(By.XPATH,
                               locators.MenuButtons.BLUE_CHEESE).is_displayed()
    assert driver.find_element(By.XPATH,
                               locators.MenuButtons.ACTIVE_FILLINGS).is_displayed()


def test_transition_to_sections_buns(driver):
    driver.get(locators.Url.BASE_URL + locators.Url.LOGIN_URL)
    # login
    utils.login_to_account(driver)

    # Булки
    time.sleep(1)
    driver.find_element(By.XPATH, locators.MenuButtons.SAUCES).click()
    driver.find_element(By.XPATH, locators.MenuButtons.BUNS).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH,
                                                           locators.MenuButtons.BUNS_200I)))
    assert driver.find_element(By.XPATH,
                               locators.MenuButtons.BUNS_200I).is_displayed()

    assert driver.find_element(By.XPATH,
                               locators.MenuButtons.ACTIVE_BUNS).is_displayed()
