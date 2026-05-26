from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    confirmation_message = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def _get_visible_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
    
    def _click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_first_name(self, first_name):
        self._get_visible_element(self.first_name_input).send_keys(first_name)
       
    def enter_last_name(self, last_name):
        self._get_visible_element(self.last_name_input).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self._get_visible_element(self.postal_code_input).send_keys(postal_code)

    def click_continue(self):
        self._click(self.continue_button)

    def click_finsish(self):
        self._click(self.finish_button)

    def get_confirmation_message(self):
        return self._get_visible_element(self.confirmation_message).text

    

