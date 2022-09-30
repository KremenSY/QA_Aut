from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import constants as const
import time
from booking_filtration import BookingFiltration

class Booking(webdriver.Firefox):
    def __init__(self, driver_path=r"C:\SE_Drivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(3)
        # self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):  # for context manager
        if self.teardown:
            self.quit()

    def lend_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.XPATH,
            const.CURRENCY_BUTTON_XPATH
        )
        currency_element.click()
        selected_currency_element = self.find_element(
            By.CSS_SELECTOR,
            r'a[data-modal-header-async-url-param="changed_currency=1&selected_currency=USD"]'
        )
        time.sleep(1)
        selected_currency_element.click()

    def change_language(self):
        language_element = self.find_element(
            By.XPATH,
            const.LANGUAGE_BUTTON_XPATH
        )
        language_element.click()
        selected_language_element = self.find_element(
            By.CSS_SELECTOR,
            'a[hreflang="en-us"]'
        )
        time.sleep(1)
        selected_language_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        time.sleep(1)
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count):
        selection_element = self.find_element(By.CSS_SELECTOR, 'label[id="xp__guests__toggle"]')
        selection_element.click()
        time.sleep(1)
        adult_minus_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
        adult_plus_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
        # default_value = 2
        default = self.find_element(By.CSS_SELECTOR, 'span[data-bui-ref="input-stepper-value"]')
        default_value=int(default.get_property('innerHTML'))
        click_number = count - default_value
        if click_number > default_value:
            for i in range(1, click_number + 1):
                adult_plus_button.click()
        if click_number < default_value:
            for i in range(1, -click_number + 1):
                adult_minus_button.click()
                if i == 1:
                    break

    def submit_search(self):
        selection_element = self.find_element(By.CSS_SELECTOR, 'button[data-sb-id="main"]')
        selection_element.click()

    def apply_filtration(self, stars):
        filtration=BookingFiltration(driver=self)
        filtration.apply_star_rating(stars)
