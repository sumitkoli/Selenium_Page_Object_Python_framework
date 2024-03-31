from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

'''
@pytest.mark.usefixtures("setup_and_teardown")
class Test_Login:
    def generate_email_using_time_stand(self):
        time_stamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        return "jack" + time_stamp + "@gmail.com"

    def test_login_with_valid_credentails(self):

        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()

        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys('jack65@gmail.com')
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys('123456')

        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

        assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()

    def test_login_with_invalid_email_valid_password(self):

        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self. driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()

        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(self.generate_email_using_time_stand())
        self. driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys('123456')

        self. driver.find_element(By.XPATH, "//input[@value='Login']").click()

        expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
            expected_warning_msg)

    def test_login_with_valid_email_invalid_password(self):


        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()

        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys('jack65@gmail.com')
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys('12345677')

        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

        expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__contains__(
            expected_warning_msg)

    def test_login_with_invalid_email_invalid_password(self):

        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()

        self. driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(self.generate_email_using_time_stand())
        self. driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys('12345677')

        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

        expectedtxt = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__eq__(
            expectedtxt)

    def test_login_with_blank_email_blank_password(self):
        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()

        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys()
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys()

        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

        expectedtxt = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text.__eq__(
            expectedtxt)'''
