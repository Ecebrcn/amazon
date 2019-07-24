from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time



browser = webdriver.Chrome(executable_path = "C:\\Users\\User\\Desktop\\python\\chromedriver.exe")

browser.get("https://www.amazon.com.tr")

time.sleep(1)

login = browser.find_element_by_id("nav-link-accountList")
login.click()

time.sleep(2)

email = browser.find_element_by_name("email")
password = browser.find_element_by_name("password")

time.sleep(1)

email.send_keys("srnbrcn@gmail.com")
password.send_keys("ecece1234")

time.sleep(1)

sign_in = browser.find_element_by_xpath("//*[@id='signInSubmit']")

sign_in.click()

time.sleep(1)

search_alani = browser.find_element_by_xpath("//*[@id='twotabsearchtextbox']")

search_alani.send_keys("samsung")

time.sleep(3)

search = browser.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input")

search.click()

time.sleep(3)

ikinci_sayfa = browser.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[7]/div/div/div/ul/li[3]/a")

ikinci_sayfa.click()

time.sleep(3)

secilen_urun = browser.find_element_by_xpath("//*[@id='search']/div[1]/div[2]/div/span[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span")

secilen_urun.click()

time.sleep(3)

#add_list = browser.find_element_by_xpath("//*[@id='add-to-wishlist-button-submit']")

add_list = browser.find_element_by_id("add-to-wishlist-button-submit")

add_list.click()

time.sleep(3)

wish_list = browser.find_element_by_id("WLHUC_viewlist")

wish_list.click()

remove = browser.find_element_by_xpath("//*[@class ='a-link-normal a-declarative g-visible-js']")

remove.click()

time.sleep(1)

browser.close()

