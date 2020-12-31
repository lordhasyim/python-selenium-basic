from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "webdriver/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("http://www.techwithtim.net")

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    button.click() 

    driver.back()
    driver.back()
    driver.back()


    
except:
    print("failed")