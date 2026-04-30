from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    

    inventory_container = (By.ID, "inventory_container")
    inventory_items = (By.CLASS_NAME, "inventory_item")
    backpack_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def _get_visible_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    def _get_visible_elements(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator)
    )
    
    def _click(self, locator):
     element = self.wait.until(
         EC.element_to_be_clickable(locator)
     )
     element.click()
    
    def is_on_inventory_page(self):
        return (
           "inventory" in self.driver.current_url 
        and self._get_visible_element(self.inventory_container).is_displayed()
        )
    
    def are_products_visible(self):
        items = self._get_visible_elements(self.inventory_items)
        return len(items) > 0
    
    def add_backpack_to_cart(self):
        self._click(self.backpack_add_to_cart_button)

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.cart_badge)

        if len(badges) == 0:
            return "0"
        
        return badges[0].text
    
    def click_cart_icon(self):
        self._click(self.cart_icon)

       

        

    