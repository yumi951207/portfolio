import requests
from bs4 import BeautifulSoup

class GetInfo:
    def __init__(self,shop_url,name,na_wifi,address):
        self.shop_url = shop_url
        self.name = name
        self.na_wifi = na_wifi
        self.address = address

    def get_info(self):
        shop_r = requests.get(self.shop_url)
        shop_soup = BeautifulSoup(shop_r.content,"lxml")
        shop_name = shop_soup.select_one(f"{self.name}")
        if shop_soup.select_one(f"{self.na_wifi}"):
            free_wifi = "あり"
        else:
            free_wifi = "なし"
        
        shop_address = shop_soup.select_one(f"{self.address}").text
        prefectures = [
            "北海道","青森県","岩手県","宮城県","福島県","秋田県","山形県","茨城県","栃木県","群馬県","埼玉県","東京都","千葉県","神奈川県","長野県","山梨県","静岡県","愛知県","岐阜県","新潟県","富山県","石川県","福井県",
            "滋賀県","京都府","大阪府","奈良県","三重県","和歌山県","兵庫県","岡山県","広島県","山口県","島根県","鳥取県","香川県","愛媛県","高知県","徳島県","福岡県","大分県","宮崎県","鹿児島県","熊本県","佐賀県","長崎県","沖縄県"]
        for i in prefectures:
            if i in shop_address:
                prefecture = i
        return prefecture,shop_name.text,free_wifi
    
class GetInfoDoutor(GetInfo):
    def __init__(self,shop_url,name,na_wifi,address,menu):
        super().__init__(shop_url,name,na_wifi,address)
        self.menu = menu

    def get_menu(self):
        shop_r = requests.get(self.shop_url)
        shop_soup = BeautifulSoup(shop_r.content,"lxml")
        shop_menu = shop_soup.select(self.menu)
        menu_list = []
        for menu in shop_menu:
            menu_list.append(menu.text)
        return menu_list