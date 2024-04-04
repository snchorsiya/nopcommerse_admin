import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Login_Admin_Page import Login_Admin_Page
from utilites.custom_logger import Log_Maker
from utilites.read_properties import Read_Config
from utilites import excel_utils


class Test_Admin_Login_Testdata_02:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".//TestData//admin_login_data.xlsx"
    status_list = []

    def test_valid_admin_login_testData(self, setup):
        self.logger.info("********** test_valid_admin_login_testData started ***********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.lp = Login_Admin_Page(self.driver)
        self.logger.info("===========Open Login Page===========")

        self.rows = excel_utils.get_row_count(self.path, "Sheet1")
        print("num of rows", self.rows)

        for row in range(2, self.rows+1):
            self.username = excel_utils.read_column(self.path, "Sheet1", row, 1)
            self.password = excel_utils.read_column(self.path, "Sheet1", row, 2)
            self.exp_login = excel_utils.read_column(self.path, "Sheet1", row, 3)

            self.lp.enter_username(self.username)
            self.logger.info("===== enter username =====")
            self.lp.enter_password(self.password)
            self.logger.info("===== enter password =====")
            self.lp.click_login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            self.logger.info("===== getting login title =" + act_title)
            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("===== Successfully login page title =====")
                    self.status_list.append("Pass")
                    self.lp.click_logout()
                    assert True
                elif self.exp_login == "No":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                    self.lp.click_logout()
            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("===== test data is failed =====")
                    self.status_list.append("Fail")
                elif self.exp_login == "No":
                    self.logger.info("test data is passed")
                    self.status_list.append("Pass")

        print("Status list is:", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test admin data driven test is Failed")
            assert False
        else:
            self.logger.info("Test admin data driven test is Passed")
            assert True
