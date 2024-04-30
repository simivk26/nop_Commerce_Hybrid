# Common things for all tc's are here
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        serv = Service(r"C:\Drivers\chrome-win64\chrome-win64\chromedriver.exe")
        preference = {"download.default_directory": r"C:\Users\simiv\PycharmProjects\nop_Commerce_Hybrid\Download"}
        ops = webdriver.ChromeOptions()
        ops.add_experimental_option("prefs", preference)
        driver = webdriver.Chrome(service=serv,options=ops)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#########PyTest HTML Reports################
# It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Tester": "Simi",
        "Project Name": "Nop Commerce",
        'Module Name' : 'Customer'
    }

    # It is hook for delete/Modify environment info to HTML Reports
    @pytest.mark.optionalhook
    def pytest_metadata(metadata):
        metadata.pop('JAVA_HOME', 'None')
        metadata.pop('Plugins', 'None')
