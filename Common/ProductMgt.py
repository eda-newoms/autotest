#!/usr/bin/python
# -*- coding: utf-8 -*-

import PageObject.ProdSku;
from selenium.webdriver.common.keys import Keys
from time import sleep;
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 新建产品
def productMgt(driver):
    #TODO: 清除chrome 浏览器的缓存
    #BLOCK: 这个内嵌在setting html 中，需要再找方法定位，没办法直接用ID查找
    # driver.get('chrome://settings/clearBrowserData'); #clear browser data
    # driver.implicitly_wait(3);
    # clear= driver.find_element_by_id('clearBrowsingDataConfirm');
    # clear.click();

    #create one product
    driver.find_element_by_link_text('产品管理').click();
    driver.implicitly_wait(5);
    driver.find_element_by_link_text('单个添加').click();
    driver.implicitly_wait(5);
    sku = PageObject.ProdSku.Sku();
    print('开始新建sku: ',sku.skuName);

    # 填写基础信息
    driver.find_element_by_name('productSku').send_keys(sku.skuName);
    driver.find_element_by_name('productSku').send_keys(Keys.TAB,sku.skuProdNameCn);
    driver.find_element_by_name('productNameEn').send_keys(sku.skuProdNameEn);
    driver.find_element_by_name('salesLink').send_keys(sku.skuLink);
    driver.find_element_by_xpath("//div[@id='collapseManual1']//button").click();

    # 计费相关信息
    driver.find_element_by_name('clengthCm').send_keys('1');
    driver.find_element_by_name('cwidthCm').send_keys('1');
    driver.find_element_by_name('cheightCm').send_keys('1');
    driver.find_element_by_name('cweightKg').send_keys('1');
    driver.find_element_by_name('exportPrice').send_keys('1');

    driver.find_element_by_xpath("//*[@id='collapseManual2']/div[1]/form/table[2]/tbody/tr/td[1]/div").click();
    driver.find_element_by_link_text('美国').click();
    driver.find_element_by_xpath('//*[@id="collapseManual2"]/div[1]/form/table[2]/tbody/tr/td[2]/div/input').send_keys('1');
    driver.find_element_by_xpath('//*[@id="collapseManual2"]/div[1]/form/table[2]/tbody/tr/td[3]/div/select/option[2]').click();
    driver.find_element_by_xpath('//div[@id="collapseManual2"]//button[2]').click();

    # 其它信息
    driver.find_element_by_xpath('//div[@id="collapseManual2"]//button[3]').click();
    return sku.skuName;


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

def SearchSkuStock(driver):
    driver.implicitly_wait(5);
    driver.find_element_by_link_text('易云仓').click();#展开
    sleep(3)
    # driver.find_element_by_link_text('展开').click();
    # # driver.find_element_by_xpath('//a/span[text()="展开"]').click();
    # driver.find_element_by_id('salableQuantityGtZero').click();
    # driver.find_element_by_xpath('//button/i[text()="查询"]').click();
    # driver.find_element_by_xpath('//i[@class="fa fa-search"][1]').click();
    sku = driver.find_element_by_xpath('//div[@class="edatable"][1]//table[1]//tr[1]//td[1]').get_attribute('textContent');
    print(sku);
    return sku;






