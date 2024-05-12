from time import sleep
import const
from selenium import webdriver

class GetDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(executable_path=const.PATH, options=options)

    driver.implicitly_wait(10)

    def __init__(self, url):
        self.url = url

    def access_site(self):
        GetDriver.driver.get(self.url)
        sleep(3)
        