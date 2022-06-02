import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class setFilter:
    driver = None
    count_on_page = 10
    config = None

    def __init__(self, driver, config, count_on_page=50):
        self.driver = driver
        self.config = config
        self.count_on_page = count_on_page

    def clearFilter(self):
        try:
            self.driver.find_element_by_id('ctl00_cph_TopStr_FilterClearTop').click()
        except:
            pass

    def setFilter(self):
        self.driver.find_element_by_id('ctl00_cph_TopStr_FilterTop').click()
        time.sleep(self.config['time_fast'])

        txtMesGodNum = self.config['mounth'] + self.config['year']

        #modal = self.driver.find_element_by_id('ctl00_cph_Filter')

        # Устанавливаем дату С (Месяц/год)
        txtMesGodFrom = self.driver.find_element_by_id('igtxtctl00_cph_Filter_ctl05_txtMesGodFrom')
        txtMesGodFrom.clear()
        txtMesGodFrom.click()
        txtMesGodFrom.send_keys(Keys.HOME, txtMesGodNum)

        # Устанавливаем дату ПО (Месяц/год)
        time.sleep(self.config['time_fast'])
        txtMesGodTo = self.driver.find_element_by_id('igtxtctl00_cph_Filter_ctl05_txtMesGodTo')
        txtMesGodTo.clear()
        txtMesGodTo.click()
        txtMesGodTo.send_keys(Keys.HOME, txtMesGodNum)

        # Кликаем по установке фильтра
        time.sleep(self.config['time_fast'])
        self.driver.find_element_by_id('ctl00_cph_Filter_ctl06_btnOk').click()



    def setCount(self):
        count = self.count_on_page
        list_item = self.driver.find_element_by_xpath("//select[@id='ctl00_cph_TopStr_pgrTopStr_Pager__pageSize']/option[text()='" + str(count) + "']")
        list_item.click()

    def go(self):
        self.clearFilter()
        time.sleep(self.config['time_fast'])
        self.setCount()
        time.sleep(self.config['time_fast'])
        self.setFilter()