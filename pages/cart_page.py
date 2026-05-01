from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    cart_item_names = (By.CLASS_NAME, "inventory_item_name")
    remove_button = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    def _get_visible_elements(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
        )
    
    def _click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        

    def is_item_in_cart(self, item_name):
        items = self.driver.find_elements(*self.cart_item_names)

        for item in items:
            if item.text == item_name:
                return True

        return False
    
    def remove_item(self):
        self._click(self.remove_button)

        self.wait.until(
            lambda d: len(d.find_elements(*self.remove_button)) == 0
        )
        
            
        
    def is_cart_empty(self):
        self.wait.until(
            lambda d: len(d.find_elements(*self.cart_item_names)) == 0
        )
        return True
