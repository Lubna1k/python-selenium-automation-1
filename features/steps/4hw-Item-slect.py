from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add-to-cart-button")
OPEN_CART = (By.CSS_SELECTOR, '#nav-cart')
PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//input[@name='proceedToRetailCheckout']")
NAVIGATION_CART_COUNT = (By.CSS_SELECTOR, '#nav-cart-count')

def click_on_add_to_cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(4)


@when('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*OPEN_CART).click()
    sleep(4)


@then('verify cart has {expected_amount} item')
def verify_cart_has(context, expected_amount):
    actual_amount = context.driver.find_element(*NAVIGATION_CART_COUNT).text
    actual_amount = int(actual_amount)
    expected_amount = int(expected_amount)