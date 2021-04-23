from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

import time

from bs4 import BeautifulSoup as bs
import requests
from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep

# https://pythonhosted.org/pynput/mouse.html


def download_pdf(mouse):

    # Reset mouse position to allow scrolling in web app
    mouse.position = (138, 14)
    # print('The current pointer position is {0}'.format(
    # mouse.position))
    sleep(1)
    mouse.click(Button.left, 1)
    

    # 
    mouse.position = (193, 200)

    sleep(1)
    mouse.click(Button.left, 1)

    #
    mouse.position = (994, 603)
    sleep(4)
    mouse.click(Button.left, 1)

def login(driver):

    login_url = "https://proxylogin.nus.edu.sg/libproxy1/public/login.asp?logup=false"
    user = "nusstu\E0014980"
    pw = "Yoshi4498&*("
    
    wait = ui.WebDriverWait(driver, 20)

    driver.get(login_url)
    time.sleep(2)


    # select type of user
    Select(driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td[4]/div[2]/form/table/tbody/tr[1]/td[2]/select")).select_by_index(1)

    # user name/email field
    user = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td[4]/div[2]/form/table/tbody/tr[2]/td[2]/input")
    user.send_keys("nusstu\E0014980")

    #password field
    pw = driver.find_element(By.XPATH, "/html/body/table[2]/tbody/tr[3]/td[4]/div[2]/form/table/tbody/tr[3]/td[2]/input")
    pw.send_keys("Yoshi4498&*(")

    # login button
    confirm = wait.until(
        ec.element_to_be_clickable((By.XPATH, "/html/body/table[2]/tbody/tr[3]/td[4]/div[2]/form/input[2]"))
    )
    sleep(1)
    confirm.click()

    # accept t&c button
    accept_terms = wait.until(
        ec.element_to_be_clickable(
            (By.XPATH, "/html/body/table[2]/tbody/tr[3]/td[4]/div/form/input[2]")
        )
    )
    sleep(1)
    accept_terms.click()
    sleep(1)


# sleep(5)

# action = webdriver.ActionChains(driver)
# action.key_down(Keys.COMMAND).send_keys("s").perform()







# print("Program Stopped")


if __name__ == '__main__':
    def on_press(key):
        pass


    def on_release(key):
        global running
        if key == keyboard.Key.esc:
            running = False


    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()


    driver = webdriver.Chrome("/Users/brandonthio/Python/chromedriver")

    login(driver)
    ## Oxford Fundamentals of Surgery (110 Chapters) URL:https://oxfordmedicine-com.libproxy1.nus.edu.sg/view/10.1093/med/9780199665549.001.0001/med-9780199665549-chapter-{}?print=pdf'.format(i)
    import ESC_scrape

    urls = ESC_scrape.get_urls()
    
    for i in range(310, len(urls)):
        print(i, urls[i])
        driver.get(urls[i])
        sleep(6)

        mouse = Controller()
        download_pdf(mouse)
        sleep(3)

    # for i in range(1,98):

    #     ## Oxford Apprach to Medical Decision Making (97 Chapters)
    #     txt_bk_url = 'https://oxfordmedicine-com.libproxy1.nus.edu.sg/view/10.1093/med/9780190862800.001.0001/med-9780190862800-chapter-{}?print=pdf'.format(i)
    #     driver.get(txt_bk_url)
    #     sleep(13)

    #     mouse = Controller()
    #     download_pdf(mouse)
    #     sleep(3)


    # Initialise mouse controller


    print("Program Stopped")

