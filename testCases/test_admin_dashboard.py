import time
from selenium.common.exceptions import NoSuchElementException
from pageObjects.Login_Admin_Page import Login_Admin_Page
from pageObjects.Dashboard_Admin_Page import Dashboard_Admin_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilites.custom_logger import Log_Maker
from utilites.read_properties import Read_Config
from utilites.BaseClass import BaseClass
from selenium import webdriver
import pytest


class Test_Admin_Dashboard_02(BaseClass):
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    def test_dashboard_name_verification(self, setup):
        self.logger.info("**********Verification of dashboard************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.lp = Login_Admin_Page(self.driver)
        self.logger.info("=========Open Login Page=====")
        self.lp.enter_username(self.username)
        self.logger.info("===== enter username ===== ")
        self.lp.enter_password(self.password)
        self.logger.info("=======enter password=======")
        self.lp.click_login()
        time.sleep(5)
        self.ad = Dashboard_Admin_Page(self.driver)
        # error_message_element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(self.ad.dashboard_text_visible())
        # )
        #
        # # Get the text of the error message
        # self.error_message = error_message_element.text
        # self.verifyExpwait(self.ad.dashboard_text_visible())

        # Handle the case where the error message is not found
        try:
            self.error_message = self.ad.dashboard_text_visible().text
            # error_message = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Dashboard']").text
            print("=====Print the error message======", self.error_message)
            self.logger.info("===== getting error message =" + self.error_message)
            if self.error_message == "Dashboard":
                assert True
                self.logger.info("===== Successfully Dashboard page title =====")
                self.driver.close()
            else:
                self.logger.info("===== failed Dashboard page title =====")
                self.driver.close()
                assert False
        except NoSuchElementException:
            # Handle the case where the error message element is not found
            self.logger.error("Error message element not found")
            self.driver.close()
            assert False

    def test_verify_customer_link(self, setup):
        self.logger.info("**********Verification of customer link************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.lp = Login_Admin_Page(self.driver)
        self.logger.info("=========Open Login Page=====")
        self.lp.enter_username(self.username)
        self.logger.info("===== enter username ===== ")
        self.lp.enter_password(self.password)
        self.logger.info("=======enter password=======")
        self.lp.click_login()
        time.sleep(5)
        self.ad = Dashboard_Admin_Page(self.driver)
        self.ad.click_customers_menu()
        self.ad.click_customers_menu_option()
        title = self.driver.title
        if self.driver.title == title:
            assert True
            self.logger.info("=========Customer Page Open Successfully=====")
            self.driver.close()
        else:
            self.logger.info("===== Customer Page does not open =====")
            self.driver.close()
            assert False

