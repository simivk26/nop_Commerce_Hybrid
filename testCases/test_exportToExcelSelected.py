import random
import time

import pytest
from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.ExportToExcelPage import ExportToExcel
from pageObjects.SearchCustomerPage import SearchCustomer


class Test_006_ExportToExcelAllFound:
    baseUrL = ReadConfig.getApplicstionURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_exportToExcelAllFound(self, setup):
        self.logger.info("***************Test_007_Export To Excel Selected*********************")
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
        self.logger.info("***************Starting Export To Excel Selected*********************")
        self.exptoxl = ExportToExcel(self.driver)

        sr = SearchCustomer(self.driver)
        self.rows = sr.getNoOfRows()
        num = random_generator(self)
        time.sleep(2)
        print("random num: ", num)
        print("rows: ", self.rows)
        for i in range(1, self.rows):
            if i == num:
                self.driver.find_element(By.XPATH, "//tbody/tr[" + str(num) + "]/td[1]").click()
                break
        self.exptoxl.clickOnExport()
        self.exptoxl.clickOnExportToExcelSelected()
        time.sleep(3)
        self.logger.info("***************Test_007_Export To Excel Selected Completed*********************")
        self.driver.close()


def random_generator(self):
    return random.randrange(1, self.rows + 1)
