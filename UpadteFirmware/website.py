import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

c = "HP LaserJet MFP E52645"
driver = webdriver.Edge(executable_path="C:\Browser\msedgedriver.exe")
driver.get("https://www.hp.com/us-en/home.html")
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='id_3']/ul/li[3]/a").click()
time.sleep(3)
driver.find_element_by_css_selector("div.product-type-text").click()
time.sleep(3)
print(c)
print(list[0])
driver.find_element_by_id("search-input-pfinder").send_keys(list[0])
time.sleep(3)
driver.find_element_by_css_selector("div.findButton  button ").click()

time.sleep(3)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(3)
driver.find_element_by_css_selector("a.firmware").click()
driver.find_element_by_xpath("//*[@id='mp-276693-1']/table/tbody/tr[1]/td[1]/div[2]/p").click()
k=driver.find_element_by_xpath("//*[@id='details-mp-276693-1']/div[1]/div[2]/p[1]")
print(k.text)
J= driver.find_element_by_xpath("//*[@id='details-mp-276693-1']/div[1]/div[2]/p[2]").text
print("Version is ",J)
