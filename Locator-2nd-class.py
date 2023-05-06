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
sleep(4)
driver.find_element(By.CLASS_NAME, 'a-icon a-icon-logo')
driver.find_elements(By.XPATH, "//a[@href='/ref=nav_logo")
driver.find_element(By.XPATH, "//a")
driver.find_element(By.XPATH, "//*[@href='/ref=nav_logo")
driver.find_element(By.XPATH, "//*[@href='/ref=nav_logo' and @aria-label='Amazon']")
#driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")

driver.find_element(By.CLASS_NAME, "a-expander-prompt")
driver.find_element(By.CLASS_NAME, "Need help?")
driver.find_element(By.XPATH, "//span[contains(text(), 'Need')]")
#Forgot your password
driver.find_element(By.ID, "auth-fpp-link-bottom")
#sign in link
driver.find_element(By.ID, "ap-other-signin-issues-link")

####create amazon account
driver.find_element(By.CSS_SELECTOR, 'createAccountSubmit')

##conditions of use link
driver.find_element(By.CSS_SELECTOR, 'a*[href="condition_of_use"]')

#####privacy notice link
driver.find_element(By.CSS_SELECTOR, 'a[href*="notification_privacy_notice"]')
driver.quit()
