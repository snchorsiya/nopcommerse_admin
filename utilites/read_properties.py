import configparser

config = configparser.RawConfigParser()
# config.read(".//Configuration//config.ini")
config.read("D://AutomationLearning//PythonAutomation//nopcommerce//Configurations//config.ini")


class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', 'admin_page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('admin login info', 'invalid_password')
        return invalid_password
