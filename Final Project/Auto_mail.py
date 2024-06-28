
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

driver = webdriver.Chrome()

# Navigate to a webpage
driver.maximize_window()

driver.get("https://accounts.google.com/v3/signin/identifier?ifkv=AaSxoQxb9tcMaa03oR2dqoaFnE_k4er1TnnF6FSedFpR_U7kR-Itp2RmMObFToj_9_yG-4S3IdOAQw&lp=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1308527356%3A1716776840944936&ddm=0")
mail_field = driver.find_element(By.NAME,"identifier")
mail_field.send_keys("abc@gmail.com")
mail_field.send_keys(Keys.RETURN)

driver.implicitly_wait(2)
password_field = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.NAME, "Passwd"))
            )
password_field.send_keys("abc")
password_field.send_keys(Keys.RETURN)

compose_btn = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'div[class="T-I T-I-KE L3"]'))
            )
compose_btn.click()

driver.implicitly_wait(5)

recipient_field = driver.recipient_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'input[class="agP aFw"]'))
            )
recipient_field.send_keys("heo2097@gmail.com")
recipient_field.send_keys(Keys.RETURN)

content_field = driver.find_element(By.CSS_SELECTOR,'div[class="Am aiL Al editable LW-avf tS-tW"]')
content_field.send_keys("HELLOOOOOOOOO test auto mail")

send_btn = driver.find_element(By.CSS_SELECTOR,'div[class="T-I J-J5-Ji aoO v7 T-I-atl L3"]')
send_btn.click()


time.sleep(20)
driver.close()


# Close the browser
driver.quit()