#coding=utf-8_sig
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
#for session
import time, os, unittest, time, re, sys

test_root_folder = 'work-bin/'



class Login(unittest.TestCase):
    
    #def setUp(self):
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


    #First browser engine initialization
    @classmethod
    def setUpClass(self):
        os.system("setxkbmap us")
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.249/"
        self.verificationErrors = []
        self.accept_next_alert = True

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # "*tests.py" file collector inside special directory
    for (path, dirs, files) in os.walk(test_root_folder):
        for f in sorted(files):
            if f.endswith('tests.py'):
                sys.path.append(path)
                fname = f.split('.py')[0]
                exec "from %s import *" % fname

    # TestUnit special functions                
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    
if __name__ == "__main__":
    unittest.main()
