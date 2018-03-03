from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import sys

fidelityUsername = sys.argv[0]
fidelityPassword = sys.argv[1]

everyDollarUsername = sys.argv[2]
everyDollarPassword = sys.argv[3]

fidelityURL = 'https://www.fidelity.com/'

fidelityWebDriver = webdriver.Chrome("D:/selenium/chromedriver")

everyDollarURL = 'https://www.everydollar.com/app/sign-in'

everyDollarWebDriver = webdriver.Chrome(sys.argv[4])
#everyDollarWebDriver = webdriver.Chrome("D:/selenium/chromedriver")



def fidelityLogin():
    fidelityWebDriver.get(fidelityURL)
    time.sleep(1)
    userNameBox = fidelityWebDriver.find_element_by_id("userId-input")
    time.sleep(1)
    userNameBox.send_keys(fidelityUsername)
    time.sleep(1)
    passwordBox = fidelityWebDriver.find_element_by_id("password")
    passwordBox.send_keys(fidelityPassword)
    fidelityWebDriver.fullscreen_window()
    passwordBox.send_keys(Keys.ENTER)

#<a href="javascript:void(0)" class="action-bar--mobile action-bar--accounts action-bar--button-clicked action-bar--animation-slide-in">Accounts</a>

def fidelityNavigateToTransactionsAfterLogin():
    time.sleep(5)
    #positionsTab = fidelityWebDriver.find_element_by_id("tab-2")
    #positionsTab.click()

def everyDollarLogin():

    everyDollarWebDriver.get(everyDollarURL)
    time.sleep(5)
    edUserNameBox = everyDollarWebDriver.find_element_by_name("email")
    edUserNameBox.send_keys(everyDollarUsername)
    edPasswordBox = everyDollarWebDriver.find_element_by_name("password")
    edPasswordBox.send_keys(everyDollarPassword)
    edPasswordBox.send_keys(Keys.ENTER)
    time.sleep(5)

def addTransactions(list):
    pyautogui.click(pyautogui.locateCenterOnScreen('addTransactionSticker.png'))
    time.sleep(2)
    pyautogui.click(pyautogui.locateCenterOnScreen('secondAddTransactionSticker.png'))


#fidelityLogin()
#fidelityNavigateToTransactionsAfterLogin()

everyDollarLogin()

addTransactions([])