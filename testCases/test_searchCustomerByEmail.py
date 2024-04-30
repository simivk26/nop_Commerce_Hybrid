import time

import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer

class Test_004_SearchCustomerByEmail:
    baseURL=ReadConfig.getApplicstionURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self,setup):
        self.logger.info("***************Test_004_Search Customer By Email*********************")
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
        addcus.clickON_Sub_CustomerMenu()

        self.logger.info("***************Searching Customer By Email*********************")
        searchcus=SearchCustomer(self.driver)
        searchcus.setEmail("brenda_lindgren@nopCommerce.com")
        searchcus.clickOnSearch()
        time.sleep(2)
        status=searchcus.searchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        assert True==status
        self.logger.info("***************Test_004_Search Customer By Email Completed*********************")
        self.driver.close()


