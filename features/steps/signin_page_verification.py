from selenium.webdriver.common.by import By
from behave import given, when, then

#test order page 7
ORDERS_PAGE = (By.ID, "nav-orders")
SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")


@given("User is on Amazon homepage")
def open_amazon(context):
    context.app.home_page.open_home_page()


@when("User navigates to signin page")
def open_orders_page(context):
    """

    :param context:
    """
    context.app.base_page.click(*ORDERS_PAGE)


@then("The sign-in page is displayed")
def verify_signin(context):
    context.app.base_page.verify_partial_text('Sign in', *SIGNIN_TEXT)


@step("I click on 'Go to Cart' button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I click on \'Go to Cart\' button')