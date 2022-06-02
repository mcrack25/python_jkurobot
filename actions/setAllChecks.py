import time
from selenium.webdriver import ActionChains

class setAllChecks():
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def go(self):
        checkMain = self.driver.find_element_by_id('ctl00_cph_grd_ctl01_mnu')

        # Наводим на элемент чекбокса
        ActionChains(self.driver).move_to_element(checkMain).perform()
        time.sleep(self.config['time_fast'])
        checksPopup = checkMain.find_elements_by_css_selector('ul li')
        for checkMenuItem in checksPopup:
            li_text = checkMenuItem.get_attribute('title')
            if 'Выбрать все' in li_text:
                ActionChains(self.driver).move_to_element(checkMenuItem).perform()
                checkMenuItem.click()
                return True
        return False