from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Сетим логин-пароль
LOGIN = ''
PASSWORD = ''

# Раскоментировать для безоконного режима
# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("--no-sandbox")


# Путь к хромдрайверу. (для безоконного режима добавить options=options после пути к драйверу)
# driver = webdriver.Chrome(executable_path='')


def Login():

    print("Логинимся")
    driver.get(url="https://hh.ru/account/login")
    driver.find_element(
        by=By.XPATH, value="//button[@data-qa='expand-login-by-password']").click()
    driver.find_element(
        by=By.XPATH, value="//input[@data-qa='login-input-username']").send_keys(LOGIN)
    driver.find_element(
        by=By.XPATH, value="//input[@data-qa='login-input-password']").send_keys(PASSWORD)
    driver.find_element(
        by=By.XPATH, value="//button[@data-qa='account-login-submit']").click()
    time.sleep(3)


def Bump():
    driver.get(
        url="https:hh.ru/applicant/resumes?hhtmFromLabel=header&hhtmFrom=main")
    time.sleep(5)
    try:
        driver.find_element(
            by=By.XPATH, value='//button[@data-qa="resume-update-button"]').click()
    except:
        print("Не вижу кнопки, может уже нажата")
    time.sleep(5)
    driver.quit()
    # print("На кнопку поднятия cv нажал!")


if __name__ == "__main__":
    while True:
        try:
            driver = webdriver.Chrome(options=options)
            Login()
            Bump()
            print("Кнопка успешно нажалась, ждем 4 часа...")
            time.sleep(14401)

        except:
            print("Все сломалось, либо скрипт не нашел кнопку. \nНО ничего страшного через 4 часа скрипт перезапустится")
            time.sleep(14401)
