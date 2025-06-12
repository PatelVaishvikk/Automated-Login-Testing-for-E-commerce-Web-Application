from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile
import time

def test_login_valid():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    # Navigate to signin page
    driver.get("http://localhost:3000/signin")

    # Fill credentials and click login
    driver.find_element(By.NAME, "email").send_keys("admin@example.com")
    driver.find_element(By.NAME, "password").send_keys("1234")
    driver.find_element(By.XPATH, "//button[text()='Signin']").click()

    # Allow time for redirect
    time.sleep(3)
    print("🔍 Current URL:", driver.current_url)
    assert driver.current_url.rstrip('/') == "http://localhost:3000"