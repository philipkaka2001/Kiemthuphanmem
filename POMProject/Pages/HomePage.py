from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class HomePage(BasePage):
    HEADER = (By.CSS_SELECTOR, "h1.dashboard-selector__title")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "account-name ")
    SETTING_ICON = (By.ID, "navSetting")

    def __init__(self, driver):
        super().__init__(driver)
    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_settings_icon_exits(self):
        return self.is_vistble(self.SETTING_ICON)

    def get_header_value(self):
        if self.is_vistble(self.HEADER):
            return self.get_element_text(self.HEADER)
    def get_account_name_value(self):
        if self.is_vistble(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)







