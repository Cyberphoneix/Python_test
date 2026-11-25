from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://money.rediff.com/sectors/bse/energy")
driver.maximize_window()
sleep(5)
text_msg=driver.find_element(By.XPATH,"//a[@href='//money.rediff.com/companies/GAIL-India-Ltd/15120010']/self::a").text
print("Text message:",text_msg)