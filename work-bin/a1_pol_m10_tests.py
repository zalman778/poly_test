# coding=utf-8_sig
#Basic Tests List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#for session
import time, os, unittest, re, sys, pol_data



#1.0.1
#title test
@unittest.skip("spec")
def test_a0(self):                
    driver = self.driver
    driver.get(self.base_url + "/auth/login/")
    try: self.assertEqual(u"Рабочий офис — Вход", driver.title)
    except AssertionError as e: self.verificationErrors.append(str(e))

#1.0.2
#Failed login test
@unittest.skip("spec")
def test_a1(self):        
    driver = self.driver
    driver.get(self.base_url)
    driver.find_element_by_id("id_login").clear()
    driver.find_element_by_id("id_login").send_keys(pol_data.b_login)
    driver.find_element_by_id("id_password").clear()
    driver.find_element_by_id("id_password").send_keys(pol_data.b_pass)
    driver.find_element_by_xpath(u"//input[@class='btn btn-primary btn-lg btn-block']").click()          
    try: self.assertEqual(u"×\nClose\nНеверное имя пользователя или пароль", 
        unicode(driver.find_element_by_xpath("//div[@class='alert alert-danger alert-dismissible']").text))
    except AssertionError as e: self.verificationErrors.append(str(e))

#1.0.3
#Right login test
#@unittest.skip("spec")
def test_a2(self):
    driver = self.driver
    t_c = False
    driver.get(self.base_url + "/auth/login/")
    pol_data.login_form_enter(self, 3)
    if driver.find_element_by_xpath("//li[@class='dropdown']/a[@class='dropdown-toggle']").text != "":
        t_c = True
    try: self.assertEqual(t_c, True)
    except AssertionError as e: self.verificationErrors.append(str(e))
