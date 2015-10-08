# coding=utf-8_sig
#Conf module Tests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#for session
import time, os, unittest, time, re, sys, pol_data, datetime 

#conf add form fill function
def fill_from_ca(self):
    driver = self.driver

    driver.find_element_by_id("id_russian_name").clear()
    os.system("setxkbmap ru")

    temp_conf_name = pol_data.db_conf_name_gen()
    
    driver.find_element_by_id("id_russian_name").send_keys(temp_conf_name)
    
    driver.find_element_by_id("id_english_name").clear()
    os.system("setxkbmap us")
    driver.find_element_by_id("id_english_name").send_keys("EN_"+temp_conf_name)
    
    driver.find_element_by_id("id_acronyms").clear()
    os.system("setxkbmap ru")
    driver.find_element_by_id("id_acronyms").send_keys(pol_data.d_acro)
    
    driver.find_element_by_id("id_website").clear()
    os.system("setxkbmap us")
    driver.find_element_by_id("id_website").send_keys(pol_data.d_web)

    #changing date to hell
    time_mdl = datetime.datetime.now()
    time_cr = str(time_mdl.day)+"."+str(time_mdl.month)+"."+str(time_mdl.year)
    driver.find_element_by_name("start_date").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, \
        Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
    driver.find_element_by_name("start_date").send_keys(time_cr)
    #eoc

    #generating searching filed for future ZC ticket
    pol_data.DataBase_added_confs_names.append(temp_conf_name)

    #changing date to hell
    time_cr = str(time_mdl.day)+"."+str(time_mdl.month)+"."+str(time_mdl.year+0)
    driver.find_element_by_name("end_date").send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, \
        Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
    driver.find_element_by_name("end_date").send_keys(time_cr)
    #eoc
                
    driver.find_element_by_id("id_country_0").clear()
    os.system("setxkbmap ru")
    driver.find_element_by_id("id_country_0").send_keys(pol_data.d_country)
    time.sleep(2)
    driver.find_element_by_css_selector("span.hilight").click()
    
    driver.find_element_by_id("id_city_0").clear()
    driver.find_element_by_id("id_city_0").send_keys(pol_data.d_city)
    driver.find_element_by_css_selector("span.hilight").click()

    driver.find_element_by_id("id_organization_0").clear()
    driver.find_element_by_id("id_organization_0").send_keys(pol_data.d_org)
    driver.find_element_by_css_selector("span.hilight").click()

    driver.find_element_by_name("submit").click()

#@unittest.skip("spec")
def test_aa(self):
    #making 6confs with different IDs
    atm_error = False
    print "\nBlock 11:"
    driver = self.driver
    driver.get(self.base_url)
    #pol_data.login_form_enter(self, 1)
    #iterations    
    for itx in range(0, 6):
        driver.get(self.base_url + "/conference/conference")
        fill_from_ca(self)
        pol_data.DataBase_added_confs.append(driver.current_url)
        if driver.find_element_by_xpath(u"//span[@class='label label-warning']").text != u"Находится на верификации":
            atm_error = True
    try: self.assertEqual(False, atm_error)
    except AssertionError as e: self.verificationErrors.append(str(e))

#Login as mod
#block 1

#@unittest.skip("spec")
def test_ab(self):
    driver = self.driver
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 2)
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-1])
    driver.find_element_by_name("reject").click()
    try: self.assertEqual(u"Отклонена верификатором", \
            driver.find_element_by_xpath(u"//span[@class='label label-danger']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_ac(self):
    #TODO make a some changes in data, heh
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-2])
    driver.find_element_by_name("save").click()
    try: self.assertEqual(u"Находится на верификации", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_ad(self):
    #TODO make a some changes in data, heh
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-2])
    driver.find_element_by_name("change").click()
    try: self.assertEqual(u"Отредактирована верификатором", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_ae(self):
    #TODO make a some changes in data, heh
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-3])
    driver.find_element_by_name("change").click()
    try: self.assertEqual(u"Отредактирована верификатором", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_af(self):
    #TODO make a some changes in data, heh
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-4])
    driver.find_element_by_name("change").click()
    try: self.assertEqual(u"Отредактирована верификатором", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_ag(self):
    #2nd to make another way - accdup by user
    #TODO make a compared conf exact
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-5])
    driver.find_element_by_xpath("//div[@id='right_sidebar']/div/div").click()
    driver.find_element_by_id("id_conference_0").clear()
    driver.find_element_by_id("id_conference_0").send_keys("Qqq")
    driver.find_element_by_css_selector("span.hilight").click()
    driver.find_element_by_name("duplicate").click()
    try: self.assertEqual(u"Помечена верификатором как дубликат", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_ah(self):
    #2nd to make another way - accdup by user
    #TODO make a compared conf exact
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-6])
    driver.find_element_by_xpath("//div[@id='right_sidebar']/div/div").click()
    time.sleep(2)
    driver.find_element_by_id("id_conference_0").clear()
    driver.find_element_by_id("id_conference_0").send_keys("Qqq")
    driver.find_element_by_css_selector("span.hilight").click()
    driver.find_element_by_name("duplicate").click()
    try: self.assertEqual(u"Помечена верификатором как дубликат", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#block 2
#login as user 
#***********************

#@unittest.skip("spec")
def test_ai(self):
    driver = self.driver
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 3)
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-1])
    driver.find_element_by_name("change").click()
    try: self.assertEqual(u"Находится на верификации", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_aj(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-2])
    driver.find_element_by_name("accept").click()
    try: self.assertEqual(u"Автор подтвердил правки", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_ak(self):
    #12; TODO make a compared conf exact
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-3])
    driver.find_element_by_name("change").click()
    try: self.assertEqual(u"Находится на верификации", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_al(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-4])
    driver.find_element_by_name("save").click()
    try: self.assertEqual(u"Отредактирована верификатором", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_am(self):
    #Tdod: check test text
    driver = self.driver
    driver.find_element_by_name("change").click()
    try: self.assertEqual(u"Находится на верификации", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_an(self):
    #TODO make a compared conf exact
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-5])
    driver.find_element_by_name("decline_dup").click()
    try: self.assertEqual(u"Находится на верификации", \
            driver.find_element_by_xpath(u"//span[@class='label label-warning']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

#@unittest.skip("spec")
def test_ao(self):
    #TODO checing after crash
    #crash
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-6])
    time.sleep(2)
    driver.find_element_by_name("accept_dup").click()
    try: self.assertEqual(u"Автор подтвердил дубликат конференции", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))


#block 3
#login as mod
#***********************

#@unittest.skip("spec")
def test_ap(self):
    driver = self.driver
    pol_data.login_form_logout(self)
    pol_data.login_form_enter(self, 2)
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-1])
    driver.find_element_by_name("verify").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

def test_aq(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-2])
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

def test_ar(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-3])
    driver.find_element_by_name("verify").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

@unittest.skip("spec")
def test_as(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-4])
    driver.find_element_by_name("verify").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

@unittest.skip("spec")
def test_at(self):
    driver = self.driver
    driver.get(pol_data.DataBase_added_confs[len(pol_data.DataBase_added_confs)-5])
    driver.find_element_by_name("verify").click()
    try: self.assertEqual(u"Верифицирована", \
            driver.find_element_by_xpath(u"//span[@class='label label-success']").text)
    except AssertionError as e: self.verificationErrors.append(str(e))

