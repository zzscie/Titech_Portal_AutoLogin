#coding:utf-8
#using the English version Titech Protal webstie to get in to the login page
#will get the username and password from the txt file and then fill the Student ID and Password automatically
#detect the card pass word required and look up the Card.txt dictionary
#
#
#required :
#library: selenium
#browser : Safari with webdriver
#Tyuu-Titech
#completeted at 10/03/2017 12:00AM
#All right reserverd
import urllib
import urllib2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Position:
    def __init__(self,str):
        self.x = ord(str[1])-ord('A')+1
        self.y = str[3]
    def Str2Pos(self):
        pos = (int(self.y)-1) * 10 + self.x -1
        return pos
class Autologin:
    def __init__(self):
        self.Username= [];
        self.Password= [];
        self.Card = [];
        self.url= 'https://portal.titech.ac.jp/portal-e.pl'
    def GetUserInfo(self):
        self.Userinfo = open("UserInfo.txt","r");
        self.Username = self.Userinfo.readline();
        self.Password= self.Userinfo.readline();
    def Disaplay(self):
        print "the student ID is :"+self.Username;
        print "the User's Password is :"+self.Password;
    def GetCardInfo(self):
        #the password card's row is from 1 to 7
        #the password card's column is from A to J
        #ord() function and chr() function help to tranform between ASCII values and Char
        self.Card = open("Card.txt","r").read().split();
        print "the User's password card is ";
        for i in range(1,8):
            print;
            for j in range(1,11):
                flag = (i-1)*j + j-1;
                print self.Card[flag],
# the following part will be the network connect part
    def ConnectToWebsite(self):
        browser = webdriver.Safari();
        browser.get(self.url)
        button = browser.find_element_by_xpath("//*[@id='portal-form']/form[2]/input")
        button.click()

        wait = WebDriverWait(browser,5)
        wait.until(EC.presence_of_element_located((By.NAME,'OK')))

        browser.implicitly_wait(3)
        usr = browser.find_element_by_name('usr_name')
        usr.send_keys(self.Username)
        password = browser.find_element_by_name('usr_password')
        password.send_keys(self.Password)
        time.sleep(3)

        button_first = browser.find_element_by_xpath('/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[5]/td/input[1]')
        button_first.click()
        time.sleep(3)

        Pass1=browser.find_element_by_xpath('/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[5]/th[1]')
        Pass2=browser.find_element_by_xpath('/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[6]/th[1]')
        Pass3=browser.find_element_by_xpath('/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[7]/th[1]')

        P1 = Position(Pass1.text).Str2Pos();
        P2 = Position(Pass2.text).Str2Pos();
        P3 = Position(Pass3.text).Str2Pos();

        elem1 = browser.find_element_by_name('message3')
        elem2 = browser.find_element_by_name('message4')
        elem3 = browser.find_element_by_name('message5')
        ##########
        elem1.send_keys(self.Card[P1])
        elem2.send_keys(self.Card[P2])
        elem3.send_keys(self.Card[P3])
        ##########
        button_last=browser.find_element_by_name('OK')
        button_last.click()
if __name__ == '__main__':
    Student = Autologin();
    Student.GetUserInfo();
    Student.Disaplay();
    Student.GetCardInfo();
    Student.ConnectToWebsite();
    while(True):
        x=0;#something will let the script loop forever
