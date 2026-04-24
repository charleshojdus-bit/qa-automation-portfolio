from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    cart_item_names = (By.CLASS_NAME, "inventory_item_name")
    remove_button = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver

    def is_item_in_cart(self, item_name):
        items = self.driver.find_elements(*self.cart_item_names)

        for item in items:
            if item.text == item_name:
                return True

        return False
    
    def remove_item(self):
        remove_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.remove_button)
    )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", remove_btn)
        self.driver.execute_script("arguments[0].click();", remove_btn)

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*self.cart_item_names)) == 0
    )
        
            
        
    def is_cart_empty(self):
        items = self.driver.find_elements(*self.cart_item_names)
        return len(items) == 0
        