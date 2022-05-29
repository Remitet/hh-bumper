from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys
import os

#Сетим логин-пароль
LOGIN = ''
PASSWORD = ''

#Раскоментировать для безоконного режима

#options = webdriver.ChromeOptions()
#options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_argument("--headless")

#Путь к хромдрайверу. (для безоконного режима добавить options=options после пути к драйверу)
driver = webdriver.Chrome(executable_path='')

def Login():
    print("Логинимся")
    driver.get(url="https://hh.ru/account/login")
    driver.find_element(by=By.XPATH, value="//button[@data-qa='expand-login-by-password']").click()
    driver.find_element(by=By.XPATH, value="//input[@data-qa='login-input-username']").send_keys(LOGIN)
    driver.find_element(by=By.XPATH, value="//input[@data-qa='login-input-password']").send_keys(PASSWORD)
    driver.find_element(by=By.XPATH, value="//button[@data-qa='account-login-submit']").click()
    time.sleep(3)

def Bump():
    driver.get(url="https:hh.ru/applicant/resumes?hhtmFromLabel=header&hhtmFrom=main")
    time.sleep(3)
    driver.find_element(by=By.XPATH, value='//button[@data-qa="resume-update-button"]').click()
    time.sleep(2)
    driver.quit()
    print("На кнопку поднятия cv нажал!")

try:
    Login()
    Bump()
    print("Ждем 5 минут")
    time.sleep(300)
except:
    print("Все сломалось")

#Перезапускаем скрипт по кд
python = sys.executable
os.execl(python, python, *sys.argv)