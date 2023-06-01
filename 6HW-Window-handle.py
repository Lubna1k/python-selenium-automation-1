from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep

ORIGINAL_PAGE = 'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'
PRIVACY_NOTICE = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_amazon_t_and_c_page(context):
    context.driver.get(ORIGINAL_PAGE)
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('This is the id for this window:',context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_on_amazon_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print('Original window id, second window id: ', windows)

    context.driver.switch_to.window(windows[1])
    context.current_window = context.driver.current_window_handle
    print('After we switched, this is the window id: ')
    print(context.current_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_page_opens(context):
    #context.driver.wait.until(EC.title_contains('privacy'))
    context.driver.wait.until(EC.url_contains("customer"))


@then('User can close new window and switch back to original')
def user_can_close_new_window_switching_back_to_original(context):
    context.driver.close()

    context.driver.switch_to.window(context.original_window)
    current_url = context.driver.current_url
    assert current_url == ORIGINAL_PAGE, f"Expected URL not found"