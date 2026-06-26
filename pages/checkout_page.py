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
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script("arguments[0].click();", element)

        return element

    def _type(self, locator, text):
        element = self._get_visible_element(locator)

        self.driver.execute_script(
            """
            const element = arguments[0];
            const value = arguments[1];

            const prototype = Object.getPrototypeOf(element);
            const valueSetter = Object.getOwnPropertyDescriptor(prototype, 'value').set;

            valueSetter.call(element, value);

            element.dispatchEvent(new Event('input', { bubbles: true }));
            element.dispatchEvent(new Event('change', { bubbles: true }));
            """,
            element,
            text,
        )

        return element

    def enter_first_name(self, first_name):
        self._type(self.first_name_input, first_name)

    def enter_last_name(self, last_name):
        self._type(self.last_name_input, last_name)

    def enter_postal_code(self, postal_code):
        self._type(self.postal_code_input, postal_code)

    def click_continue(self):
        self._click(self.continue_button)

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-two")
        )

    def click_finish(self):
        self._click(self.finish_button)

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-complete")
        )

    def get_confirmation_message(self):
        return self._get_visible_element(self.confirmation_message).text
