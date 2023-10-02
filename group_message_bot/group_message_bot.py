from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

#fill array with responses
response = []
driver.get('https://www.instagram.com/')

#Change username and password to your username and password
wait.until(ec.element_to_be_clickable((By.NAME, "username"))).send_keys(username)
el = wait.until(ec.element_to_be_clickable((By.NAME, "password")))
el.send_keys(password)

sleep(5)

el.send_keys(Keys.ENTER)

sleep(5)
 #Change URL to custom message URL
driver.get(URL)
sleep(5)
driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
sleep(5)

def send_message():
  message_bar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
  message_bar.send_keys(random.choice(response))
  message_bar.send_keys(Keys.ENTER)

def page_source_update():
 output = driver.page_source
 with open('page_source.txt', 'w', encoding= "utf-8") as f:
  f.write(output)
  f.close()
 f1 = open('page_source.txt', 'r')
 num = f1.read()
 #Change prompt to custom prompt that bot will respond too.
 count = num.count(prompt)
 return count

 
def message_loop(x):
 search_text = "Thoughts?"
 stop_command = "Stop!"
 count = x
 #Change URL to custom message URL
 driver.get(URL)
 sleep(10)
 prompts = page_source_update()

 if x == 0 and x != prompts:
  count = prompts
  sleep(3)
  message_loop(count)
 elif x != 0 and x < prompts:
  send_message()
  count = prompts
  sleep(3)
  message_loop(count)
 else:
  message_loop(count)   
 


message_loop(0)



 

 



