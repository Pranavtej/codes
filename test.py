from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch the browser and navigate to the page
driver = webdriver.Chrome()
driver.get('https://app.cloudqa.io/home/AutomationPracticeForm')

# Find the fields using Selenium's locators and perform actions on them
first_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'First Name')]/following-sibling::input")))
last_name_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Last Name')]/following-sibling::input")))
email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")))

first_name_field.send_keys('Pranav')
last_name_field.send_keys('Teja')
email_field.send_keys('pranavtejapathi@gmail.com')

# Submit the form
# submit_button = driver.find_element(By.ID, 'submit')
# submit_button.click()

# Wait for 5 seconds before closing the browser
time.sleep(50)

# Close the browser after the test is finished
# driver.quit()
