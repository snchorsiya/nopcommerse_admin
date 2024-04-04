import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


class Add_Customer_Page:
    btn_add_new_xpath = "//a[normalize-space()='Add new']"
    text_email_id = "Email"
    text_password_id = "Password"
    text_fname_id = "FirstName"
    text_lname_id = "LastName"
    rdo_gender_male_id = "Gender_Male"
    rdo_gender_female_id = "Gender_Female"
    text_dob_id = "DateOfBirth"
    text_companyname_id = "Company"
    chbx_tax_exempt_id = "IsTaxExempt"
    drp_newsletter_cusrole_list_xpath = "//div[@role='listbox']"
    # drp_newsletter_cusrole_list_xpath = "//select[@id='SelectedNewsletterSubscriptionStoreIds']"
    cusrole_guests_xpath = "//li[contains(text(),'Guests')]"
    cusrole_administrators_xpath = "//li[contains(text(),'Administrators')]"
    cusrole_forummoderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    cusrole_registered_xpath = "//li[contains(text(),'Registered')]"
    cusrole_vendors_xpath = "//li[contains(text(),'Vendors')]"
    drpdwn_mngofvendor_id = "VendorId"
    text_admincomment_id = "AdminComment"
    btn_save_name = "save"

    def __init__(self, driver):
        self.driver = driver

    def btn_click_addnew(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_xpath).click()

    def txt_enter_email(self, email):
        self.driver.find_element(By.ID, self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def txt_enter_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def txt_enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.text_fname_id).clear()
        self.driver.find_element(By.ID, self.text_fname_id).send_keys(firstname)

    def txt_enter_lastname(self, lname):
        self.driver.find_element(By.ID, self.text_lname_id).send_keys(lname)

    def select_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdo_gender_male_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()
        else:
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()

    def txt_enter_dob(self, dob):
        self.driver.find_element(By.ID, self.text_dob_id).clear()
        self.driver.find_element(By.ID, self.text_dob_id).send_keys(dob)

    def txt_enter_companyname(self, companyname):
        self.driver.find_element(By.ID, self.text_companyname_id).clear()
        self.driver.find_element(By.ID, self.text_companyname_id).send_keys(companyname)

    def select_tax_exempt(self):
        self.driver.find_element(By.ID, self.chbx_tax_exempt_id).click()
        time.sleep(3)

    def select_newsletter(self, value):
        elements = self.driver.find_elements(By.XPATH, self.drp_newsletter_cusrole_list_xpath)
        newsletter_field = elements[0]
        newsletter_field.click()
        time.sleep(3)
        if value == "Your store name":
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Your store name')]").click()
        elif value == "Test store 2":
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Test store 2')]").click()
        else:
            self.driver.find_element(By.XPATH, "//li[contains(text(),'Your store name')]").click()

    def select_customer_role(self, role):
        elements = self.driver.find_elements(By.XPATH, self.drp_newsletter_cusrole_list_xpath)
        customer_field = elements[1]
        customer_field.click()
        time.sleep(3)
        if role == "Guests":
            self.driver.find_element(By.XPATH, self.cusrole_registered_xpath).click()
            time.sleep(3)
            customer_field.click()
            self.driver.find_element(By.XPATH, self.cusrole_guests_xpath).click()
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.cusrole_administrators_xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.cusrole_forummoderators_xpath).click()
        elif role == "Registered":
            pass
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.cusrole_vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.cusrole_administrators_xpath).click()

    def select_manager_of_vendor(self, value):
        drp_dwn = Select(self.driver.find_element(By.ID, self.drpdwn_mngofvendor_id))
        drp_dwn.select_by_visible_text(value)

    def txt_enter_admin_comments(self, admincomments):
        self.driver.find_element(By.ID, self.text_admincomment_id).clear()
        self.driver.find_element(By.ID, self.text_admincomment_id).send_keys(admincomments)

    def btn_click_save(self):
        self.driver.find_element(By.NAME, self.btn_save_name).click()







