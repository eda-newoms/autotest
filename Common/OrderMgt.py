#!/usr/bin/python
# -*- coding: utf-8 -*-

import PageObject.OrderInfo;
from selenium.webdriver.common.keys import Keys
from time import sleep;
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 创建订单
def CreateOrder(driver,skuName):
    #TODO: 清除chrome 浏览器的缓存
    #BLOCK: 这个内嵌在setting html 中，需要再找方法定位，没办法直接用ID查找
    # driver.get('chrome://settings/clearBrowserData'); #clear browser data
    # driver.implicitly_wait(3);
    # clear= driver.find_element_by_id('clearBrowsingDataConfirm');
    # clear.click();


    #create one order
    driver.find_element_by_link_text('订单管理').click();
    driver.implicitly_wait(5);
    driver.find_element_by_xpath('//button[text="添加"]').click();
    driver.implicitly_wait(5);
    order = PageObject.OrderInfo.OrderInfo();
    print('开始新建订单，销售平台订单号: ',order.channelOrderId);

    # driver.find_element_by_name('channelId').click();
    driver.find_element_by_xpath('//select[@name="channelId"]/option[2]').click();
    driver.find_element_by_name('channelOrderId').send_keys(order.channelOrderId);
    driver.find_element_by_name('//select[@name="warehouseId"]/option[text="Los Angeles Warehouse"]').click();#Los Angeles Warehouse

    driver.find_element_by_xpath('//div[@class="ngui-auto-complete"]//ul//li[1]').click();#$('div.ngui-auto-complete ul li')



# 查询特定产品
def findProd(driver,skuName):
    print("开始查询指定ｓｋｕ："+skuName)
    driver.find_element_by_link_text('产品管理').click();
    driver.find_element_by_link_text('产品列表').click();
    driver.implicitly_wait(5);
    driver.find_element_by_name('searchWords').send_keys(skuName,Keys.ENTER);
    tr = driver.find_elements_by_xpath('//eda-table/div/table/tbody/tr');
    return tr;

# 关联产品
def matchProd(driver,skuName):
    print("开始关联产品ｓｋｕ: "+skuName);
    driver.find_element_by_link_text('产品管理').click();
    driver.find_element_by_link_text('关联管理').click();
    sleep(3);
    # driver.find_element_by_xpath('//productrelated[.//button[text()="导出"]]').click();
    # driver.find_element_by_xpath('//productrelated/div/div[2]/div/button').click();

    addBtn = driver.find_element_by_xpath('//productrelated/div/div[2]/div/div/button');
    # addLink = driver.find_element_by_class_name('bluepop-item');
    print(addBtn);
    action =ActionChains(driver);
    action.move_to_element(addBtn).send_keys(Keys.DOWN).perform();
    # TODO: 没找到单个添加关联ｓｋｕ的控件
    action.click(driver.find_element_by_class_name('bluepop-item')).perform();
    driver.implicitly_wait(5);

    channelSku = driver.find_element_by_name('channelSku');
    try:
        WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(channelSku));
        channelSku.send_keys(skuName);
        driver.find_element_by_xpath('//select[name="channelAccountId"]/option[1]').click();
        driver.find_element_by_name('channelAccountId').send_keys(Keys.TAB,Keys.TAB,skuName);
        driver.find_element_by_xpath('//button[text()="保存"]')
    finally:
        print("Failed!未找到关联产品弹框！")







