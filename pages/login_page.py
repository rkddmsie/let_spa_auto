from pages.base_page import BasePage
from locators.login_locator import LoginLocator

class LoginPage(BasePage):

    def login(self, username, password):
        self.fill(LoginLocator.USERNAME, username)
        self.fill(LoginLocator.PASSWORD, password)
        self.click(LoginLocator.LOGIN_BTN)