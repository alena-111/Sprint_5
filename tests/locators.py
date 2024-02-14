class Button:
    BUTTON_REGISTRATION = '//button[text()="Зарегистрироваться"]'
    BUTTON_LOGIN = '//button[text()="Войти"]'
    BUTTON_CREATE_ORDER = '//button[text()="Оформить заказ"]'
    BUTTON_LOGIN_ON_ACCOUNT = '//button[text()="Войти в аккаунт"]'
    BUTTON_PERSONAL_ACCOUNT = '//p[text()="Личный Кабинет"]'
    BUTTON_LOGOUT = '//button[text()="Выход"]'


class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    LOGIN_URL = '/login'
    REGISTER_URL = '/register'


class Links:
    LOGIN_LINK = '//a[text()="Войти"]'
    RESTORE_PASSWORD = '//a[text()="Восстановить пароль"]'
    BUTTON_PROFILE = '//a[text()="Профиль"]'
    CONSTRUCTOR_LINK = '//p[text()="Конструктор"]'


class Inputs:
    NAME_INPUT_VALUE = 'Name'
    INPUT_NAME = 'name'
    INPUT_PASSWORD = 'Пароль'
    INPUT_EMAIL = "//*[text()='Email']/following-sibling::input"
    PASSWORD_INPUT_ERROR = '//p[text()="Некорректный пароль"]'


class MenuButtons:
    SAUCES = '//span[text()="Соусы"]'
    FILLINGS = '//span[text()="Начинки"]'
    SAUCE_WITH_SPIKES = '//img[@alt="Соус с шипами Антарианского плоскоходца"]'
    BLUE_CHEESE = '//img[@alt ="Сыр с астероидной плесенью"]'
    BUNS_200I = '//img[contains(@alt,"Краторная булка N-200i")]'
    BUNS = '//span[text()="Булки"]'
    ACTIVE_BUNS = '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]//span[text()="Булки"]'
    ACTIVE_FILLINGS = '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]//span[text()="Начинки"]'
    ACTIVE_SAUCES = '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]//span[text()="Соусы"]'
