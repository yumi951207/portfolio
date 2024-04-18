import const
import requests
from bs4 import BeautifulSoup

class GetInfo:
    def __init__(self,b_url):
        self.b_url = b_url

    def get_info(self):
        r = requests.get(self.b_url)
        soup = BeautifulSoup(r.content,"lxml")
        branch_name = soup.select_one(".store-detail__title-text")
        if soup.select_one(".store-detail__text-detail:-soup-contains('STARBUCKS')"):
            free_wifi = "あり"
        else:
            free_wifi = "なし"
        cafe_d = {}
        address = soup.select_one(".store-detail__content-text").text
        print(address)
        prefecture_l = [
            "北海道道","青森県","岩手県","宮城県","福島県","秋田県","山形県","茨城県","栃木県","群馬県","埼玉県","東京都","千葉県","神奈川県","長野県","山梨県","静岡県","愛知県","岐阜県","新潟県","富山県","石川県","福井県",
            "滋賀県","京都府","大阪府","奈良県","三重県","和歌山県","兵庫県","岡山県","広島県","山口県","島根県","鳥取県","香川県","愛媛県","高知県","徳島県","福岡県","大分県","宮崎県","鹿児島県","熊本県","佐賀県","長崎県","沖縄県"]
        for i in prefecture_l:
            if i in address:
                prefecture = i
        cafe_d["都道府県"] = prefecture
        cafe_d["店名"] = branch_name.text
        cafe_d["Wifiの有無"] = free_wifi
        return cafe_d