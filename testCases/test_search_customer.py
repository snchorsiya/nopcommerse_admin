import string
import time
import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Login_Admin_Page import Login_Admin_Page
from pageObjects.Dashboard_Admin_Page import Dashboard_Admin_Page
from pageObjects.Add_Customer_Page import Add_Customer_Page
from pageObjects.Search_Customer_Page import Search_Customer_Page
from utilites.read_properties import Read_Config
from utilites.custom_logger import Log_Maker
from selenium.webdriver.common.action_chains import ActionChains


class Test_Search_Customer_04:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_search_customer_by_email(self, setup):
        self.logger.info("*************Test_Search_Customer_04_001_with email started*******")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.lp = Login_Admin_Page(self.driver)
        self.lp.enter_password(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.logger.info("**********Login completed***********")
        self.logger.info("*********Click on Link in Dashboard*********")
        self.ad = Dashboard_Admin_Page(self.driver)
        self.ad.click_customers_menu()
        self.ad.click_customers_menu_option()
        time.sleep(3)
        self.logger.info("***********Navigate to customer page***********")
        self.add_customer = Add_Customer_Page(self.driver)
        self.logger.info("***********Starting Customer Search By Email***********")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.txt_enter_customer_email("g46nmeu3@outlook.com")
        time.sleep(3)
        # js_code = self.driver.execute_script("arguments[0].scrollIntoView();")
        self.search_customer.btn_click_search()
        self.driver.execute_script("window.scrollTo(-10, document.body.scrollHeight)")
        time.sleep(5)
        is_email_present = self.search_customer.search_customer_by_email("g46nmeu3@outlook.com")
        if is_email_present == True:
            assert True
            self.logger.info("*************Test_Search_Customer_04_001_with email test passed*******")
            self.driver.close()
        else:
            self.logger.info("*************Test_Search_Customer_04_001_with email test failed******")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.logger.info("*************Test_Search_Customer_04_002_with name started*******")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.lp = Login_Admin_Page(self.driver)
        self.lp.enter_password(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.logger.info("**********Login completed***********")
        self.logger.info("*********Click on Link in Dashboard*********")
        self.ad = Dashboard_Admin_Page(self.driver)
        self.ad.click_customers_menu()
        self.ad.click_customers_menu_option()
        time.sleep(3)
        self.logger.info("***********Navigate to customer page***********")
        self.add_customer = Add_Customer_Page(self.driver)
        self.logger.info("***********Starting Customer Search By Name***********")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.txt_enter_customer_firstname("Sn")
        self.search_customer.txt_enter_customer_lastname("Ch")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.search_customer.btn_click_search()
        self.driver.execute_script("window.scrollTo(-10, document.body.scrollHeight)")
        time.sleep(5)
        is_name_present = self.search_customer.search_customer_by_name("Sn Ch")
        if is_name_present == True:
            assert True
            self.logger.info("*************Test_Search_Customer_04_002_with name test passed*******")
            self.driver.close()
        else:
            self.logger.info("*************Test_Search_Customer_04_002_with name test failed******")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_companyname(self, setup):
        self.logger.info("*************Test_Search_Customer_04_003_with companyname started*******")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.lp = Login_Admin_Page(self.driver)
        self.lp.enter_password(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.logger.info("**********Login completed***********")
        self.logger.info("*********Click on Link in Dashboard*********")
        self.ad = Dashboard_Admin_Page(self.driver)
        self.ad.click_customers_menu()
        self.ad.click_customers_menu_option()
        time.sleep(3)
        self.logger.info("***********Navigate to customer page***********")
        self.add_customer = Add_Customer_Page(self.driver)
        self.logger.info("***********Starting Customer Search By CompanyName***********")
        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.txt_enter_customer_companyname("QACompany")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.search_customer.btn_click_search()
        self.driver.execute_script("window.scrollTo(-10, document.body.scrollHeight)")
        time.sleep(5)
        is_companyname_present = self.search_customer.search_customer_by_company("QACompany")
        if is_companyname_present == True:
            assert True
            self.logger.info("*************Test_Search_Customer_04_003_with companyname test passed*******")
            self.driver.close()
        else:
            self.logger.info("*************Test_Search_Customer_04_003_with companyname test failed******")
            self.driver.close()
            assert False
