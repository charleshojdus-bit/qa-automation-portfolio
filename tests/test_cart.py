from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_open_cart(driver):
   
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add item and open cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.click_cart_icon()

    
    cart_page = CartPage(driver)
    assert cart_page.is_item_in_cart("Sauce Labs Backpack")

def test_remove_item_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.click_cart_icon()

    cart_page = CartPage(driver)
    assert cart_page.is_item_in_cart("Sauce Labs Backpack")
    cart_page.remove_item()

    assert cart_page.is_cart_empty()

    