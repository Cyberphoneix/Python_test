from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://IFS-SERVER34:44340")

waitcommand=WebDriverWait(driver,10)
waitcommand.until(EC.presence_of_element_located((By.XPATH,"//input[@id='username']"))).send_keys("ifsadmin")
waitcommand.until(EC.presence_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("Password1!")
waitcommand.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='kc-login']"))).click()
waitcommand.until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class, 'dropdown-item') and contains(text(), ' Starter_kit assets')]"))).click()
name=waitcommand.until(EC.presence_of_element_located((By.XPATH,"//a[contains(@class, 'dropdown-item') and contains(text(), ' Starter_kit assets')]"))).text
print("Plant_name:",name)
