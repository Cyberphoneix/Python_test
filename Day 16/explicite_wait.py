from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, TimeoutException
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
# mywait=WebDriverWait(driver,10)
mywait=WebDriverWait(driver,10,poll_frequency=1,ignored_exceptions=)
driver.get("https://www.Amazon.in/")
driver.maximize_window()

searchlink=mywait.until(EC.presence_of_element_located((By.LINK_TEXT,"Sell")))
searchlink.click()

//*[@id="navbarNav"]/ul[2]/li[3]/a/button