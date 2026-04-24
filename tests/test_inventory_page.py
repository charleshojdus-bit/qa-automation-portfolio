from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.common.exceptions import TimeoutException


def test_inventory_page_loads(driver):
    try:
        login_page = LoginPage(driver)
        login_page.open()

        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)

        assert inventory_page.is_on_inventory_page()
        assert inventory_page.are_products_visible()

    except TimeoutException:
        print("DEBUG URL:", driver.current_url)
        print("DEBUG TITLE:", driver.title)
        driver.save_screenshot("inventory_page_debug.png")
        raise
         
def test_add_item_to_cart(driver):
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce") 

        inventory_page = InventoryPage(driver)

        assert inventory_page.is_on_inventory_page()
        assert inventory_page.are_products_visible()

        inventory_page.add_backpack_to_cart()

        assert inventory_page.get_cart_count() == "1"

    except (TimeoutException, AssertionError):
        print("DEBUG URL:", driver.current_url)
        print(" DEBUG TITLE:", driver.title)
        driver.save_screenshot("add_to_cart_debug.png")
        raise

