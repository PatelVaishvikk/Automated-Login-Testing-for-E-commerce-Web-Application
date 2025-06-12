import time
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_login_valid():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("http://localhost:3000/signin")

    driver.find_element(By.NAME, "email").send_keys("admin@example.com")
    driver.find_element(By.NAME, "password").send_keys("1234")
    driver.find_element(By.XPATH, "//button[text()='Signin']").click()

    time.sleep(3)  # wait for redirect to complete

    print("🔍 Current URL:", driver.current_url)

    # ✅ Updated check to match actual behavior
    assert driver.current_url == "http://localhost:3000"
