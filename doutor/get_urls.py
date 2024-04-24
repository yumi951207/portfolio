from time import sleep
import const
from selenium import webdriver

class GetUrls():
    def __init__(self,url):
        self.url = url

    def get_urls(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

        driver = webdriver.Chrome(executable_path=const.PATH,options=options)

        driver.implicitly_wait(10)

        driver.get(self.url)
        sleep(3)

        # while True:
        #     next_page = driver.find_element_by_id('w_7_searchresult_1_1_searchmore')
        #     shops = driver.find_elements_by_css_selector(".w_7_searchresult_1_1-spot-name > a")
        #     url_list = [shop.get_attribute("href") for shop in shops]
        #     try:
        #         next_page.click()
        #     except:
        #         break
        # return url_list
        count = 0
        while count < 31:
            next_page = driver.find_element_by_id('w_7_searchresult_1_1_searchmore')
            shops = driver.find_elements_by_css_selector(".w_7_searchresult_1_1-spot-name > a")
            url_list = [shop.get_attribute("href") for shop in shops]
            next_page.click()
            count += 1

        return url_list

        driver.quit()
        