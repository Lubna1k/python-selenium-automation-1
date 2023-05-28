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
driver.get('https://www.amazon.com')

driver.find_element(By.ID, 'nav-orders').click()
#Amazon Logo
driver.find_element(By.CSS_SELECTOR, "i[role='img'][aria-label='Amazon']")
# Creat account
driver.find_element(By.CLASS_NAME, 'a-spacing-small')

#email field
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#continue button
driver.find_element(By.CSS_SELECTOR, '#continue')


#need help link
driver.find_element(By.CSS_SELECTOR, '.a-expander-prompt')
#Forgot your password link, this would need a comment
driver.find_element(By.CSS_SELECTOR, 'auth-fpp-link-bottom')
#other issues with sign in link
driver.find_element(By.CSS_SELECTOR, 'ap-other-signin-issues-link')
#create amazon account
driver.find_element(By.CSS_SELECTOR, 'createAccountSubmit')
#conditions of use link
driver.find_element(By.CSS_SELECTOR, "a*[href='condition_of_use']")
driver.find_element(By.ID, "legalTextRow")
#privacy notice link
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice']").click()