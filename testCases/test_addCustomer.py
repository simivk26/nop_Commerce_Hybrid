import random
import string

import pytest
from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
class Test_003_AddCustomer:
    baseUrL= ReadConfig.getApplicstionURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("***************Test_003_Add Customer*********************")
        self.driver=setup
        self.driver.get(self.baseUrL)
        self.driver.maximize_window()
        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("***************Login Successful*********************")

        self.logger.info("***************Starting Add Customer Test*********************")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickONCustomerMenu()
        self.addcust.clickON_Sub_CustomerMenu()
        self.addcust.clickONAddNew()

        self.logger.info("***************Providing Customer Details*********************")
        self.email=random_generator()+'@gmail.com'
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName(random_generator())
        self.addcust.setLastName(random_generator())
        self.addcust.setGender('Female')
        self.addcust.setDOB('5/03/1992')
        self.addcust.setCompanyName('Dell')
        self.addcust.setTaxExempt()
        self.addcust.setNewsletter('Your store name')
        self.addcust.setCustomerRole('Vendors')
        self.addcust.setManagerOfVendor('Vendor 1')
        self.addcust.setAdminComments('This is for testing....')
        self.addcust.clickOnSave()
        self.logger.info("***************Saving Customer Details*********************")

        self.logger.info("***************Validate Add Customer Details*********************")

        self.msg=self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("***************Add Customer Passed*********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_AddCustomer.png")
            self.logger.info("***************Add Customer Failed*********************")
            assert False
        self.driver.close()
        self.logger.info("***************Test_003_Add Customer Completed*********************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
