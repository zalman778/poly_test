# coding=utf-8_sig
#Basic Tests List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#for session
import time, os, unittest, re, sys, pol_data, datetime

#temporary
#pol_data.DataBase_added_grantbox = 'BOX_2015_7_16-15_9_12'

#Testing NewGrantZc formand buttons

#func filling form on grant zc
def fill_form_ia(self):
	driver = self.driver
	driver.get(self.base_url + "/grant/request")
	driver.find_element_by_id("id_message").clear()
	driver.find_element_by_id("id_message").send_keys("some random text")
	driver.find_element_by_id("id_site_url").clear()
	driver.find_element_by_id("id_site_url").send_keys("http://io.io")
	driver.find_element_by_name("create").click()
	##table[@id='conf-list']//tr @data-href?



#ja - making 3 applications, and saving them into pol_data
def test_ia(self):
	atm_error = False
	print "\nBlock 18:"
	driver = self.driver
	pol_data.login_form_logout(self)
	pol_data.login_form_enter(self, 3)
	for ix in range(0, 3):
		fill_form_ia(self)
		pol_data.DataBase_added_grant_zc.append(driver.current_url)
	#driver.find_element_by_xpath("")

#this one is crashing
#@unittest.skip("spec")
def test_ib(self):
	driver = self.driver
	pol_data.login_form_logout(self)
	pol_data.login_form_enter(self, 1)
	driver.get(pol_data.DataBase_added_grant_zc[0])
	driver.find_element_by_name("reject").click()
	try: self.assertEqual(u"Отклонено", \
			driver.find_element_by_xpath(u"//span[@class='label label-danger']").text)
	except AssertionError as e: self.verificationErrors.append(str(e))

def test_ic(self):
	driver = self.driver
	print '\n'
	for i in pol_data.DataBase_added_grant_zc:
		print i, '\n'
	pol_data.login_form_logout(self)
	pol_data.login_form_enter(self, 1)
	driver.get(pol_data.DataBase_added_grant_zc[1])
	driver.find_element_by_name("create").click()
	driver.find_element_by_id("id_container_0").clear()
	driver.find_element_by_id("id_container_0").send_keys("con")
	driver.find_element_by_css_selector("span.hilight").click()
	driver.find_element_by_xpath(u"//input[@value=\"Выбрать\"]").click()

def test_id(self):
	driver = self.driver
	driver.get(pol_data.DataBase_added_grant_zc[2])
	driver.find_element_by_name("create").click()
	driver.find_element_by_id("id_container_0").clear()
	driver.find_element_by_id("id_container_0").send_keys(pol_data.DataBase_added_grantbox)
	driver.find_element_by_css_selector("span.hilight").click()
	driver.find_element_by_xpath(u"//input[@value=\"Выбрать\"]").click()
	try: self.assertEqual(driver.title, "Рабочий офис - Создание конкурса или гранта")
	except AssertionError as e: self.verificationErrors.append(str(e))


#@unittest.skip("spec")
def test_ie(self):
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












