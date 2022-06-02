import time
from libs.GetDriver import GetDriver

class doLogin():
    config = None
    base = None
    driver = None

    def __init__(self, driver, meta, base):
        self.config = meta['config']
        self.base = base
        self.driver = driver

    def go(self):
        self.driver.get(self.config['url'])
        time.sleep(self.config['time_fast'])

        loginForm = self.driver.find_element_by_class_name('login_form')
        # print(loginForm.get_attribute('outerHTML'))

        login_inputs = loginForm.find_elements_by_class_name('login_input')
        for login_input in login_inputs:
            if login_input.get_attribute("id") == 'tbUserName':
                # Находим поле Логина
                IdLogin = login_input

                # Очищаем введённое значение
                IdLogin.clear()
                # Вводим значение в поле поиска
                IdLogin.send_keys(self.base['login'])

            elif login_input.get_attribute("id") == 'tbPassword':
                # Находим поле Пароля
                IdPass = login_input
                # Очищаем введённое значение
                IdPass.clear()
                # Вводим значение в поле поиска
                IdPass.send_keys(self.base['pass'])

        # Выбираем базу
        popupBases = loginForm.find_element_by_class_name('dropbtn')
        popupBases.click()
        time.sleep(2)

        myDropdown = self.driver.find_element_by_id('myDropdown')

        listBases = myDropdown.find_elements_by_class_name('listBaseRow')

        for itemBase in listBases:
            baseTds = itemBase.find_elements_by_tag_name('td')
            baseName = baseTds[3].text.strip()
            if (baseName == self.base['base']):
                baseTds[0].click()
                break

        time.sleep(2)

        # Находим кнопку Вход
        lbtnLogin = self.driver.find_element_by_id('lbtnLogin')
        # Нажимаем кнопку Enter и переходим на главную страницу *****************************
        lbtnLogin.click()