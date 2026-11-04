from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    x_value = browser.find_element(By.ID, "input_value")
    x = x_value.text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "label[for='robotCheckbox']")

    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")

    radiobutton.click()

    submitbtn = browser.find_element(By.CSS_SELECTOR, "button.btn")

    submitbtn.click()

finally:
    sleep(5)
