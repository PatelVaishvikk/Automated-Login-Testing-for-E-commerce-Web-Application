from selenium.webdriver.common.by import By
import time

def test_invalid_login(driver):
    driver.get("http://localhost:3000/signin")
    driver.find_element(By.ID, "email").send_keys("wrong@example.com")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.XPATH, "//button[text()='Signin']").click()
    time.sleep(2)
    assert "Invalid email or password" in driver.page_source or "signin" in driver.current_url
