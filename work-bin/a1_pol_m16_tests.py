# coding=utf-8_sig
#OIS Tests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#for session
import time, os, unittest, re, sys, pol_data, datetime

#Тестирование раздела Члены дисс. советов
#Добавление и верификация заявок
#Everuthing works from single user with all right: mpetrov
# - 1st one found with only 1 search result:
#Journal of the Irrigation and Drainage Division
#21st Century Music
#Others causes crash by get() methid returning more than 1 result.

#fa - chcking page title and availablity
@unittest.skip("spec")
def test_ga(self):
	driver = self.driver
	print "\nBlock 16:"
	driver.get(self.base_url + "/disscouncil/disscouncils/available/")
	try: self.assertEqual(u"Рабочий офис — Члены дисс. советов", driver.title)
	except AssertionError as e: self.verificationErrors.append(str(e))

#f1 - filling form func def fill_f_form(self, ix):
def fill_form_ga(self, ix):
	driver = self.driver
	
	driver.find_element_by_id("id_code").clear()
	driver.find_element_by_id("id_code").send_keys("code_"+pol_data.currDateGen())
	
	#selecting today as a start day
	time_mdl = datetime.datetime.now()
	time_cr = str(time_mdl.day)+"."+str(time_mdl.month)+"."+str(time_mdl.year)
	driver.find_element_by_id("id_date_from").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, \
		Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
	driver.find_element_by_id("id_date_from").send_keys(time_cr)

	#random date in future (+ix years)
	time_cr = str(time_mdl.day)+"."+str(time_mdl.month)+"."+str(time_mdl.year+ix+1)
	driver.find_element_by_id("id_date_to").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, \
		Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
	driver.find_element_by_id("id_date_to").send_keys(time_cr)
	driver.find_element_by_name("submit").click()



#f2 - usinf func to make 2 appls
def test_gb(self):
	driver = self.driver
	print "\nBlock 16:"
	pol_data.login_form_logout(self)
	pol_data.login_form_enter(self, 3)
	err_flag = False
	for itx in range(0, 2):
		driver.get(self.base_url + "/disscouncil/disscouncil/available/")
		fill_form_ga(self, itx)
		pol_data.DataBase_added_disscouncil.append(driver.current_url)
		if driver.find_element_by_xpath(u"//span[@class='label label-warning']").text != u"Находится на верификации":
			err_flag = True
	try: self.assertEqual(False, err_flag)
	except AssertionError as e: self.verificationErrors.append(str(e))


#fc - logging in as mod and rejecting appl -  CRASHING, but working as mod Vlad and user mpetrov - 'Appointment' object has no attribute 'user_post'
def test_gc(self):
	driver = self.driver
	#pol_data.login_form_logout(self)
	#pol_data.login_form_enter(self, 2)
	driver.get(pol_data.DataBase_added_disscouncil[0])
	driver.find_element_by_name("reject").click()
	try: self.assertEqual(u"Отклонено", \
			driver.find_element_by_xpath(u"//span[@class='label label-danger']").text)
	except AssertionError as e: self.verificationErrors.append(str(e))

#fd - logging in as mod and verifying appl
def test_gd(self):
	driver = self.driver
	driver.get(pol_data.DataBase_added_disscouncil[1])
	driver.find_element_by_name("verify").click()
	try: self.assertEqual(u"Верифицировано", \
			driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
	except AssertionError as e: self.verificationErrors.append(str(e))






