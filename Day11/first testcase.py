from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://IFS-SERVER34:44340/")
driver.maximize_window()
sleep(5)
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("default_username")
sleep(10)
username_field.clear()
username_field.send_keys("vadmin")
sleep(10)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("default_password")
sleep(10)
password_field.clear()
password_field.send_keys("Password1@")
driver.find_element(By.ID,"kc-form-buttons").click()
sleep(10)
actual_result=driver.title

expected_text="Honeywell | Immersive Field Simulator"

if actual_result==expected_text:
    print("Test case is passed")
else:
    print("Test case is failed")
