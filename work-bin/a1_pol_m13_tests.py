# coding=utf-8_sig
#OIS Tests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#for session
import time, os, unittest, re, sys, pol_data

#Global vars
gl_curr_url = ''

#---------------Some additional functions----------------------
#function, which will complete FORM of making ticket for ZV.OIS
def fill_form_122(self, run_cnt):
    driver = self.driver
    driver.get(self.base_url + "/patent/pendpat/")
    driver.find_element_by_id("id_app_num").clear()
    driver.find_element_by_id("id_app_num").send_keys(pol_data.db_ois_num_gen())
    Select(driver.find_element_by_id("id_pat_type")).select_by_visible_text(u"ноу-хау")
    driver.find_element_by_css_selector("span.input-group-addon").click()
    driver.find_element_by_xpath("//table[@class='table-condensed']//tr[3]/td[5]").click()
    driver.find_element_by_id("id_name").clear()
    driver.find_element_by_id("id_name").send_keys(pol_data.db_fake_item_names())
    driver.find_element_by_link_text(u"Добавить правообладателя").click()
    driver.find_element_by_id("id_copyrighters-0-internal_copyrighter_0").clear()
    driver.find_element_by_id("id_copyrighters-0-internal_copyrighter_0").send_keys(pol_data.db_real_staff_gen())
    driver.find_element_by_css_selector("span.hilight").click()
    driver.find_element_by_link_text(u"Добавить правообладателя").click()
    Select(driver.find_element_by_id("id_copyrighters-1-copyrighter_type")).select_by_visible_text(u"организация")
    driver.find_element_by_id("id_copyrighters-1-organization_0").clear()
    driver.find_element_by_id("id_copyrighters-1-organization_0").send_keys(u"Спб")
    driver.find_element_by_css_selector("span.hilight").click()
    driver.find_element_by_link_text(u"Добавить автора").click()
    driver.find_element_by_id("id_authors-0-internal_author_0").clear()
    driver.find_element_by_id("id_authors-0-internal_author_0").send_keys(pol_data.db_real_staff_gen())
    driver.find_element_by_css_selector("span.hilight").click()
    driver.find_element_by_link_text(u"Добавить автора").click()
    Select(driver.find_element_by_id("id_authors-1-author_type")).select_by_visible_text(u"сотрудник другой организации")
    driver.find_element_by_id("id_authors-1-external_author").clear()
    driver.find_element_by_id("id_authors-1-external_author").send_keys(pol_data.db_fake_staff_gen())
    driver.find_element_by_id("id_authors-1-ea_organization_0").clear()
    driver.find_element_by_id("id_authors-1-ea_organization_0").send_keys(u"Спб")
    driver.find_element_by_css_selector("span.hilight").click()
    driver.find_element_by_name("submit").click()

#---------------Module Tests----------------------
#test 1.3.0
@unittest.skip("spec")
def test_c0(self):
    driver = self.driver
    print "\nBlock 13:"
    #driver.get(self.base_url + "/")
    driver.get(self.base_url + "/patent/patents/my/")
    driver.find_element_by_link_text(u"Научная работа").click()
    driver.find_element_by_link_text(u"Каталог заявок на ОИС").click()
    driver.find_element_by_link_text(u"Добавить заявку на ОИС").click()
    try: self.assertEqual(u"Рабочий офис — Заявка на ОИС", driver.title)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.3.1
#@unittest.skip("spec")
def test_c1(self):
    driver = self.driver
    print "\nBlock 13:"
    fill_form_122(self, 0)    
    global gl_curr_url
    gl_curr_url = driver.current_url
    try: self.assertEqual(u"Находится на верификации", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))


#test 1.3.2 - Crashing
#@unittest.skip("spec")
def test_c2(self):
    driver = self.driver
    global gl_curr_url
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 2)
    driver.get(gl_curr_url)
    driver.find_element_by_name("reject").click()
    try: self.assertEqual(u"Отклонена", \
            driver.find_element_by_xpath(u"//span[@class='label label-danger']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.3.3
#@unittest.skip("spec")
def test_c3(self):
    driver = self.driver
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 3)
    fill_form_122(self, 1)    
    global gl_curr_url
    gl_curr_url = driver.current_url
    try: self.assertEqual(u"Находится на верификации", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.3.4
#@unittest.skip("spec")
def test_c4(self):
    driver = self.driver
    global gl_curr_url
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 2)
    driver.get(gl_curr_url)
    driver.find_element_by_name("verify").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.3.5
#@unittest.skip("spec")
def test_c5(self):
    driver = self.driver
    #TODO: implement some chnages
    driver.find_element_by_name("change").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.3.6
#@unittest.skip("spec")
def test_c6(self):
    driver = self.driver
    driver.find_element_by_name("reject").click()
    try: self.assertEqual(u"Отклонена", \
            driver.find_element_by_xpath(u"//span[@class='label label-danger']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#test 1.3.7
#@unittest.skip("spec")
def test_c7(self):
    driver = self.driver
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 3)
    fill_form_122(self, 2)    
    global gl_curr_url
    gl_curr_url = driver.current_url
    try: self.assertEqual(u"Находится на верификации", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))


#test 1.3.8
#@unittest.skip("spec")
def test_c8(self):
    driver = self.driver
    global gl_curr_url
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 2)
    driver.get(gl_curr_url)
    driver.find_element_by_name("verify").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

