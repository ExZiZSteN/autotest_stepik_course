from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import math


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)

    sum = num1 + num2
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    sleep(5)
    browser.quit()