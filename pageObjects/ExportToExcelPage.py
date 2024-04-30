

from selenium.webdriver.common.by import By

class ExportToExcel:
    btnExport_xpath="//button[@class='btn btn-success dropdown-toggle']"
    btnExportToExcelAllFound_xpath="//button[normalize-space()='Export to Excel (all found)']"
    btnExportToExcelSelected_xpath="//button[@id='exportexcel-selected']"
    chkSelect2_xpath="//input[@value='130']"
    chkSelect4_xpath ="//input[@value='6']"

    #tableRows_xpath="//tbody/tr"
    #tableColumns_xpath="//div[@class='dataTables_scrollHeadInner']//tr/th"

    def __init__(self,driver):
        self.driver=driver

    def clickOnExport(self):
        self.driver.find_element(By.XPATH,self.btnExport_xpath).click()

    def clickOnExportToExcelAllFound(self):
        self.driver.find_element(By.XPATH, self.btnExportToExcelAllFound_xpath).click()

    def clickOnExportToExcelSelected(self):
        self.driver.find_element(By.XPATH, self.btnExportToExcelSelected_xpath).click()



