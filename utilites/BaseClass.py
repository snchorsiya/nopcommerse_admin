import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.Login_Admin_Page import Login_Admin_Page
from pageObjects.Dashboard_Admin_Page import Dashboard_Admin_Page
from pageObjects.Add_Customer_Page import Add_Customer_Page
from pageObjects.Search_Customer_Page import Search_Customer_Page


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyExpwait(self, error_message_element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, error_message_element)))
