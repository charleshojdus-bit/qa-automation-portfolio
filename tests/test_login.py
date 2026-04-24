from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage

def test_login_success(driver):
    
        login_page = LoginPage(driver)
        login_page.open()

      

        login_page.login("standard_user", "secret_sauce")
        assert login_page.is_on_inventory_page()

    

def test_login_invalid_password(driver):
    try:
        login_page = LoginPage(driver)
        login_page.open()

        print("Current URL:", driver.current_url)
        print("Page title:", driver.title)

        login_page.login("standard_user", "wrongpassword")
        error = login_page.get_error_message()
        assert "epic sadface" in error.lower()

    except TimeoutException:
        print("DEBUG URL:", driver.current_url)
        print("DEBUG TITLE:", driver.title)
        driver.save_screenshot("login_debug_invalid.png")
        raise

def test_login_empty_fields(driver):
    try:
        login_page = LoginPage(driver)
        login_page.open()

        print("Current URL:", driver.current_url)
        print("Page title:", driver.title)

        login_page.click_login()
        error = login_page.get_error_message()
        assert "required" in error.lower(), "Error message not displayed for empty login"

    except TimeoutException:
        print("DEBUG URL:", driver.current_url)
        print("DEBUG TITLE:", driver.title)
        driver.save_screenshot("login_debug_empty_fields.png")
        raise

def test_login_missing_password(driver):
    try:
        login_page = LoginPage(driver)
        login_page.open()

        print("Current URL:", driver.current_url)
        print("Page title:", driver.title)

        login_page.login("standard_user", "")
        error = login_page.get_error_message()
        assert"password is required" in error.lower()

    except TimeoutException:
        print("DEBUG URL:", driver.current_url)
        print("DEBUG TITLE:", driver.title)
        driver.save_screenshot("missing_password_error.png")
        raise

def test_locked_out_user(driver):
    login_page = LoginPage(driver)

    login_page.open()

    login_page.login("locked_out_user", "secret_sauce")

    error = login_page.get_error_message()

    assert "locked out" in error.lower()
    assert not login_page.is_on_inventory_page()

def test_invalid_username(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    login_page.login("wrong_user", "secret_sauce")

    assert login_page.is_error_displayed()



