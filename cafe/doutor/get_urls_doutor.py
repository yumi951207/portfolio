import sys
sys.path.append("../common_mod/")
from common_mod import get_driver

class GetUrlsDoutor(get_driver.GetDriver):
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
        shops = GetUrlsDoutor.driver.find_elements_by_css_selector(".w_7_searchresult_1_1-spot-name > a")
        count = 0
        while count < 31:
            next_page = GetUrlsDoutor.driver.find_element_by_id('w_7_searchresult_1_1_searchmore')
            shops = GetUrlsDoutor.driver.find_elements_by_css_selector(".w_7_searchresult_1_1-spot-name > a")
            url_list = [shop.get_attribute("href") for shop in shops]
            next_page.click()
            count += 1

        return url_list

        GetUrlsDoutor.driver.quit()