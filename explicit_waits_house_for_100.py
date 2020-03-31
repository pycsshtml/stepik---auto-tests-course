# 2.4 Задание: ждем нужный текст на странице
# https://stepik.org/lesson/181384/step/8?unit=156009

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math 
import time

# Определении математической функции:
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    # Запуск броузера и сайта
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # Selenium должен проверять в течение 12 секунд, пока цена не снизится до 100
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
            )
    # Нажатие на кнопку "book"
    button = browser.find_element_by_id("book")
    button.click()
    # Поиск поля для введения ответа    
    x = browser.find_element_by_css_selector('#input_value').text
    # Вызов функции
    y = calc(x)
    # Вставить ответ
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    # Нажать на кнопку "submit"
    button = browser.find_element_by_css_selector("button.btn[type='submit']")
    button.click()

finally:
    # Время для копирование кода пользователем
    time.sleep(10)
    # Закрыть броузер
    browser.quit()
