from selenium.webdriver.common.by import By


class Search_Page_Object:
    def __init__(self, driver):
        self.driver = driver

    valid_hp_product_link = "HP LP3065"
    no_product_message = "//p[contains(text(),'There is no product that matches the search criter')]"

    def display_the_status_of_valid_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_hp_product_link).is_displayed()

    def retrieve_no_product_message(self):
        return self.driver.find_element(By.XPATH, self.no_product_message).text
