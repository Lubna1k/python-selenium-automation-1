from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given
from behave import then

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
BS_FIVE_CATEGORIES = (By.XPATH, "//a[contains(@href, 'ref=zg_bs_tab')]")
BESTSELLERS_CATEGORIES_BAR = (By.CSS_SELECTOR, "div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq")


@given('Open Amazon Best seller')
def open_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    sleep(4)


@then('Verify that Bestsellers categories are present')
def click_on_bs(context):
    result = context.driver.find_element(*BESTSELLERS_CATEGORIES_BAR)
    assert result != None


@then('Verify that Best Sellers has {expected_amounts} links')
def verify_five_links_count(context, expected_amounts):
    print('Original Type:', type(expected_amounts))
    expected_amounts = int(expected_amounts)
    print('Type after converting:', type(expected_amounts))
    bestsellers_links = context.driver.find_elements(*BS_FIVE_CATEGORIES)
    print(bestsellers_links)
    print('numbers of links:', len(bestsellers_links))
    # asserting that the count of footer links is equal
    assert len(
        bestsellers_links) == expected_amounts, f'Expected {expected_amounts} links, but got {len(bestsellers_links)}'

