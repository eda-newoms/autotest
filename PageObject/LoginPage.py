import  selenium;

class loginElements():
    def login(self,page):
        print('hello')
        userNameInput= page.find_element_by_id('username');
        passwordInput=page.find_element_by_id('password');
        loginBtn=page.find_element_by_id('loginname');
