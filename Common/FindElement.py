# -*- coding: utf-8 -*-
from selenium import webdriver


class FindElement:
    # def GetElement(self,by='id',name=''):

    def FindElementById(self,driver,id):
        try:
            element=driver.find_element_by_id(id);
            return element;
        except ValueError:
            print('Id is null');

    def FindElementsById(self,driver,id):
        try:
            element=driver.find_elements_by_id(id);
            return element;
        except ValueError:
            print('Id is null');

    def FindElementByClass(self,driver,className):
        try:
            element=driver.find_element_by_class_name(className);
            return element;
        except ValueError:
            print('class name is null');

    def FindElementsByClass(self,driver,className):
        try:
            element=driver.find_elements_by_class_name(className);
            return element;
        except ValueError:
            print('class name is null');

    def FindElementByName(self,driver,name):
        try:
            element=driver.find_element_by_name(name);
            return element;
        except ValueError:
            print('class name is null');

    def FindElementsByName(self,driver,name):
        try:
            element = driver.find_elements_by_name(name);
            return element;
        except ValueError:
            print('class name is null');

    def FindElementByXPath(self,driver,xpath):
        try:
            element = driver.find_element_by_xpath(xpath);
            return element;
        except ValueError:
            print('class name is null');

    def FindElementsByXPath(self,driver,xpath):
        try:
            element = driver.find_elements_by_xpath(xpath);
            return element;
        except ValueError:
            print('class name is null');


