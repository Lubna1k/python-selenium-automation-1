from behave import when, then
from selenium.webdriver.common.by import By

CART_COUNT = (By.ID, 'nav-cart-count')
CART_EMPTY_MESSAGE = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")


@when('Click on cart icon')
def open_cart_page(context):
    #context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    context.app.cart.click_cart_icon()


@then('Verify "Your Shopping Cart is empty" text present')
def verify_cart_verify_empty_text(context):
    # empty_msg = context.driver.find_element(*CART_EMPTY_MESSAGE).text
    # print(empty_msg)
    context.app.cart.verify_empty()

    assert context.app.cart.verify_empty() is True