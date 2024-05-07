from bs4 import BeautifulSoup

class GetInfo:
    def __init__(self,shop_soup,name,na_wifi,address):
        self.shop_soup = shop_soup
        self.name = name
        self.na_wifi = na_wifi
        self.address = address

    def get_info(self):
        self.shop_name = self.shop_soup.select_one(f"{self.name}")
        if self.shop_soup.select_one(f"{self.na_wifi}"):
            self.free_wifi = "あり"
        else:
            self.free_wifi = "なし"
        
        shop_address = self.shop_soup.select_one(f"{self.address}").text
        prefectures = [
            "北海道","青森県","岩手県","宮城県","福島県","秋田県","山形県","茨城県","栃木県","群馬県","埼玉県","東京都","千葉県","神奈川県","長野県","山梨県","静岡県","愛知県","岐阜県","新潟県","富山県","石川県","福井県",
            "滋賀県","京都府","大阪府","奈良県","三重県","和歌山県","兵庫県","岡山県","広島県","山口県","島根県","鳥取県","香川県","愛媛県","高知県","徳島県","福岡県","大分県","宮崎県","鹿児島県","熊本県","佐賀県","長崎県","沖縄県"]
        for i in prefectures:
            if i in shop_address:
                self.prefecture = i