from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.click_cart_icon()

    assert cart_page.is_item_in_cart("Sauce Labs Backpack")

    cart_page.click_checkout()

    checkout_page.enter_first_name("Charles")
    checkout_page.enter_last_name("Hojdus")
    checkout_page.enter_postal_code("19101")
    checkout_page.click_continue()
    checkout_page.click_finish()

    assert checkout_page.get_confirmation_message() == "Thank you for your order!"