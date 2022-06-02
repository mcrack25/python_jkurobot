import time
from selenium.webdriver import ActionChains

class downloadFile():
    driver = None
    config = None

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    # Находим кнопку печать
    def go(self):
        time.sleep(self.config['time_fast'])
        top_menu = self.driver.find_element_by_id('ctl00_cph_mnu')
        top_menu_lis = top_menu.find_elements_by_tag_name('li')
        for top_menu_li in top_menu_lis:
            if 'Печать' in top_menu_li.text:
                ActionChains(self.driver).move_to_element(top_menu_li).perform()
                time.sleep(self.config['time_fast'])
                sub_top_menu_lis = top_menu_li.find_elements_by_tag_name('li')
                for sub_top_menu_li in sub_top_menu_lis:
                    if 'Список сводной ведомости по выплате' in sub_top_menu_li.text:
                        ActionChains(self.driver).move_to_element(sub_top_menu_li).perform()
                        time.sleep(self.config['time_fast'])
                        subsub_top_menu_lis = sub_top_menu_li.find_elements_by_tag_name('li')
                        for subsub_top_menu_li in subsub_top_menu_lis:
                            if 'с итогами по видам ГСП' in subsub_top_menu_li.text:
                                ActionChains(self.driver).move_to_element(subsub_top_menu_li).perform()
                                subsub_top_menu_li.click()
                                return True
        return False