from selenium.webdriver.common.by import By
import time

def test_valid_login(driver):
    driver.get("http://localhost:3000/signin")
    driver.find_element(By.ID, "email").send_keys("admin@example.com")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.XPATH, "//button[text()='Signin']").click()
    time.sleep(2)
    assert "profile" in driver.page_source or "amazona" in driver.page_source
