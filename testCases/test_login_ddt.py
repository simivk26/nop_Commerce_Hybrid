import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicstionURL()
    path=".//TestData//TestData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_Login_ddt(self, setup):
        self.logger.info("******************Test_002_DDT_Login Started********************")
        self.logger.info("***************Verifying test Login DDT*********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        self.row=ExcelUtils.getRowCount(self.path,'Hybrid_TestData')
        print("Number of Rows: ",self.row)
        status_lst=[]  #Empty list
        for r in range(2,self.row+1):
            self.username=ExcelUtils.readData(self.path,'Hybrid_TestData',r,1)
            self.password=ExcelUtils.readData(self.path,'Hybrid_TestData',r,2)
            self.exp=ExcelUtils.readData(self.path,'Hybrid_TestData',r,3)
            lp.setUserName(self.username)
            lp.setPassword(self.password)
            lp.clickLogin()
            act_title = self.driver.title

            if act_title == 'Dashboard / nopCommerce administration':
                if self.exp=='Pass':
                    self.logger.info("****************Passed**************")
                    status_lst.append('Pass')
                    lp.clickLogout()
                elif self.exp=='Fail':
                    self.logger.info("****************Failed**************")
                    status_lst.append('Fail')
                    lp.clickLogout()
            else:
                if self.exp=='Fail':
                    self.logger.info("****************Passed**************")
                    status_lst.append('Pass')
                elif self.exp=='Pass':
                    self.logger.info("****************Failed**************")
                    status_lst.append('Fail')
        if 'Fail' not in status_lst:
            self.logger.info("****************DDT_Login Test Passed**************")
            self.driver.close()
            assert True
        else:
            self.logger.info("****************DDT_Login Test Failed**************")
            self.driver.close()
            assert False
        self.logger.info("****************Test_002_DDT_Login Completed**************")

