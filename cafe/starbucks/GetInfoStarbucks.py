from bs4 import BeautifulSoup
from GetInfo import GetInfo

class GetInfoStarbucks(GetInfo):
    def __init__(self, shop_url, name, na_wifi, address):
        super().__init__(shop_url, name, na_wifi, address)

    def get_info(self):
        super().get_info()
        if self.shop_soup.select_one(".access-row:-soup-contains('参考情報')"):
            return self.prefecture, self.shop_name.text, self.free_wifi, self.shop_soup.select_one(".access-row:-soup-contains('参考情報')").text
        else:
            return self.prefecture, self.shop_name.text, self.free_wifi, "なし"