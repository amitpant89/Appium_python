__author__ = 'WP8Dev'
import os
import unittest
import time
from appium import webdriver
''' ScrollTest.com by Promode '''
''' This Test Case Just Click on the Refresh Button My Application '''
''' Just Click and Verify it in you Phone '''
''' Copyright 2015 '''


class ContactAppTestAppium(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'ZY322BQKG5'
        desired_caps['app'] = 'D:\\apk\\foneapp.apk'
        desired_caps['appPackage'] = 'com.clearfly.groupfone'
        desired_caps['appActivity'] = '.activities.SplashActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(7)
    def test_clicklogin(self):
                                        
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click() 
        

       ## loginButton = 


        for x in range(1,6):
             print  self.driver.find_element_by_id("com.clearfly.groupfone:id/tvLogin")
        ##time.sleep(5)
        
        print loginButton
        print loginButton.is_displayed()

        print self.assertTrue(loginButton.is_displayed())   
        
        ##loginButton.click()
        
        '''self.driver.find_element_by_id("com.clearfly.groupfone:id/country_isd_code_text_view").click()
        self.driver.find_element_by_id("com.clearfly.groupfone:id/country_code").click()
        loginButton = self.driver.find_element_by_id("com.clearfly.groupfone:id/tvLogin")
        self.assertTrue(loginButton.is_displayed())
        loginButton.click()

        ##self.driver.find_element_by_id("com.clearfly.groupfone:id/tvIsdCode").click()
        ##time.sleep(3)
        ##self.driver.find_element_by_id("com.clearfly.groupfone:id/country_name").click() 
        
      

        ##Click I Agree & continue
        iagree = self.driver.find_element_by_id("com.clearfly.groupfone:id/btn_agreement")
        self.assertTrue(iagree.is_displayed())
        iagree.click()'''

        


        
        

        
         

        ## Right now we are just verify the displayed message on the Phone
        ## You can right code to handle that toast message and Verify that message


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ContactAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)


