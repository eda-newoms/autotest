#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import ChooseEnv;
import PageObject.LoginPage;

def Login(driver):
    #TODO: 清除chrome 浏览器的缓存
    #BLOCK: 这个内嵌在setting html 中，需要再找方法定位，没办法直接用ID查找
    # driver.get('chrome://settings/clearBrowserData'); #clear browser data
    # driver.implicitly_wait(3);
    # clear= driver.find_element_by_id('clearBrowsingDataConfirm');
    # clear.click();
    url = ChooseEnv.url;
    user = ChooseEnv.user;
    pwd = ChooseEnv.pwd;

    driver.get(url+'newoms');
    driver.maximize_window();
    driver.implicitly_wait(3);

    frame=driver.find_element_by_class_name('frmHeight');
    driver.switch_to.frame(frame);
    driver.find_element_by_id('username').send_keys(user);
    driver.find_element_by_id('password').send_keys(pwd);
    driver.find_element_by_id('loginname').click();
    # page = PageObject.LoginPage.loginElements();
    # loginPage = page.login(driver);
    # usr=page.login(driver).userNameInput;
    #
    #
    # loginPage.userNameInput.send_keys(user);
    # loginPage.passwordInput.send_keys(pwd);
    # loginPage.loginBtn.click();


    driver.implicitly_wait(20);

    print("\n")
    print('Log in newoms successfully!')

    # driver.close();