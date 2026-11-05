import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block > .first_class > input")
        first_name.send_keys("Mikhail")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block > .second_class > input")
        last_name.send_keys("Shestakov")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block > .third_class > input")
        email.send_keys("fasfa")

        phone = browser.find_element(By.CSS_SELECTOR, ".second_block > .first_class > input")
        phone.send_keys('23141')
        address = browser.find_element(By.CSS_SELECTOR, ".second_block > .second_class > input")
        address.send_keys("dsadfafv")

        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()

        sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block > .first_class > input")
        first_name.send_keys("Mikhail")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block > .second_class > input")
        last_name.send_keys("Shestakov")
        email = browser.find_element(By.CSS_SELECTOR, ".first_block > .third_class > input")
        email.send_keys("fasfa")

        phone = browser.find_element(By.CSS_SELECTOR, ".second_block > .first_class > input")
        phone.send_keys('23141')
        address = browser.find_element(By.CSS_SELECTOR, ".second_block > .second_class > input")
        address.send_keys("dsadfafv")

        submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
        submit_button.click()

        sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()