from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os
import urllib
import time
# Author Maximover


def download_gif(text, font_size):
    desired_text = text
    desired_font_size = font_size

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://cooltext.com/Logo-Design-Burning")
        # XPath
        text_input = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td[2]/div[1]/div/form/div[1]/table/tbody/tr[1]/td[2]/textarea')
        image_handle = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td[2]/center[1]/img[1]')
        font_input = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/div[1]/div/form/div[1]/table/tbody/tr[3]/td[2]/input')
        text_input.send_keys(desired_text)
        font_input.send_keys(Keys.CONTROL + 'a')
        font_input.send_keys(desired_font_size)
        time.sleep(5)
        image_link = image_handle.get_attribute("src")
        PATHTOSAVE = "text.gif".encode('unicode_escape')
        urllib.request.urlretrieve(image_link, PATHTOSAVE)
        driver.quit()
        print(f'File {desired_text}.gif was created successfully')
    except:
        print(f"An Error Ocurred")
        if driver: driver.quit()