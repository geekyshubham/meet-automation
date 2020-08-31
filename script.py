
import time
import re
import string
import random
import sys
import colorama
import os
import collections
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
from __colors__.colors import * #colors for banner
from pyenviron import *
from __dataFiles__ import rollCalls
from __timeCheck__.timeCheck import * #for future time_table integration


######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########

typex = 'chrome'
#chrome support only as of now for countering instability


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

CPPJ = 'https://meet.google.com/zfa-gmjq-itd'

DAIT='https://meet.google.com/zpy-qpau-git'

DAIL='https://meet.google.com/cez-ztbd-vdn'

TEST= 'https://meet.google.com/tsx-vtox-mdw'

#Prof Kalpesh Joshi	https://meet.google.com/gib-cuik-uma

OT=PY='https://meet.google.com/jxw-eped-jqa'


def start_bot(meet_url,user_mail,password,messageString):
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
    roll_no = int(messageString.split(' ')[0])
    classMates = rollCalls.getClassmates(roll_no)
    #fetching the previous message senders
    driver.maximize_window()
    print("First Signing In to Your VIT Account: ")
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
    timeStamp=currentTime()
    endTime=endTimer(timeStamp)
    time.sleep(10)
    #dismiss_popup
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
  
    time.sleep(3)
    #join meeting
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[1]'))).click()
    time.sleep(3)
    #pin_bottom_bar --- not necessary though ---
    driver.implicitly_wait(10)
    #message pane opening...
    driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span').click()
    time.sleep(5)
    peoples = (driver.find_element_by_xpath('//body/div/c-wiz/div/div/div/div/div/div/div/div/div/div[1]/span[1]/div[1]/span[2]').text).replace('(','').replace(')','')
    print("no of people joined:"+peoples)

    time.sleep(20*60)#sleep time where no actions are performed
    
    print("Reading Messages and Checking if people are leaving...")
    print("your roll_no is : "+str(roll_no))
    print("your msg string is: "+messageString)
    messages = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[1]')
    run_once=0
    while(True):
        peoples = int((driver.find_element_by_xpath('//body/div/c-wiz/div/div/div/div/div/div/div/div/div/div[1]/span[1]/div[1]/span[2]').text).replace('(','').replace(')',''))
        if (int(peoples)<25):#25_num defines when to leave meeting
            driver.get('https://www.google.com')
            print("\nLEFT MEETING ")
            break
        else:
            messages = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[4]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[1]')
            inner_text= driver.execute_script("return arguments[0].innerText;", messages)
            lines = inner_text.split('\n')
            time.sleep(1)


            sys.stdout.write("\rTotal Messages Count:"+str(int(len(lines)/2))+" Last Message: "+str(lines[-1]))
            sys.stdout.flush()
            Msg=str(lines[-1]).lower() #fetching the last message and lowering case for comaparision
            
            lMsg=rollCalls.stringHandeler(Msg)
            
            for mates in classMates:
                temp=mates.split()
                
                if collections.Counter(lMsg)==collections.Counter(temp[:3]):#comparing 
                    #messaging bot
                    time.sleep(3)
                    if run_once==0:
                        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//textarea[@name='chatTextInput']"))).send_keys(messageString)
                        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
                    run_once=1

            ###the code below has different logic based on no of msgs it decides to send msg. ###
            ### deprecated code ###
            '''
            if ((int(len(lines)/2)) > (roll_no-2)):#temp_changes
                WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"//textarea[@name='chatTextInput']"))).send_keys(messageString)

                webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
                # WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.XPATH,"//body/div/c-wiz/div/div/div/div/div/div/div/div/div/span/div/div/div[2]"))).click()
                roll_no=69696
                print("Message Sent!")
                time.sleep(5)
            '''
    
        


 
def main():
    
    sys.stdout.write(bannerTop())
    

    user_input = input("Enter Subject:\nSE for Soft.Engineering\nOOP for JAVA CPP\nDAIT for DAI Theory\nDAIL for DAI Labs\nCN for Computer Network \nEnter Code: ")
    
    meet_url = globals()[user_input]
    messageString=input("Enter Your roll_no space your name for msg.: ")
    user_mail=input("Enter your VIT email : ")
    password=input("Enter your password : ")

    ###ENTER BELOW FIELDS TO GET RID OF INPUTS###
    
    '''
    meet_url=TEST
    user_mail='shubham.takankhar19@vit.edu'
    password =os.environ.get('PASS')
    messageString='55 Shubham'
    '''

    start_bot(meet_url,user_mail,password,messageString)

if __name__ == '__main__':
    main()
