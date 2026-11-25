from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
sleep(5)
print(driver.title)
print(driver.current_url)
print(driver.page_source)



