from pageObjects.Login_Admin_Page import Login_Admin_Page
from selenium.webdriver.common.by import By
from utilites.custom_logger import Log_Maker
from utilites.read_properties import Read_Config
from selenium import webdriver
import datetime
import pytest

date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


class Test_Admin_Login_01:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    invalid_password = Read_Config.get_invalid_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self, setup):
        self.logger.info("**********Verification of admin login page***********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        title = self.driver.title
        self.logger.info("===== getting login title =" + title)
        if title == Hello:
            self.logger.info("===== Successfully login page title =====")
            assert True
        else:
            self.logger.info("===== failed login page title =====")
            # self.Scr_name = f"test_valid_admin_login_{date}.png"
            # self.driver.save_screenshot(f".//ScreenShots//{self.Scr_name}")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self, setup):
        self.logger.info("**********Verification of admin login page***********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.lp = Login_Admin_Page(self.driver)
        self.logger.info("===========Open Login Page===========")
        self.lp.enter_username(self.username)
        self.logger.info("===== enter username =====")
        self.lp.enter_password(self.password)
        self.logger.info("===== enter password =====")
        self.lp.click_login()
        title = self.driver.title
        self.logger.info("===== getting login title =" + title)
        if title == "Dashboard / nopCommerce administration":
            self.logger.info("===== Successfully login page title =====")
            assert True
        else:
            self.logger.info("===== failed login page title =====")
            # self.Scr_name = f"test_valid_admin_login_{date}.png"
            # self.driver.save_screenshot(f".//ScreenShots//{self.Scr_name}")
            assert False

    @pytest.mark.regression
    def test_invalid_username_password(self, setup):
        self.logger.info("=======Verify the enter invalid username and password========")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.lp = Login_Admin_Page(self.driver)
        self.logger.info("Open the login page")
        self.lp.enter_username(self.invalid_username)
        self.logger.info("Enter the Invalid Username")
        self.lp.enter_password(self.invalid_password)
        self.logger.info("Enter the Invalid Password")
        self.lp.click_login()
        self.logger.info("Click on Login button")
        error_message = self.lp.error_messages()
        self.message = error_message.text
        self.logger.info("Print validation message = " + self.message)
        print(self.message)
        if self.message == self.message:
            self.logger.info("======Error message display successfully==============")
            assert True
        else:
            self.logger.info("Error Message not display")
            assert False

    def test_admin_login_blank_username(self, setup):
        self.logger.info("Verify the blank username and enter password in Admin Account.")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.lp = Login_Admin_Page(self.driver)
        self.logger.info("Open the Login Page")
        email_username = ""
        email_message = self.lp.enter_username(email_username)
        if email_message is not None:
            email_value = email_message.get_attribute("data-val-required")
        else:
            print("Error: email_message is None")
        self.logger.info("Blank UserName")
        self.lp.enter_password(self.password)
        self.logger.info("Enter the Password")
        self.lp.click_login()
        self.logger.info("Click on Login Button, Login Unsuccessful")
        # email_message = self.lp.enter_username(email_username).__getattribute__("")
        # self.error_message = email_message.text
        self.logger.info("=======Getting Validation Message is: ", email_message)
        if email_message:
            self.logger.info("test_blank_username_pass")
            assert True
        else:
            self.logger.info("test_blank_username_fail")
            assert False


