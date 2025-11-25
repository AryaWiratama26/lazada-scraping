import time, random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv
from typing import Literal

TYPE_FILE = Literal['csv', 'txt']

CHROME_DRIVER_PATH = "/usr/bin/chromedriver"

OP = webdriver.ChromeOptions()
# OP.add_argument('--headless')  
OP.add_argument("--disable-blink-features=AutomationControlled")

OP.add_argument("--no-sandbox")
OP.add_argument("--disable-dev-shm-usage")
OP.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36")

service = Service(executable_path=CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=service, options=OP)


DATA_SCARPING = {
    'title': [],
    'price': []
}


class LazadaBot:
    def __init__(self):
        pass
    


    def __save_to_file(self, file_type, price, title, output_file):
        if file_type == 'csv':

            with open(f"{output_file}.csv", "a") as f:

                writer = csv.writer(f)
                writer.writerow([title, price])
        elif file_type == 'txt':

            with open(f"{output_file}.txt", "a") as f:
                f.write(f"{title}, {price}\n")
        else:

            raise ValueError("Harus csv atau txt!")

    def scrap(self, keyword, n_data, output_file, file_type: TYPE_FILE = 'csv'):

        try:
            driver.get("https://www.lazada.co.id/")


            time.sleep(2)

            search_keyword = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Cari di Lazada']"))
            )

            search_keyword.send_keys(keyword)
            search_keyword.send_keys(Keys.ENTER)

            start = 0
            end = 800

            time.sleep(3)
            driver.execute_script(f"window.scrollTo({start}, {end});")
            time.sleep(2)


           
            div_card = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-qa-locator='product-item']"))
            )

            for card in div_card[:n_data]:


                try:        
                    price = card.find_element(By.XPATH, ".//span[contains(text(), 'Rp')]").text
                    title = card.find_element(By.CSS_SELECTOR, "a[title]").text
                    
                    price = price.replace("Rp", "")
                    price = price.replace(".", "")
                    price = price.replace(",", "")
                    
                    
                    DATA_SCARPING['title'].append(title)
                    DATA_SCARPING['price'].append(price)

                    
                    self.__save_to_file(file_type, price, title, output_file)

                    print(f"Data di scraping, file bernama {output_file}.{file_type}")

                except Exception as e:
                    print("Errorr brow:\n {e}")


            time.sleep(5)

        except Exception as e:
            
            print(e)

             