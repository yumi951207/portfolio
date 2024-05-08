from time import sleep
import requests
from bs4 import BeautifulSoup
import sys
sys.path.append("./common_mod/")
sys.path.append("./doutor/")
from common_mod import const
from common_mod import to_csv
from doutor import get_urls_doutor
from doutor import get_info_doutor

getdriver = get_urls_doutor.GetUrlsDoutor(const.URL_DOUTOR)
shop_urls = getdriver.access_site()
cafe_list = []
for url in shop_urls:
    cafe_dict = {}
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"lxml")
    getinfodoutor = get_info_doutor.GetInfoDoutor(
        soup,"h1","td:-soup-contains('FREE Wi-Fi')","tr.w_7_detail_2_2_5-spot-detail-row > td",
        "#w_7_detail_2_2_3-widget-body > table > tbody > tr:first-of-type > td > span")
    cafe_d = getinfodoutor.get_info()
    print(cafe_d)
    cafe_dict["都道府県"] = cafe_d[0]
    cafe_dict["店名"] = cafe_d[1]
    cafe_dict["Wifiの有無"] = cafe_d[2]
    cafe_dict["メニュー"] = cafe_d[3]

    cafe_list.append(cafe_dict)
sleep(3)
# print(cafe_list)

tocsv = to_csv.ToCSV(cafe_list,"doutor_list")
tocsv.list_to_csv()