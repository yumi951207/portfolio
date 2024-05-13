from time import sleep
from selenium.webdriver.support.ui import Select
from GetDriver import GetDriver
from const import STARBUCKS

class GetUrlsStarbucks(GetDriver):
    def __init__(self,url):
        super().__init__(url)

    def access_site(self):
        super().access_site()
        pull_down = GetUrlsStarbucks.driver.find_element_by_css_selector(STARBUCKS.PULL_DOWN_CSS.value)
        pull_down.click()
        shop_id_list = []
        for i in range(1,2):
            Select(pull_down).select_by_value(str(i))
            sleep(3)
            shops_id = GetUrlsStarbucks.driver.find_elements_by_css_selector(STARBUCKS.SHOP_ID_CSS.value)
            shop_id_list = [id.get_attribute(STARBUCKS.ATTR.value) for id in shops_id]
            sleep(3)
        GetUrlsStarbucks.driver.quit()
        return shop_id_list
