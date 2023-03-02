from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class interaction:
    def webinteraction(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        driver.get("http://localhost/opencart/upload/index.php?route=common/home&language=en-gb")
        driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("Macbook")
        driver.find_element(By.XPATH,"//button[@class='btn btn-light btn-lg']").click()
        driver.find_element(By.XPATH,"//img[@title='MacBook Pro']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[@id='button-cart']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[normalize-space()='1 item(s) - $2,000.00']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//strong[normalize-space()='Checkout']").click()
        driver.close()

interact=interaction()
interact.webinteraction()