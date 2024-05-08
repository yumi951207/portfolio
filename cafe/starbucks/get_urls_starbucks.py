import sys
from time import sleep
from selenium.webdriver.support.ui import Select
sys.path.append("../common_mod/")
from common_mod import get_driver

class GetUrlsStarBucks(get_driver.GetDriver):
    def __init__(self,url):
        super().__init__(url)

    def access_site(self):
        super().access_site()
        pull_down = GetUrlsStarBucks.driver.find_element_by_css_selector(".selectbox")
        pull_down.click()
        shop_id_list = []
        for i in range(1,2):
            Select(pull_down).select_by_value(str(i))
            sleep(3)
            shops_id = GetUrlsStarBucks.driver.find_elements_by_css_selector(".searching-result__item")
            shop_id_list = [id.get_attribute("data-store_id") for id in shops_id]
            sleep(3)
        
        return shop_id_list