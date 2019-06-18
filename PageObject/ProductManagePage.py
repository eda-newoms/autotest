
from selenium import webdriver

import Common.FindElement
import selenium;

class ProdManagePage:
    def createNewProd(driver):
        # common = Common.FindElement.FindElement();
        # navigateLink=common.FindElementsByClass(driver, 'nav-link')

        navigateLink=driver.find_elements_by_class_name('nav-link');
        for i in navigateLink:
            if(i.text=="产品管理"):
                i.click();
                driver.find_element_by_id('main-template');
                addProdBtn = driver.find_element_by_xpath("//div[class='mgb20']/button[contains(text(),'添加')]");
                addProdBtn.click();
                print("test");

        print("createNewProd");




