import time

from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


class AddCustomer:
    lnkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_submenu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    chkTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    txtNewsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    lstitemYourStoreName_xpath = "//li[normalize-space()='Your store name']"
    lstitem_TestStore2_xpath = "//li[normalize-space()='Test store 2']"
    txtCustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemForumModerators_xpath = "//li[normalize-space()='Forum Moderators']"
    lstitemGuests_xpath = "//li[normalize-space()='Guests']"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpMngOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminComment_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    # Action methods
    def clickONCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_menu_xpath).click()

    def clickON_Sub_CustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomer_submenu_xpath).click()

    def clickONAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(companyName)

    def setTaxExempt(self):
        self.driver.find_element(By.XPATH, self.chkTaxExempt_xpath).click()

    def setNewsletter(self, storeName):
        self.driver.find_element(By.XPATH, self.txtNewsletter_xpath).click()
        time.sleep(2)
        if storeName == 'Your store name':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemYourStoreName_xpath)
        elif storeName == 'Test store 2':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitem_TestStore2_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemYourStoreName_xpath)
        time.sleep(2)
        self.listitem.click()

    def setCustomerRole(self, role):
        self.listitem = self.driver.find_element(By.XPATH, self.txtCustomerRoles_xpath).click()
        if role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Forum Moderators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemForumModerators_xpath)
        elif role == 'Guests':
            self.driver.find_element(By.XPATH,
                                     "//ul[@id='SelectedCustomerRoleIds_taglist']//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(2)
        self.listitem.click()

    def setManagerOfVendor(self, value):
        time.sleep(2)
        drp = Select(self.driver.find_element(By.XPATH, self.drpMngOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminComments(self, comment):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
