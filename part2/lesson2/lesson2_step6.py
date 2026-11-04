from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    x_value = browser.find_element(By.ID, "input_value").text
    y = calc(x_value)
    browser.execute_script("window.scrollBy(0, 100);")

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    radio.click()

    submitbtn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submitbtn.click()
finally:
    sleep(5)
    browser.quit()
