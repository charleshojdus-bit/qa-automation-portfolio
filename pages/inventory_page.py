from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    inventory_container = (By.ID, "inventory_container")
    inventory_items = (By.CLASS_NAME, "inventory_item")
    backpack_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")


    def is_on_inventory_page(self):
        return "inventory" in self.driver.current_url 
        self.driver.find_element(*self.inventory_container).is_displayed()
    
    def are_products_visible(self):
        items = self.driver.find_elements(*self.inventory_items)
        return len(items) > 0
    
    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack_add_to_cart_button).click()

        

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text
    
    def click_cart_icon(self):
        self.driver.find_element(*self.cart_icon).click()
    
    
    

        

    