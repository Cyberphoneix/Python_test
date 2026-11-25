from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(5)

search_box=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div/span/div/div[3]/div[2]/ul[1]/span/span[1]/li/span/a/div/label/i")

# print("is_displayed:",search_box.is_displayed())
# print("is_enabled:",search_box.is_enabled())
print(search_box.is_selected())


