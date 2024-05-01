import time

import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer

class Test_005_SearchCustomerByName:
    baseURL=ReadConfig.getApplicstionURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByName(self,setup):
        self.logger.info("***************Test_005_Search Customer By Name*********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("***************Login Successful*********************")

        addcus=AddCustomer(self.driver)
        addcus.clickONCustomerMenu()
        time.sleep(2)
        addcus.clickON_Sub_CustomerMenu()

        self.logger.info("***************Searching Customer By Name*********************")
        searchcus=SearchCustomer(self.driver)
        searchcus.setFirstName("John")
        searchcus.setLastName("Smith")
        searchcus.clickOnSearch()
        time.sleep(2)
        status=searchcus.searchCustomerByName("John Smith")
        assert True==status
        self.logger.info("***************Test_005_Search Customer By Name Completed*********************")
        self.driver.close()