from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x_element = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    y = calc(x_element)
    answer_element = browser.find_element(By.ID, "answer")
    answer_element.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    submitbtn = browser.find_element(By.CSS_SELECTOR, "button.btn")

    submitbtn.click()

finally:
    sleep(5)
    browser.quit()