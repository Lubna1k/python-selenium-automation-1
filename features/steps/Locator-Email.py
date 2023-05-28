from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()
expected_text: str = 'Sign in'
actual_text = driver.find_element(By.CLASS_NAME, "a-spacing-small")
expected_text = 'email or phone'
actual_result = driver.find_element(By.ID, "ap_email")
driver.find_element(By.CLASS_NAME, 'a-expander-prompt')
#CONTINUE BUTTON
driver.find_element(By.CLASS_NAME, 'a-button-input')