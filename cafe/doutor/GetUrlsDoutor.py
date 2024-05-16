from GetDriver import GetDriver
from const import DOUTOR
from typing import Protocol

class GetUrlsDoutorProtocol(Protocol):
    def access_site(self) -> list:
        ...

class GetUrlsDoutor(GetUrlsDoutorProtocol, GetDriver):
# while True:
#     next_page = driver.find_element_by_id('w_7_searchresult_1_1_searchmore')
#     shops = driver.find_elements_by_css_selector(".w_7_searchresult_1_1-spot-name > a")
#     url_list = [shop.get_attribute("href") for shop in shops]
#     try:
#         next_page.click()
#     except:
#         break
# return url_list
    def __init__(self,url):
        super().__init__(url)

    def access_site(self):
        super().access_site()
        # shops = GetUrlsDoutor.driver.find_elements_by_css_selector(".w_7_searchresult_1_1-spot-name > a")
        count = 0
        while count < 31:
            next_page = GetUrlsDoutor.driver.find_element_by_id(DOUTOR.NEXTPAGE_ID.value)
            shops = GetUrlsDoutor.driver.find_elements_by_css_selector(DOUTOR.SHOPS_CSS.value)
            url_list = [shop.get_attribute(DOUTOR.ATTR.value) for shop in shops]
            next_page.click()
            count += 1

        GetUrlsDoutor.driver.quit()
        return url_list