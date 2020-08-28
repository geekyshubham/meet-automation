import time
import re
import string
import random
import sys
import colorama
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from random import randint
from __banner.myBanner import bannerTop
from __colors__.colors import *

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########
typex = 'chrome'

'''
batch=input("Enter your batch B1 or B2 or B3: ")

if not batch.upper() in ['B1','B2','B3']:
    print("Enter correct batch")
    batch=input("Enter your batch B1 or B2 or B3: ")

if batch == 'B3':
    pass
'''
SE ='https://meet.google.com/xot-pzip-wnh'

CN = 'https://meet.google.com/yko-bysx-ksm'

OOP = 'https://meet.google.com/zfa-gmjq-itd'

DAIT='https://meet.google.com/zpy-qpau-git'

DAIL='https://meet.google.com/cez-ztbd-vdn'

TEST= 'https://meet.google.com/tsx-vtox-mdw'

#Prof Kalpesh Joshi	https://meet.google.com/gib-cuik-uma

OT=PY='https://meet.google.com/jxw-eped-jqa'


def start_bot(meet_url,user_mail,password):
    try:
        # For Chrome
        if typex == 'chrome':
            chrome_options = Options()
            #options.add_argument("--incognito","--start-maximized","--headless")
            #set chrome options to disable mic and cam
            chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'./webdriver/chromedriver')
        # For Firefox
        elif typex == 'firefox':
            cap = DesiredCapabilities().FIREFOX
            cap['marionette'] = True
            driver = webdriver.Firefox(capabilities=cap, executable_path=r'./webdriver/geckodriver')
        elif typex == '':
            print(fr + 'Error - Run setup.py first')
            exit()
    except Exception as e:
        time.sleep(0.4)
        print('\n' + fr + 'Error - '+ str(e))
        exit()

    driver.maximize_window()
    print("First Sign In to Your VIT Account: ")
    driver.get('https://accounts.google.com')
    driver.find_element_by_xpath("//input[@id='identifierId']").send_keys(user_mail)
    driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']").click()
    time.sleep(5)

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH,'//input[@type="password"]'))
    ).send_keys(password)

    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()

  
    time.sleep(3)
    driver.get(meet_url)
    
    print("Successfully Signed In Now lets join Meeting :v ")
    time.sleep(10)
    
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
  
    time.sleep(3)

    driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//body/div/c-wiz/div/div/div/div/div/div/div[4]/div[1]/span[1]/span[1]').click()
    time.sleep(3)
    attendies = driver.find_element_by_xpath('//body/div/c-wiz/div/div/div/div/div/div/div/div/div[1]/span[1]/span[1]/div[1]/div[1]/span[2]').text
    time.sleep(600)
    while(True):
        attendies = driver.find_element_by_xpath('//body/div/c-wiz/div/div/div/div/div/div/div/div/div[1]/span[1]/span[1]/div[1]/div[1]/span[2]').text
        print(attendies)
        if int(attendies) < 20:
            driver.find_element_by_xpath('//body/div/c-wiz/div/div/div/div/div/div[2]/div[2]/div[1]/span[1]/span[1]//*[local-name()="svg"]').click()
        else:
            comments = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH,'//div//div//div//div//div//div//div//div//div//div[3]//span[1]//span[1]//div[1]//div[1]//span[2]'))
    ).send_keys(password)


def main():
    sys.stdout.write(bannerTop())
    print("MADE WITH ❤ BY SHUBHAM")

    user_input = input("Enter Subject:\nSE for Soft.Engineering\nOOP for JAVA CPP\nDAIT for DAI Theory\nDAIL for DAI Labs\n Enter Code: ")
    
    meet_url = globals()[user_input]

    user_mail=input("Enter your VIT email : ")
    password=input("Enter your password : ")

    start_bot(meet_url,user_mail,password)

if __name__ == '__main__':
    main()