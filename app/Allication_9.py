from pages.header import Header
from pages.main_page import MainPage
from pages.search_results import SearchResultsPage
from pages.cart_page import CartPage
from pages.sign_in_page import SignInPage
from pages.product_page import ProductPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.product_page = ProductPage(self.driver)