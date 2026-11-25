import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://ifs-server31.ifsdc150.honeywell.com:44340/login")
driver.maximize_window()
time.sleep(1)
wait_time=60
WebDriverWait(driver,wait_time).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='Username']"))).send_keys("v")
time.sleep(1)
WebDriverWait(driver,wait_time).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("Password1")
time.sleep(1)
# Test case 1: Verify login with invalid credentials
WebDriverWait(driver,wait_time).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']"))).click()
error_msg=WebDriverWait(driver,wait_time).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='modal-body' and text()=' Invalid user credentials ']")))
time.sleep(2)
expected_text="Invalid user credentials"
actual_text=error_msg.text.strip()
if actual_text==expected_text:
    print("error msg verified")
else:
    print(f"Error message mismatch: '{actual_text}'")
time.sleep(2)
driver.close()

# Test case 2: Verify login with valid credentials
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ser_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://ifs-server31.ifsdc150.honeywell.com:44340/login")
driver.maximize_window()
time.sleep(1)
wait_time=10
WebDriverWait(driver,wait_time).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='Username']"))).send_keys("va")
time.sleep(1)
WebDriverWait(driver,wait_time).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("Password1")
time.sleep(1)
WebDriverWait(driver,wait_time).until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']"))).click()
try:
    dashboard=WebDriverWait(driver,wait_time).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='tile ta-title-l active']")))
    print("Login successful, dashboard is displayed.")
except:
    print("Login failed or dashboard not found.")
time.sleep(10)
driver.close()