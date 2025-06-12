from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile

def test_login_valid():
    options = Options()
    options.add_argument("--headless")  # for CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ✅ this ensures unique user-data-dir every time
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("http://localhost:3000/signin")

    driver.find_element(By.NAME, "email").send_keys("admin@example.com")
    driver.find_element(By.NAME, "password").send_keys("1234")
    driver.find_element(By.XPATH, "//button[text()='Signin']").click()

    assert "profile" in driver.current_url
    driver.quit()
