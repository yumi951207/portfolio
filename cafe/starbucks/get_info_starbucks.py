import sys
from bs4 import BeautifulSoup
sys.path.append("../common_mod/")
from common_mod import cafe_info

class GetInfoDoutor(cafe_info.GetInfo):
    def __init__(self,shop_url,name,na_wifi,address):
        super().__init__(shop_url,name,na_wifi,address)

    def get_info(self):
        super().get_info()
        if self.shop_soup.select_one(".access-row:-soup-contains('参考情報')"):
            return self.shop_soup.select_one(".access-row:-soup-contains('参考情報')")
        else:
            return "なし"