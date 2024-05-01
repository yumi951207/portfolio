import requests
import sys
from bs4 import BeautifulSoup
sys.path.append("../common_mod/")
from common_mod import cafe_info

class GetInfoDoutor(cafe_info.GetInfo):
    def __init__(self,shop_url,name,na_wifi,address,menu):
        super().__init__(shop_url,name,na_wifi,address)
        self.menu = menu

    def get_info(self):
        super().get_info()
        shop_r = requests.get(self.shop_url)
        shop_soup = BeautifulSoup(shop_r.content,"lxml")
        shop_menu = shop_soup.select_one(f"{self.menu}")
        menu_list = []
        for menu in shop_menu:
            menu_list.append(menu.text)
        return menu_list