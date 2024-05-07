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
        shop_menu = self.shop_soup.select_one(f"{self.menu}")
        menu_list = []
        for menu in shop_menu:
            menu_list.append(menu.text)
        return self.prefecture,self.shop_name.text,self.free_wifi,menu_list