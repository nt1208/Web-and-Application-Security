from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

driver = webdriver.Chrome()

url = "https://tiki.vn/"
driver.get(url) 


driver.implicitly_wait(2)  # seconds
search_field = driver.find_element(By.CSS_SELECTOR, 'input[data-view-id="main_search_form_input"]')

search_field.send_keys("laptop")

search_field.send_keys(Keys.RETURN) 


calalog = driver.find_element(By.CSS_SELECTOR, 'div[class="CatalogProducts__Wrapper-sc-1r8ct7c-0 jOZPiC"]')
items = calalog.find_elements(By.CSS_SELECTOR, 'div[class="styles__ProductItemContainerStyled-sc-bszvl7-0 elOGIo"]')

for item in items:
    try:
        info = WebDriverWait(item, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="content"]')))
    except StaleElementReferenceException:
        # If StaleElementReferenceException occurs, refresh the item
        item = driver.find_element(By.CSS_SELECTOR, 'div[class="styles__ProductItemContainerStyled-sc-bszvl7-0 elOGIo"]')
        info = WebDriverWait(item, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class="content"]')))

    try:
        price_field = info.find_element(By.CSS_SELECTOR, 'div[class="price-discount__price"]')
        html_string = price_field.get_attribute('innerHTML')
        numeric_string = re.sub(r'\D', '', html_string)
        formatted_string = '{:,}'.format(int(numeric_string)).replace(',', '.')

    except NoSuchElementException:
        # Handle case when price element is not found
        formatted_string = "Price not available"

    try:
        name_field = info.find_element(By.CSS_SELECTOR, 'div[class="style__AboveProductNameStyled-sc-m30gte-0 hjPFIz above-product-name-info"]')
        name = name_field.text
    except NoSuchElementException:
        # Handle case when name element is not found
        name = "Name not available"
    try:
        sold_field1 = info.find_element(By.CSS_SELECTOR, 'span[class*="quantity"]')
        sold = sold_field1.text
        numbers = re.findall(r'\d+', sold)
        number_string = ''.join(numbers)
    except:
 
        number_string = "0"

    

    print("Name:", name)
    print("Price:", formatted_string + " Sold: "+ number_string)
   

time.sleep(20)

driver.quit()
