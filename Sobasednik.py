from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Windows/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://qahacking.guru/")
time.sleep(2)
driver.set_window_size(1500,900)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[3]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/nav/div[2]/ul/li[3]/a").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div[3]/div/div[2]/div[3]/div/div[1]/div[1]/div/div/div[3]/div[7]/a[1]").click()
time.sleep(2)
driver.find_element(By.NAME, "quantity[0]").click()
time.sleep(2)
driver.find_element(By.NAME, "quantity[0]").clear()
driver.find_element(By.NAME, "quantity[0]").send_keys("10")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".cart_reload > img").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Оформить заказ").click()
time.sleep(2)
driver.find_element(By.ID, "f_name").click()
driver.find_element(By.ID, "f_name").send_keys("Кристина")
driver.find_element(By.ID, "l_name").click()
driver.find_element(By.ID, "l_name").send_keys("Студент")
driver.find_element(By.ID, "email").click()
driver.find_element(By.ID, "email").send_keys("mail@mail.ru")
driver.find_element(By.ID, "street").click()
driver.find_element(By.ID, "street").send_keys("123")
driver.find_element(By.ID, "zip").click()
driver.find_element(By.ID, "zip").send_keys("432010")
driver.find_element(By.ID, "city").click()
driver.find_element(By.ID, "city").send_keys("Идеальск")
driver.find_element(By.ID, "country").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='country']/option[177]").click()
driver.find_element(By.ID, "phone").click()
driver.find_element(By.ID, "phone").send_keys("79958643311")
driver.find_element(By.NAME, "next").click()
time.sleep(2)
driver.find_element(By.ID, "payment_submit").click()
driver.find_element(By.CSS_SELECTOR, ".button").click()
driver.find_element(By.NAME, "finish_registration").click()
driver.find_element(By.ID, "agb").click()
driver.find_element(By.NAME, "finish_registration").click()
time.sleep(2)