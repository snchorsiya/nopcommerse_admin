from selenium.webdriver.common.by import By


class Dashboard_Admin_Page:
    logo_xpath = "//img[@class='brand-image-xl logo-xl']"
    dashboard_txt_xpath = "//h1[normalize-space()='Dashboard']"
    dashboard_username_xpath = "(//li[@class='nav-item'])[3]"
    link_customer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menu_option_xpath = "//li[@class='nav-item']//p[normalize-space(text())='Customers']"

    def __init__(self, driver):
        self.driver = driver

    def logo_display(self):
        self.driver.find_element(By.XPATH, self.logo_xpath)

    def dashboard_text_visible(self):
        error_element = self.driver.find_element(By.XPATH, self.dashboard_txt_xpath)
        # self.driver.find_element(By.XPATH, self.dashboard_txt_xpath)
        return error_element

    def dashboard_username_visible(self):
        self.driver.find_element(By.XPATH, self.dashboard_username_xpath)

    def click_customers_menu(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_xpath).click()

    def click_customers_menu_option(self):
        self.driver.find_element(By.XPATH, self.link_customer_menu_option_xpath).click()
