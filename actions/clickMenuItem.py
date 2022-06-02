import time

class clickMenuItem:
    text = None
    driver = None
    sec = 0

    def __init__(self, driver, text, sec=2):
        self.text = text
        self.driver = driver
        self.sec = sec

    def search_item(self):
        search_box = self.driver.find_element_by_id('ctl00_cph_ctrlFastFind_pnl')
        input = search_box.find_element_by_tag_name('input')
        input.clear()
        input.send_keys(self.text)
        button = search_box.find_element_by_tag_name('a')
        button.click()

    def go(self):
        self.search_item()
        time.sleep(self.sec)
        item = self.driver.find_element_by_id('ctl00cphuwT_1')
        item.click()
