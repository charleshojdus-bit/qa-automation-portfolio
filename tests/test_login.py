from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.login_page import LoginPage

def test_login_success(driver):
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://www.saucedemo.com/")

        print("Current URL:", driver.current_url)
        print("Page title:", driver.title)

        username = wait.until(
            EC.visibility_of_element_located(LoginPage.username_input)
        )
        password = wait.until(
            EC.visibility_of_element_located(LoginPage.password_input)
        )
        login_button = wait.until(
            EC.element_to_be_clickable(LoginPage.login_button)
        )
        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

        wait.until(EC.url_contains("inventory"))
        assert "inventory" in driver.current_url.lower()

    except TimeoutException:
        print("DEBUG URL:", driver.current_url)
        print("DEBUG TITLE:", driver.title)
        driver.save_screenshot("login_debug_success.png")
        raise

def test_login_invalid_password(driver):
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://www.saucedemo.com/")

        print("Current URL:", driver.current_url)
        print("Page title:", driver.title)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "wrongpassword")

        error = login_page.get_error_message()
        assert "epic sadface" in error.lower()

        

    except TimeoutException:
        print("DEBUG URL:", driver.current_url)
        print("DEBUG TITLE:", driver.title)
        driver.save_screenshot("login_debug_invalid.png")
        raise

def test_login_locked_user(driver):
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://www.saucedemo.com/")

        print("Current URL:", driver.current_url)
        print("Page title:", driver.title)

        username = wait.until(
            EC.visibility_of_element_located(LoginPage.username_input)
        )
        password = wait.until(
            EC.visibility_of_element_located(LoginPage.password_input)
        )
        login_button = wait.until(
            EC.element_to_be_clickable(LoginPage.login_button)
        )

        username.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        login_button.click()

        error = wait.until(
            EC.visibility_of_element_located(LoginPage.error_message)
        )

        assert "locked out" in error.text.lower()

    except TimeoutException:
        print("DEBUG URL:", driver.current_url)
        print("DEBUG TITLE:", driver.title)
        driver.save_screenshot("login_debug_locked.png")
        raise
    

        
        
