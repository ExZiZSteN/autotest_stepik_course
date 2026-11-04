from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

    alert = browser.switch_to.alert
    alert.accept()
    sleep(2)
    x_value = browser.find_element(By.ID, "input_value").text
    y = calc(x_value)
    answer = browser.find_element(By.ID, "answer").send_keys(y)
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()

finally:
    sleep(10)
    browser.quit()