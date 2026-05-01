from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"

    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.XPATH, '//h3[@data-test="error"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.get(self.URL)

    def _get_visible_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    def _click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def enter_username(self, username):
        field = self._get_visible_element(self.username_input) 
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self._get_visible_element(self.password_input)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self._click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        error = self._get_visible_element(self.error_message)
        return error.text
           
    def is_error_displayed(self):
        return self._get_visible_element(self.error_message).is_displayed()
    
    def is_on_inventory_page(self):
        return "inventory" in self.driver.current_url.lower()
    
    
    
    






























































































































































































































































































































































































