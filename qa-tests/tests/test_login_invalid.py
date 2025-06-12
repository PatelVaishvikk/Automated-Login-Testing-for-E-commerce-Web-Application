# from selenium.webdriver.common.by import By
# import time

# def test_invalid_login(driver):
#     driver.get("http://localhost:3000/signin")
#     driver.find_element(By.ID, "email").send_keys("wrong@example.com")
#     driver.find_element(By.ID, "password").send_keys("wrongpassword")
#     driver.find_element(By.XPATH, "//button[text()='Signin']").click()
#     time.sleep(2)
#     assert "Invalid email or password" in driver.page_source or "signin" in driver.current_url
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import tempfile

def test_login_invalid():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    # ✅ TEMP directory to avoid user-data-dir error
    chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("http://localhost:3000/signin")

    driver.find_element(By.NAME, "email").send_keys("wrong@example.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.XPATH, "//button[text()='Signin']").click()

time.sleep(3)
print("🔍 Current URL:", driver.current_url)
assert driver.current_url.rstrip('/') == "http://localhost:3000"