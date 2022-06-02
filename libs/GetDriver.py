import os
from selenium import webdriver

class GetDriver:
    driver = None
    download_dir = None

    def __init__(self, ROOT_DIR, config):
        self.download_dir = os.path.join(ROOT_DIR, 'downloads')

        driver = None
        drivers_path = os.path.join(ROOT_DIR, 'drivers')

        if config['browser'] == 'firefox':
            driver_firefox = os.path.join(drivers_path, config['driver'])

            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.dir", self.download_dir)
            profile.set_preference("browser.download.useDownloadDir", True)
            profile.set_preference("browser.download.viewableInternally.enabledTypes", "")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            driver = webdriver.Firefox(firefox_profile=profile, executable_path=driver_firefox)

        elif config['browser'] == 'chrome':
            options = webdriver.ChromeOptions()
            prefs = {"download.default_directory": self.download_dir}
            options.add_experimental_option("prefs", prefs)
            driver_chrome = os.path.join(drivers_path, config['driver'])
            driver = webdriver.Chrome(chrome_options=options, executable_path=driver_chrome)
        self.driver = driver

    def get(self):
        return self.driver