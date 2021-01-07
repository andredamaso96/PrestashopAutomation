from selenium import webdriver
import time
from getpass import getpass 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver import ActionChains

username = '**************'
password = '**************'

class MyTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login_process(self):
        self.driver.get("https://web.noblestrategy.pt/lojadobuggy.pt/admin727eibj6a/index.php/sell/catalog/products/82?_token=e09T5RCFkwuGURfZioND8f72BcnbVY7naWB2WNhlXyQ#tab-step1") 
        #successfully navigated to URL_1

        elem = self.driver.find_element_by_id("email")
        elem.clear()
        elem.send_keys(username)

        elem = self.driver.find_element_by_id("passwd")
        elem.clear()
        elem.send_keys(password)
        self.driver.find_element_by_id("submit_login").click()
        time.sleep(3)
        #successfully entered URL_2 

    def query(self):
        # self.driver.get("https://web.noblestrategy.pt/lojadobuggy.pt/")
        # do smth
        # self.driver.execute_script("window.open('https://web.noblestrategy.pt/lojadobuggy.pt/admin727eibj6a/index.php/sell/catalog/products/82?_token=1h8U0YHyxOZLXhJ1wj6KSTqMt59Foog8S1oQ42_mRT8');")
        self.driver.maximize_window()
        for i in range(1278, 3374):
            url = f'https://web.noblestrategy.pt/lojadobuggy.pt/admin727eibj6a/index.php/sell/catalog/products/{i}?_token=e09T5RCFkwuGURfZioND8f72BcnbVY7naWB2WNhlXyQ#tab-step1'
            self.driver.get(url)
            time.sleep(3) 
            self.driver.refresh()
            

            #clicar no token
            self.driver.find_element_by_xpath('//*[@id="csrf-white-container"]/div/div[2]/a[1]').click()
            #WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="csrf-white-container"]/div/div[2]/a[1]'))).click()

            #guardar produto
            try:
                self.driver.find_element_by_id("submit").click()
            except Exception:
                #nao faz nada
                pass

test = MyTest()
test.login_process()
test.query()