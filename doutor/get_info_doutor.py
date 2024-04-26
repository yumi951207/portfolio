import requests
from bs4 import BeautifulSoup
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from get_info import GetInfo


class GetInfoDoutor(GetInfo):
    def __init__(self,shop_url,name,na_wifi,address,menu):
        super().__init__(shop_url,name,na_wifi,address)
        self.menu = menu

    def get_menu(self):
        super().get_info()
        shop_r = requests.get(self.shop_url)
        shop_soup = BeautifulSoup(shop_r.content,"lxml")
        shop_menu = shop_soup.select(self.menu)
        menu_list = []
        for menu in shop_menu:
            menu_list.append(menu.text)
        return menu_list