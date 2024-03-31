from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

'''
@pytest.mark.usefixtures("setup_and_teardown")
class Test_register:

    def generate_email_using_time_stand(self):
        time_stamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        return "jack"+time_stamp+"@gmail.com"

    def test_register_form_with_valid_details(self):

        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()

        self.driver.find_element(By.ID,"input-firstname").send_keys('Jack')
        self.driver.find_element(By.ID,"input-lastname").send_keys('Jones')
        self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_using_time_stand())

        self.driver.find_element(By.ID,"input-telephone").send_keys('7208334345')
        self.driver.find_element(By.ID,"input-password").send_keys('123456')
        self.driver.find_element(By.ID,"input-confirm").send_keys('123456')
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@class='btn btn-primary']").click()
        expected_heading = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//h1[contains(text(),'Your Account Has Been Created!')]").text.__eq__(expected_heading)

    def test_register_with_all_fields(self):
        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()

        self.driver.find_element(By.ID, "input-firstname").send_keys('Jack')
        self.driver.find_element(By.ID, "input-lastname").send_keys('Jones')
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_using_time_stand())

        self.driver.find_element(By.ID, "input-telephone").send_keys('7208334345')
        self.driver.find_element(By.ID, "input-password").send_keys('123456')
        self.driver.find_element(By.ID, "input-confirm").send_keys('123456')
        self.driver.find_element(By.XPATH,"//div[@class='col-sm-10']/label/input[@value='1']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-primary']").click()
        expected_heading = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]").text.__eq__(
            expected_heading)

    def test_register_with_existing_email(self):
        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()

        self.driver.find_element(By.ID, "input-firstname").send_keys('Jack')
        self.driver.find_element(By.ID, "input-lastname").send_keys('Jones')
        self.driver.find_element(By.ID, "input-email").send_keys('jack@gmail.com')

        self. driver.find_element(By.ID, "input-telephone").send_keys('7208334345')
        self.driver.find_element(By.ID, "input-password").send_keys('123456')
        self.driver.find_element(By.ID, "input-confirm").send_keys('123456')
        self.driver.find_element(By.XPATH, "//div[@class='col-sm-10']/label/input[@value='1']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-primary']").click()
        expected_warning = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
            expected_warning)

    def test_register_with_blank_details(self):

        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()

        self.driver.find_element(By.XPATH, "//input[@class='btn btn-primary']").click()

        expected_firstname_warning = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//div[contains(text(),'First Name must be between 1 and 32 characters!')]").text.__contains__(
            expected_firstname_warning)

        expected_lastname_warning = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]").text.__contains__(
            expected_lastname_warning)

        expected_email_warning = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, "//div[contains(text(),'E-Mail Address does not appear to be valid!')]").text.__contains__(
            expected_email_warning)

        expected_TelNumber_warning = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//div[contains(text(),'Telephone must be between 3 and 32 characters!')]").text.__contains__(
            expected_TelNumber_warning)

        expected_password_warning = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH,"//div[contains(text(),'Password must be between 4 and 20 characters!')]").text.__contains__(
            expected_password_warning)

        expected_warning = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
            expected_warning)'''
