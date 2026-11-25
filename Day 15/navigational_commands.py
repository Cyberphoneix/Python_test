from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
sleep(5)
driver.get("https://www.amazon.in/")
sleep(5)
driver.back()
sleep(5)
driver.forward()
sleep(5)