import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicstionURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_HomePageTitle(self, setup):
        self.logger.info("***************Test_001_Login*********************")
        self.logger.info("***************Verifying Home Page Title*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("***************Home Page Title Testcase Passed*********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("***************Home Page Title Testcase Failed*********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("***************Test_001_Login*********************")
        self.logger.info("***************Verifying test_Login*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
            self.logger.info("***************Login Testcase Passed*********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("***************Login Testcase Failed*********************")
            assert False
