from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
PATH = "/home/ignacio/development/chromedriver"

email = ""
pw = ""
target_user = ""

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
driver = webdriver.Chrome(PATH,)
driver.get("https://messenger.com")

form = driver.find_element_by_tag_name("form")
email = form.find_element_by_id("email")
password = form.find_element_by_id("pass")
submit = form.find_element_by_tag_name("button")

email.send_keys(email)
password.send_keys(pw)
submit.send_keys(Keys.ENTER)
icons = driver.find_elements(
    By.CSS_SELECTOR, "._1ht5._2il3._6zka._5l-3._3itx")
current = None

for icon in icons:
    # if(icon.get_attribute("data-href"))
    if(f"https://www.messenger.com/t/{target_user}" == icon.get_attribute("data-href")):
        current = icon
    else:
        print("NOT FOUND")


current.click()
message_head = driver.find_element(
    By.CSS_SELECTOR, "._1mf._1mj")
# .notranslate._5rpu div div div span span
message_head.send_keys("Specified Message!")


message_head.send_keys(Keys.ENTER)
