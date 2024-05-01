import time

import pytest

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.ExportToExcelPage import ExportToExcel


class Test_006_ExportToExcelAllFound:
    baseUrL = ReadConfig.getApplicstionURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_exportToExcelAllFound(self, setup):
        self.logger.info("***************Test_006_Export To Excel All Found*********************")
        self.driver = setup
        self.driver.get(self.baseUrL)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("***************Login Successful*********************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickONCustomerMenu()
        time.sleep(2)
        self.addcust.clickON_Sub_CustomerMenu()

        self.logger.info("***************Starting Export ToExcel All Found*********************")
        self.exptoxl = ExportToExcel(self.driver)
        self.exptoxl.clickOnExport()
        self.exptoxl.clickOnExportToExcelAllFound()
        time.sleep(3)
        self.logger.info("***************Test_006_Export To Excel All Found Completed*********************")
        self.driver.close()
