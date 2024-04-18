from time import sleep
from selenium.webdriver.support.ui import Select
import const


from selenium import webdriver

class GetUrls:
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

        pull_down = driver.find_element_by_css_selector(".selectbox")
        pull_down.click()
        shop_id_list = []
        for i in range(1,2):
            Select(pull_down).select_by_value(str(i))
            sleep(3)
            shops = driver.find_elements_by_css_selector(".searching-result__item")
            for shop in shops:
                shop_id = shop.get_attribute("data-store_id")
                shop_id_list.append(shop_id)
            sleep(3)
        
        return shop_id_list
        driver.quit()

    