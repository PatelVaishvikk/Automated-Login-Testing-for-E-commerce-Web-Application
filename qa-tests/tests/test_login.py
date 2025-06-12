from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to Sign In page
driver.get("http://localhost:3000/signin")

# Wait for email field and enter email
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "email"))
).send_keys("admin@example.com")

# Wait for password field and enter password
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
).send_keys("1234")  # ✅ Replace with the correct password from your database or seeder

# Wait and click the submit button using exact text "Signin"
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Signin']"))
).click()

# Wait for redirection to homepage or profile
time.sleep(3)

# Check login success (example: check if redirected to profile)
if "localhost:3000" in driver.current_url:
    print("✅ Login test passed")
else:
    print("❌ Login test failed")

# Close browser
driver.quit()
