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


def fill_form_kb(self, itx):
	#itx=ix+1
	driver = self.driver
	driver.get(self.base_url + "/grant/part")
	driver.find_element_by_id("id_grant_0").clear()
	driver.find_element_by_id("id_grant_0").send_keys("CONC_15_07_14")
	driver.find_element_by_css_selector("span.hilight").click()

	driver.find_element_by_name("select").click()
	driver.find_element_by_id("id_project_name").clear()
	driver.find_element_by_id("id_project_name").send_keys("nazv_project")

	driver.find_element_by_id("id_project_abstract").clear()
	driver.find_element_by_id("id_project_abstract").send_keys("anotation_proj")

	driver.find_element_by_id("id_degree").clear()
	driver.find_element_by_id("id_degree").send_keys("0,5")

	driver.find_element_by_link_text(u"Добавить соавтора").click()
	driver.find_element_by_id("id_internal-0-user_post_0").clear()
	driver.find_element_by_id("id_internal-0-user_post_0").send_keys(u"Гагарский Кирилл Алексеевич")
	driver.find_element_by_css_selector("span.hilight").click()

	driver.find_element_by_id("id_internal-0-degree").clear()
	driver.find_element_by_id("id_internal-0-degree").send_keys("0,25")

	driver.find_element_by_xpath(u"(//a[contains(text(),'Добавить соавтора')])[2]").click()
	driver.find_element_by_id("id_external-0-user_name").clear()
	driver.find_element_by_id("id_external-0-user_name").send_keys(pol_data.db_fake_staff_gen())

	driver.find_element_by_id("id_external-0-organization_0").clear()
	driver.find_element_by_id("id_external-0-organization_0").send_keys(u"СПбПУ")
	driver.find_element_by_css_selector("span.hilight").click()

	driver.find_element_by_id("id_external-0-degree").clear()
	driver.find_element_by_id("id_external-0-degree").send_keys("0,25")

	driver.find_element_by_name("submit").click()

#1.0.1
#title test
#@unittest.skip("spec")
def test_ka(self):                
	driver = self.driver
	print "\nBlock 19:"
	driver.get(self.base_url + "/grant/part/available")
	try: self.assertEqual(u"Рабочий офис — Список заявок", driver.title)
	except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_kb(self):
	atm_error = False
	driver = self.driver
	pol_data.login_form_logout(self)
	pol_data.login_form_enter(self, 3)
	for ix in range(0, 1):
		fill_form_kb(self, ix)
		#if driver.find_element_by_xpath(u"//span[@class='label label-warning']").text != u"Находится на верификации":
		#    atm_error = True
		pol_data.DataBase_added_grant.append(driver.current_url)
	try: self.assertEqual(atm_error, False)
	except AssertionError as e: self.verificationErrors.append(str(e))




