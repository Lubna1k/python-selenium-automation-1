from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#test order page verification
@given("User is on Amazon homepage")
def open_amazon(context):
    context.driver.get("https://www.amazon.com")


@when("User navigates to the orders page")
def open_orders_page(context):
    context.driver.find_element(By.ID, "nav-orders").click()


@then("The sign-in page is displayed")
def verify_signin(context):
    expected_text = "Sign in"
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_text == actual_result, f"Expected {expected_text} but got {actual_result}"
    assert context.driver.find_element(By.ID, "ap_email")


def step(param):
    pass


def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I click on an item \'add to card\' button')


def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And I click on \'Add to Cart\' button')


def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And open item page')


@step("open item page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And open item page')