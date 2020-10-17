from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

PATH = "/home/ignacio/development/chromedriver"


option = webdriver.ChromeOptions()
option.add_argument("-incognito")

browser = webdriver.Chrome(PATH, options=option)

browser.get("https://github.com/theAspiringDev1")
# wait for the browser for timeout
timeout = 20

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".avatar.avatar-user.width-full.border.bg-white")))
except TimeoutException:
    print("TIMED OUT")
    browser.quit()


# FIND PIN REPOS

pinned_repos = browser.find_elements_by_css_selector(
    "a.text-bold.flex-auto.min-width-0")

languages = browser.find_elements_by_xpath(
    "//span[@itemprop='programmingLanguage']")

titles = [pin.text for pin in pinned_repos]
programming_languages = [lang.text for lang in languages]
programming_languages = programming_languages[:6]

git_repos = []

for title, lang in zip(titles, programming_languages):
    git_repos.append({
        "repo_title": title,
        "language": lang
    })

for item in git_repos:
    print(item)
