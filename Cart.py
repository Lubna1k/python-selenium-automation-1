from selenium.webdriver.common.by import By
from pages.base_page import Page
# from selenium.webdriver.support import expected_conditions as EC
#from pages.header import Page


class Cart(Page):
    CART_COUNT = (By.ID, 'nav-cart-count')
    CART_EMPTY_MESSAGE = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")

    def click_cart_icon(self):
        self.click(*self.CART_COUNT)

    def verify_empty(self):
        found = self.find_element(*self.CART_EMPTY_MESSAGE)

        if found is None:
            return False
        else:
            return True