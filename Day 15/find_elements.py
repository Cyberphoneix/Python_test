from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
	driver.get("https://ifs-server14.ifsdc70.honeywell.com:44340")
	driver.maximize_window()
	wait = WebDriverWait(driver, 20)

	wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("syedadmin")
	wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("Password1")
	wait.until(EC.element_to_be_clickable((By.ID, "kc-form-buttons"))).click()

	wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Lesson Editor']"))).click()
	wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
	checkboxes = [
		checkbox
		for checkbox in driver.find_elements(By.XPATH, "//input[@type='checkbox']")
		if checkbox.is_displayed()
	]

	checkbox_texts = [get_checkbox_text(checkbox, index) for index, checkbox in enumerate(checkboxes, start=1)]

	print("Total checkboxes:", len(checkboxes))
	for index, text in enumerate(checkbox_texts, start=1):
		print(f"{index}. {text}")
finally:
	driver.quit()
