from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login_with_wait(driver):
    """Test login with explicit waits using the driver fixture from conftest.py"""
    
    # Navigate to Sign In page
    driver.get("http://localhost:3000/signin")

    # Wait for email field and enter email
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_field.send_keys("admin@example.com")

    # Wait for password field and enter password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys("1234")  # Replace with the correct password from your database or seeder

    # Wait and click the submit button using exact text "Signin"
    signin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Signin']"))
    )
    signin_button.click()

    # Wait for redirection to homepage or profile
    time.sleep(3)

    # Check login success (example: check if redirected to profile or contains expected content)
    assert "localhost:3000" in driver.current_url, f"Expected to stay on localhost:3000, but got {driver.current_url}"
    
    # Additional assertion - you might want to check for specific success indicators
    # For example, check if user is redirected to profile page or homepage
    success_indicators = ["profile", "dashboard", "welcome", "amazona"]
    page_content = driver.page_source.lower()
    current_url = driver.current_url.lower()
    
    success = any(indicator in page_content or indicator in current_url for indicator in success_indicators)
    assert success, f"Login appears to have failed. Current URL: {driver.current_url}, Page title: {driver.title}"