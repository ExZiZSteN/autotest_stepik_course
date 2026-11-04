from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")

    input_name = browser.find_element(By.TAG_NAME, "input")
    input_name.send_keys("Mikhail")

    input_lastname = browser.find_element(By.NAME, "last_name")
    input_lastname.send_keys("Shestakov")

    input_city = browser.find_element(By.CLASS_NAME, "city")
    input_city.send_keys("Perm")

    input_country = browser.find_element(By.ID, "country")
    input_country.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button#submit_button.btn")

    button.click()

finally:
    time.sleep(30)
    browser.quit()