# -*- coding: UTF-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import Common.Login
from time import sleep;
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class RMA:
    def openRmaPage(self,driver):
        # １．登录首页
        # Common.Login.Login(driver);
        # driver.implicitly_wait(3);

        # 2.打开入库单界面
        sleep(3);
        driver.find_element_by_link_text('易云仓').click();
        driver.find_element_by_link_text('入库管理').click();
        # driver.find_element_by_link_text('入库单管理').click();
        sleep(10);

    #type＝ Standrd 标准；FT_EXAMONLY　自发国内;NO_FT 自发国外
    def createRMA(self,driver,*type):
        driver.find_element_by_link_text('添加入库单').click();
        option = driver.find_element_by_name('orderType');
        #３．选择入库单服务内容
        if(type=='自发国内'):
            Select(option).select_by_value('FT_EXAMONLY').click();
            # driver.find_element_by_xpath('//select[@name="orderType"/option[text()="自发国内验服务"]').click();


        elif(type == '自发国外' ):
            # driver.find_element_by_xpath('//select[@name="orderType"/option[text()="自发海外验服务"]').click();
            Select(option).select_by_value('NO_FT').click();

        #１．填写入库单内容
        firstWarehouseCode = driver.find_element_by_xpath('//eda-detailbox[1]/section/div[2]/div/div[1]/div/select');
        Select(firstWarehouseCode).select_by_value('CNSZ');

        # eda - detailbox[1] / section / div[2] / div / div[2] / div / select
        warehouseCode = driver.find_element_by_xpath('//eda-detailbox[1]/section/div[2]/div/div[2]/div/select');
        Select(warehouseCode).select_by_value('USLA');

        driver.find_element_by_xpath('//select[@name="courierAccountMgmtId"]/option[@value="2000669"]').click();

        driver.find_element_by_xpath('//select[@name="deliveryType"]//option[@value="customersend"]').click();

        driver.find_element_by_name('homeDeliveryExpectedDate').click();
        driver.find_element_by_css_selector('td.today').click();

        driver.find_element_by_xpath('//select[@name="exCustoms"]//option[@value="NORMALTRADE"]').click();

        driver.find_element_by_xpath('//select[@name="inCustoms"]//option[@value="EDADO"]').click();

        driver.find_element_by_xpath('//button[text()="添加箱号"]').click();
        sleep(5);
        # 　２．填写箱号信息
        driver.find_element_by_name('sellerCartonCode').send_keys("1");
        driver.find_element_by_name('lengthCm').send_keys('1');
        driver.find_element_by_name('widthCm').send_keys('1');
        driver.find_element_by_name('heightCm').send_keys('1', Keys.TAB, "tes");

        # 3. 输入ｓｋｕ并保存箱号
        sleep(5);
        driver.find_element_by_xpath('//div[@class="ngui-auto-complete"]//ul//li[1]').click();
        driver.find_element_by_xpath('//td//input').send_keys('1');
        driver.find_element_by_xpath('//inboundcreate/eda-modal[3]/div/div/div/div[3]/button[1]').click();
        sleep(5)

        # 3.直接入库单，确定发布
        driver.find_element_by_xpath('//button[text()="直接发布"]').click();
        sleep(5);
        rev= driver.find_element_by_xpath('//div[@class="form-group col-md-4 col-sm-6"][1]//span').is_displayed();
        revText = driver.find_element_by_xpath('//div[@class="form-group col-md-4 col-sm-6"][1]//span').get_attribute('textContent');
        print(rev,revText)

        # sleep(5);
        driver.find_element_by_xpath('//div[@class="col-sm-4"]/button[1]').click();
        print("成功新建并发布入库单：" + revText);
        return revText;


    def searchRev(self,driver,skuName):
        # １.打开入库单界面
        sleep(3);
        driver.find_element_by_partial_link_text('易云仓').click();
        driver.find_element_by_link_text('入库管理').click();
        driver.find_element_by_link_text('入库单管理').click();
        driver.find_element_by_name('businessNum').send_keys(skuName,Keys.ENTER);
        sleep(3);
        result = driver.find_elements_by_link_text('全部(1)');
        return len(result)>0;



















    # def createExamonlyRMA(self,d):


