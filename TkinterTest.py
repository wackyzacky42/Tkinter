from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# from Tkinter import *


# master =  Tk()
# Label(master, text = "First Name").grid(row = 0)
# Label(master, text = "Last Name").grid(row = 1)

# e1 = Entry(master)
# e2 = Entry(master)

# e1.grid(row = 0, column = 1)
# e2.grid(row = 1, column = 1)

# mainloop()

# root = Tk()

# w = Label(root, text = "Hello Tkinter!")
# #w.pack()

# root.mainloop()

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
actions =  ActionChains(driver)
driver.implicitly_wait(10)
# driver.get("http://auth-main.motiga.net:83/0.0/login")
# elem = driver.find_element_by_name("login")
# elem.send_keys("zackn@motiga.com")
# elem = driver.find_element_by_name("password")
# elem.send_keys("password")
# elem.send_keys(Keys.RETURN)
# driver.get("http://auth-main.motiga.net:83/0.0/player_search")
# driver.navigate().to("http://www.google.com")
# elem = driver.find_element_by_xpath("/0.0/player_search")
#elem = driver.find_element_by_id("environment")
#print(elem)
driver.get("http://auth-main.motiga.net:83/0.0/player_search")
elem = driver.find_element_by_name("login")
elem.send_keys("zackn@motiga.com")
elem = driver.find_element_by_name("password")
elem.send_keys("password")
elem.send_keys(Keys.RETURN)
time.sleep(2)
elem = driver.find_element_by_id("email-search")
elem.send_keys("zackn@motiga.com")
elem.send_keys(Keys.RETURN)
time.sleep(2)
elem = driver.find_element_by_link_text("Player Account")
elem.click()
time.sleep(2)
# elem = driver.find_element_by_link_text("Player Account")#kvstoreEditModal
# currentURL = driver.current_url
# print(currentURL)
# driver.get(currentURL + "#kvstoreEditModal")
elem = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div/h2/a")
elem.send_keys(Keys.RETURN)
time.sleep(2)
elem = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div/div/div/div/form/div[1]/textarea")
profile_text = dict(elem.text)
print profile_text.get("totalgold")
# print elem.text
# elem.clear()
# elem.send_keys(profile_text)

# actions.click()
# assert "Nominations" in driver.title
# driver.get("http://auth-main.motiga.net:83/0.0/player_search")

# driver.close()
# ACTION CHAINS!!!!!
# http://selenium-python.readthedocs.org/en/latest/api.html#module-selenium.webdriver.common.action_chains