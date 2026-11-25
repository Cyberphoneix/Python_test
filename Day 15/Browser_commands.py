from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
sleep(10)
driver.back()
driver.forward()
driver.find_element(By.XPATH,"//a[text()='OrangeHRM, Inc']").click()
sleep(10)
driver.quit()
sleep(30)
driver.back()
driver.forward()