# coding=utf-8_sig
#OIS Appl Tests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#for session
import time, os, unittest, time, re, sys, random
from pol_data import *

gl_curr_url = ""

#---------------Some additional functions----------------------
#function, which will complete FORM of making ticket for OIS
def fill_form_141(self, run_cnt):
    driver.get(self.base_url + "/patent/patent/")
    driver.find_element_by_id("id_app_num").clear()
    driver.find_element_by_id("id_app_num").send_keys(str(random.randint(1000000,3000000)))
    driver.find_element_by_id("id_pend_num_0").clear()
    driver.find_element_by_id("id_pend_num_0").send_keys(pol_data.DataBase_added_ois_nums[len(DataBase_added_ois_nums)-run_cnt])
    driver.find_element_by_css_selector("span.hilight").click()
    driver.find_element_by_css_selector("span.glyphicon-calendar.glyphicon").click()
    driver.find_element_by_xpath("//table[@class='table-condensed']//tr[2]/td[5]").click()
    driver.find_element_by_css_selector("#id_expiration_date_picker > span.input-group-addon > span.glyphicon-calendar.glyphicon").click()
    driver.find_element_by_xpath("(//body//div[@class='bootstrap-datetimepicker-widget dropdown-menu'])[3]//table/tbody/tr[4]/td[5]").click()
    driver.find_element_by_name("submit").click()
    driver.find_element_by_name("verify").click()

#---------------Module Tests----------------------
#test 1.4.0
@unittest.skip("spec")
def test_d0(self):
    driver = self.driver
    print "\nBlock 14:"
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 3)
    driver.get(self.base_url + "/patent/patents/my/")
    driver.find_element_by_link_text(u"Научная работа").click()
    driver.find_element_by_link_text(u"Каталог ОИС").click()
    driver.find_element_by_link_text(u"Добавить ОИС").click()
    try: self.assertEqual(u"Рабочий офис — ОИС", driver.title)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.4.1
@unittest.skip("spec")
def test_d1(self):
    driver = self.driver
    global gl_curr_url
    fill_form_141(0)
    gl_curr_url = driver.current_url
    try: self.assertEqual(u"Находится на верификации", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.4.2 
@unittest.skip("spec")
def test_d2(self):
    driver = self.driver
    global gl_curr_url
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 2)
    driver.get(gl_curr_url)
    driver.find_element_by_name("reject").click()
    try: self.assertEqual(u"Отклонено", \
            driver.find_element_by_xpath(u"//span[@class='label label-danger']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.4.3
@unittest.skip("spec")
def test_d3(self):
    driver = self.driver
    global gl_curr_url
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 3)
    fill_form_141(0)
    gl_curr_url = driver.current_url
    try: self.assertEqual(u"Находится на верификации", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.4.4
@unittest.skip("spec")
def test_d4(self):
    driver = self.driver
    driver.find_element_by_name("verify").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.4.5
#@unittest.skip("spec")
def test_d5(self):
    driver = self.driver
    #TODO: implement some chnages
    driver.find_element_by_name("change").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
'''
#test 1.4.5
@unittest.skip("spec")
def test_p4(self):
    driver = self.driver
    driver.find_element_by_id("id_name").clear()
    driver.find_element_by_id("id_name").send_keys("")
    driver.find_element_by_id("id_name").clear()
    driver.find_element_by_id("id_name").send_keys(pol_data.db_fake_item_names())
    driver.find_element_by_id("id_content").clear()
    driver.find_element_by_id("id_content").send_keys(u"Новый комментарий А.")
    Select(driver.find_element_by_id("id_pat_type")).select_by_visible_text(u"товарный знак")
    driver.find_element_by_name("change").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))
'''

