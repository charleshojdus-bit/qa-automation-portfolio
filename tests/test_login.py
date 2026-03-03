from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def test_login_success():
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")

        username = wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        password = wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )

        username.send_keys("Admin")
        password.send_keys("admin123")
        password.send_keys(Keys.RETURN)

        wait.until(EC.url_contains("dashboard"))

        assert "dashboard" in driver.current_url.lower()
        print("✅ Positive Login Test Passed")
    finally:
        driver.quit()

def test_login_invalid_password():
    driver = setup_driver()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        username = wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        password = wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        
        username.send_keys("Admin")
        password.send_keys("wrongpassword")
        password.send_keys(Keys.RETURN)
        error_message = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-alert-content-text"))
        )
        

        assert "invalid" in error_message.text.lower()
        print("✅ Negative Login Test Passed")

    finally:
        driver.quit()

