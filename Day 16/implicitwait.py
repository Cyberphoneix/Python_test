from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.implicitly_wait(60)
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.NAME,"q").send_keys("selenium")
driver.find_element(By.NAME,'q').submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()