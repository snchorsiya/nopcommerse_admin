import os.path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            print(f"Screenshot captured: {file_name}")
            if file_name:
                html = '<div><img src=".//ScreenShots//%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    try:
        screenshot_path = f".//ScreenShots//{name}"
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.get_screenshot_as_file(screenshot_path)
        print("Current working directory:", os.getcwd())
    except Exception as e:
        print(f"An error occurred while capturing screenshot: {e}")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser: chrome or firefox or edge")


def pytest_html_report_title(report):
    report.title = "NopCommerce Report"


@pytest.fixture()
def setup(request):
    global driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        chr_option = Options()
        chr_option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chr_option)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
