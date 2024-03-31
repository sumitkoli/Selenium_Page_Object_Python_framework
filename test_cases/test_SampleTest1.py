import pytest

from pages.HomePage import HomePage_Object
from pages.Search_Page import Search_Page_Object


@pytest.mark.usefixtures("setup_and_teardown")
class Test_Search:

    def test_search_for_a_valid_product(self):
        home_page = HomePage_Object(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        home_page.click_on_search_button()
        search_page = Search_Page_Object(self.driver)
        assert search_page.display_the_status_of_valid_product()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage_Object(self.driver)
        home_page.enter_product_into_search_box_field('Honda')
        home_page.click_on_search_button()
        expectedtext="There is no product that matches the search criteria."
        search_page = Search_Page_Object(self.driver)
        assert search_page.retrieve_no_product_message().__eq__(expectedtext)

    def test_search_for_blank_value(self):
        home_page = HomePage_Object(self.driver)
        home_page.enter_product_into_search_box_field('')
        home_page.click_on_search_button()

        expectedtext = "There is no product that matches the search criteria."
        search_page = Search_Page_Object(self.driver)
        assert search_page.retrieve_no_product_message().__eq__(expectedtext)