from GetDriver import GetDriver
from const import TULLYS
# from typing import Protocol

# class GetUrlsDoutorProtocol(Protocol):
#     def access_site(self) -> list:
#         ...

class GetUrlsTullys(GetDriver):
    def __init__(self,url):
        super().__init__(url)

    def access_site(self):
        super().access_site()
        # shops = GetUrlsTullys.driver.find_elements_by_css_selector(TULLYS.SHOPS_CSS)
        # url_list = [shop.get_attribute(TULLYS.ATTR) for shop in shops]

        iframe = GetUrlsTullys.driver.switch_to_frame(GetUrlsTullys.driver.find_element_by_tag_name("iframe"))
        GetUrlsTullys.driver.switch_to.frame(iframe)
        # GetUrlsTullys.driver.execute_script('window.scrollTo(0,500)')

        GetUrlsTullys.driver.quit()
