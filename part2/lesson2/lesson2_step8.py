from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import math
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    firstname = browser.find_element(By.NAME, "firstname").send_keys('dsa')
    lastname = browser.find_element(By.NAME, "lastname").send_keys('dsa')
    email = browser.find_element(By.NAME, "email").send_keys('dsa')

    file_input = browser.find_element(By.NAME, "file")
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(curr_dir, "image_2025-08-29_01-42-57.png")
    file_input.send_keys(file)
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    sleep(10)
    browser.quit()