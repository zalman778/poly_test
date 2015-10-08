# coding=utf-8_sig
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#for session
import time, os, unittest, time, re, sys, pol_data, datetime
temp_var_1 = ''

#Tessting box creation

#1.0.1
#@unittest.skip("spec")
def test_ha(self):                
	driver = self.driver
	print "\nBlock 17:"
	driver.get(self.base_url + "/grant/")
	try: self.assertEqual(u"Рабочий офис — Конкурсы и гранты", driver.title)
	except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_hb(self):                
	driver = self.driver
	global temp_var_1
	#pol_data.login_form_logout(self)
	#pol_data.login_form_enter(self, 3)
	driver.get(self.base_url + "/grant/container/new")
	temp_var_1 = str(pol_data.currDateGen())
	pol_data.DataBase_added_grantbox = "BOX_"+temp_var_1

	driver.find_element_by_id("id_name").clear()
	driver.find_element_by_id("id_name").send_keys("BOX_"+temp_var_1)

	driver.find_element_by_id("id_short_name").clear()
	driver.find_element_by_id("id_short_name").send_keys("box_"+temp_var_1)

	driver.find_element_by_id("id_grant_url").clear()
	driver.find_element_by_id("id_grant_url").send_keys("http://yandex.fi")

	driver.find_element_by_xpath(u"//input[@value='Создать']").click()
	
	try: self.assertNotEqual(driver.find_elements_by_xpath("//div[@id='grantTree']//*[contains(text(), 'BOX_"+temp_var_1+"')]"), None)
	except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_hc(self):
	driver = self.driver
	global temp_var_1
	print temp_var_1
	driver.get(self.base_url + "/grant/")
	driver.find_element_by_xpath(u"//*[contains(text(),\"BOX_"+temp_var_1+"\")]/..").click()
	driver.find_element_by_xpath(u"(//input[@value=\"Создать\"])[2]").click()
	

#@unittest.skip("spec")
def test_hd(self):
	driver = self.driver
	
	driver.find_element_by_id("id_name").clear()
	driver.find_element_by_id("id_name").send_keys("CONC_"+str(pol_data.currDateGen()))

	driver.find_element_by_id("id_short_name").clear()
	driver.find_element_by_id("id_short_name").send_keys("conc_"+str(pol_data.currDateGen()))

	driver.find_element_by_id("id_grant_url").clear()
	driver.find_element_by_id("id_grant_url").send_keys("http://yandex.fi")

	driver.find_element_by_id("id_max_funding").clear()
	driver.find_element_by_id("id_max_funding").send_keys("100500")

	driver.find_element_by_id("id_project_count").clear()
	driver.find_element_by_id("id_project_count").send_keys("5")

	driver.find_element_by_id("id_single_project_max_funding").clear()
	driver.find_element_by_id("id_single_project_max_funding").send_keys("100000")

	#changing date to hell
	time_mdl = datetime.datetime.now()
	time_cr = str(time_mdl.day)+"."+str(time_mdl.month)+"."+str(time_mdl.year-1)
	driver.find_element_by_id("id_date_start").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, \
		Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
	driver.find_element_by_id("id_date_start").send_keys(time_cr)
	#eoc

	time_mdl = datetime.datetime.now()
	time_cr = str(time_mdl.day)+"."+str(time_mdl.month)+"."+str(time_mdl.year+1)
	driver.find_element_by_id("id_date_end").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, \
		Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
	driver.find_element_by_id("id_date_end").send_keys(time_cr)


	time_mdl = datetime.datetime.now()
	time_cr = str(time_mdl.day)+"."+str(time_mdl.month)+"."+str(time_mdl.year)
	driver.find_element_by_id("id_app_date_start").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, \
		Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
	driver.find_element_by_id("id_app_date_start").send_keys(time_cr)


	time_mdl = datetime.datetime.now()
	time_cr = str(time_mdl.day)+"."+str(time_mdl.month)+"."+str(time_mdl.year+1)
	driver.find_element_by_id("id_app_date_end").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, \
		Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
	driver.find_element_by_id("id_app_date_end").send_keys(time_cr)

	driver.find_element_by_id("id_app_address").clear()
	driver.find_element_by_id("id_app_address").send_keys("spbdtu, 9c")

	driver.find_element_by_id("id_person_max_project_count").clear()
	driver.find_element_by_id("id_person_max_project_count").send_keys("5")

	driver.find_element_by_xpath(u"//input[@value='Создать']").click()



