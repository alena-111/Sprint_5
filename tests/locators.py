class Button:
    button_registration = '//button[text()="Зарегистрироваться"]'
    button_login = '//button[text()="Войти"]'
    button_create_order = '//button[text()="Оформить заказ"]'
    button_login_on_account = '//button[text()="Войти в аккаунт"]'
    button_personal_account = '//p[text()="Личный Кабинет"]'
    button_logout = '//button[text()="Выход"]'


class Url:
    login_url = 'https://stellarburgers.nomoreparties.site/login'
    menu_url = 'https://stellarburgers.nomoreparties.site/'
    register_url = 'https://stellarburgers.nomoreparties.site/register'


class Links:
    login_link = '//a[text()="Войти"]'
    restore_password = '//a[text()="Восстановить пароль"]'
    button_profile = '//a[text()="Профиль"]'
    constructor_link = '//p[text()="Конструктор"]'


class Inputs:
    name_input_value = 'Name'
    input_name = 'name'
    input_login = '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]'
    input_password = 'Пароль'
    input_email = '/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]'
    password_input_error = '//p[text()="Некорректный пароль"]'


class MenuButtons:
    sauces = '//span[text()="Соусы"]'
    fillings = '//span[text()="Начинки"]'
    sauce_with_spikes = '//img[@alt="Соус с шипами Антарианского плоскоходца"]'
    blue_cheese = '//img[@alt ="Сыр с астероидной плесенью"]'
    buns_200i = '//img[contains(@alt,"Краторная булка N-200i")]'
    buns = '//span[text()="Булки"]'
