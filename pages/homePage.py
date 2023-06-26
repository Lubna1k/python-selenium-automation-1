from pages.base_page import HomePage


class HomePage(HomePage):

    def open_home_page(self):
        self.open_url('https://www.amazon.com/')