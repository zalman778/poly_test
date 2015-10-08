# coding=utf-8_sig
#Cond Appl Tests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#for session
import time, os, unittest, time, re, sys, pol_data, datetime

#temp added
#pol_data.DataBase_added_confs_names = [
#u"qqq, '2014-11-24", u"qqq, '2014-11-25",u"qqq, '2015-05-19",u"qqq, '2015-07-09", u"qqq, '2014-11-28",u"qqq, '2015-07-08"]
#heh


def fill_form_zcx(self, itx):
    #itx=ix+1
    driver = self.driver
    driver.get(self.base_url+"/conference/confpart")
    #driver.find_element_by_link_text(u"Добавить заявку на участие").click()
    driver.find_element_by_id("id_conference_0").clear()
    
    #searching exact conf by name and then by date
    driver.find_element_by_id("id_conference_0").send_keys(pol_data.DataBase_added_confs_names[len(pol_data.DataBase_added_confs_names)-1])
    driver.find_element_by_css_selector("span.hilight").click()
    #end of search 
    driver.find_element_by_name("select").click()
    #changing date to hell
    time_mdl = datetime.datetime.now()
    time_cr = str(time_mdl.day)+"."+str(time_mdl.month)+"."+str(time_mdl.year)
    driver.find_element_by_id("id_end_date").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, \
        Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
    driver.find_element_by_id("id_end_date").send_keys(time_cr)
    #eoc
    driver.find_element_by_name("submit").click()

#***********************
# Block 0
# Logging in as user
#***********************

#@unittest.skip("spec")
def test_ba(self):
    atm_error = False
    #print pol_data.DataBase_added_confs
    print "\nBlock 12:"
    driver = self.driver
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 3)
    for ix in range(1, 5):
        fill_form_zcx(self, ix)
        if driver.find_element_by_xpath(u"//span[@class='label label-warning']").text != u"Находится на верификации":
            atm_error = True
        pol_data.DataBase_added_confs_zc.append(driver.current_url)
    try: self.assertEqual(atm_error, False)
    except AssertionError as e: self.verificationErrors.append(str(e))

def test_bb(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-5])
    driver.find_element_by_link_text(u"Создать заявку").click()
    driver.find_element_by_name("submit").click()
    pol_data.DataBase_added_confs_zc.append(driver.current_url)
    try: self.assertEqual(driver.find_element_by_xpath(u"//span[@class='label label-warning']").text, u"Конференция еще не верифицирована")
    except AssertionError as e: self.verificationErrors.append(str(e))

#No such way U:accdup
def test_bc(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-5])
    driver.find_element_by_xpath("//div[@id='right_sidebar']/div/div").click()
    driver.find_element_by_id("id_conference_0").clear()
    driver.find_element_by_id("id_conference_0").send_keys("Qqq")
    driver.find_element_by_css_selector("span.hilight").click()
    driver.find_element_by_name("duplicate").click()

def test_bd(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-4])
    driver.find_element_by_link_text(u"Создать заявку").click()
    driver.find_element_by_name("submit").click()
    pol_data.DataBase_added_confs_zc.append(driver.current_url)
    #print "some info:"
    #print pol_data.DataBase_added_confs_zc
    try: self.assertEqual(driver.find_element_by_xpath(u"//span[@class='label label-warning']").text, u"Конференция еще не верифицирована")
    except AssertionError as e: self.verificationErrors.append(str(e))

#***********************
# Block 1
# Logging in as mod
#***********************

#@unittest.skip("spec")
def test_be(self):
    driver = self.driver
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 2)
    driver.get(pol_data.DataBase_added_confs_zc[len(pol_data.DataBase_added_confs_zc)-6])
    driver.find_element_by_name("reject").click()
    try: self.assertEqual(driver.find_element_by_xpath(u"//span[@class='label label-danger']").text, u"Отклонена верификатором")
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_bf(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs_zc[len(pol_data.DataBase_added_confs_zc)-5])
    driver.find_element_by_name("reject").click()
    try: self.assertEqual(driver.find_element_by_xpath(u"//span[@class='label label-danger']").text, u"Отклонена верификатором")
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_bg(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs_zc[len(pol_data.DataBase_added_confs_zc)-4])
    driver.find_element_by_name("save").click()
    try: self.assertEqual(driver.find_element_by_xpath(u"//span[@class='label label-warning']").text, u"Находится на верификации")
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_bh(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs_zc[len(pol_data.DataBase_added_confs_zc)-4])
    driver.find_element_by_name("content").send_keys("Comment_1")
    driver.find_element_by_name("change").click() 
    try: self.assertEqual(driver.find_element_by_xpath(u"//span[@class='label label-warning']").text, u"Отредактирована верификатором")
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_bi(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs_zc[len(pol_data.DataBase_added_confs_zc)-3])
    driver.find_element_by_name("content").send_keys("Comment_2")
    driver.find_element_by_name("change").click() 
    try: self.assertEqual(driver.find_element_by_xpath(u"//span[@class='label label-warning']").text, u"Отредактирована верификатором")
    except AssertionError as e: self.verificationErrors.append(str(e))

#cant be testes due to false way U:accdup
@unittest.skip("spec")
def test_bj(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs_zc[len(pol_data.DataBase_added_confs_zc)-5])
    #time.sleep(15)
    driver.find_element_by_name("verify").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

def test_bk(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-4])
    driver.find_element_by_name("verify").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#***********************
# Block 2
# Logging in as user
#***********************

#@unittest.skip("spec")
def test_bl(self):
    driver = self.driver
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 3)
    driver.get(pol_data.DataBase_added_confs_zc[len(pol_data.DataBase_added_confs_zc)-5])
    driver.find_element_by_name("change").click() 
    try: self.assertEqual(driver.find_element_by_xpath(u"//span[@class='label label-warning']").text, u"Находится на верификации")
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_bm(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs_zc[len(pol_data.DataBase_added_confs_zc)-4])
    driver.find_element_by_name("change").click() 
    try: self.assertEqual(driver.find_element_by_xpath(u"//span[@class='label label-warning']").text, u"Находится на верификации")
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_bn(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs_zc[len(pol_data.DataBase_added_confs_zc)-3])
    driver.find_element_by_name("change").click() 
    try: self.assertEqual(driver.find_element_by_xpath(u"//span[@class='label label-warning']").text, u"Находится на верификации")
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_bo(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs_zc[len(pol_data.DataBase_added_confs_zc)-1])
    time.sleep(5)

