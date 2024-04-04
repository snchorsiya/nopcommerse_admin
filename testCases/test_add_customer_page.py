import string
import time
import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Login_Admin_Page import Login_Admin_Page
from pageObjects.Dashboard_Admin_Page import Dashboard_Admin_Page
from utilites.read_properties import Read_Config
from utilites.custom_logger import Log_Maker
from pageObjects.Add_Customer_Page import Add_Customer_Page


class Test_Add_New_Customer_03:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_customer(self, setup):
        self.logger.info("**********Test_Add_New_Customer_03*********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.lp = Login_Admin_Page(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.logger.info("*********Login completed************")
        self.logger.info("**********Click on Link in Admin Dashboard*********")
        self.ad = Dashboard_Admin_Page(self.driver)
        self.ad.click_customers_menu()
        self.ad.click_customers_menu_option()
        time.sleep(3)
        self.logger.info("*************Starting add customer test************")
        self.add_customer = Add_Customer_Page(self.driver)
        title = self.driver.title
        print("*******Print the title*********", title)
        time.sleep(3)
        self.add_customer.btn_click_addnew()
        self.logger.info("************Providing customer info started**********")
        email = generate_random_email()
        self.add_customer.txt_enter_email(email)
        print(email)
        self.add_customer.txt_enter_password("Admin@123")
        self.add_customer.txt_enter_firstname("Sn")
        self.add_customer.txt_enter_lastname("Ch")
        self.add_customer.select_gender("Male")
        self.add_customer.txt_enter_dob("01/01/1997")
        self.add_customer.txt_enter_companyname("QACompany")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        self.add_customer.select_tax_exempt()
        self.add_customer.select_newsletter("Test store 2")
        self.logger.info("***********Test store 2 selected**********")
        self.add_customer.select_customer_role("Registered")
        self.add_customer.select_manager_of_vendor("Vendor 1")
        self.add_customer.txt_enter_admin_comments("Test admin comment")

        self.add_customer.btn_click_save()
        time.sleep(3)
        customer_add_success_text = "The new customer has been added successfully."
        success_text = self.driver.find_element(By.XPATH, "//div[@class='content-wrapper']/div[1]").text
        if customer_add_success_text in success_text:
            assert True
            self.logger.info("**********Test_Add_New_Customer_03 test passed************")
            self.driver.close()
        else:
            self.logger.info("**********Test_Add_New_Customer_03 test failed************")
            self.driver.close()
            assert False


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['gmail.com', 'yahoo.com', 'yopmail.com', 'outlook.com'])
    return f'{username}@{domain}'
