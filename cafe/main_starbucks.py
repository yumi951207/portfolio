from time import sleep
import requests
from bs4 import BeautifulSoup
import sys
sys.path.append("./common_mod/")
sys.path.append("./starbucks/")
import const
from GetUrlsStarbucks import GetUrlsStarbucks
from GetInfoStarbucks import GetInfoStarbucks
from ToCSV import ToCSV

getdriver = GetUrlsStarbucks(const.URL_STARBUCKS)
id_list = getdriver.access_site()
cafe_list = []
count = 0
for id in id_list:
    cafe_dict = {}
    url = const.URL_STARBUCKS_BASE + f"detail-{id}/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"lxml")
    getinfostarbucks = GetInfoStarbucks(
        soup,
        ".store-detail__title-text",
        ".store-detail__text-title:-soup-contains('無線LAN')",
        ".store-detail__content-desc > div:first-of-type")
    cafe_d = getinfostarbucks.get_info()
    print(cafe_d)
    cafe_dict["都道府県"] = cafe_d[0]
    cafe_dict["店名"] = cafe_d[1]
    cafe_dict["Wifiの有無"] = cafe_d[2]
    cafe_dict["参考情報"] = cafe_d[3]

    cafe_list.append(cafe_dict)
    sleep(3)
    count += 1
    if count > 5:
        break

tocsv = ToCSV(cafe_list,"starbucks_list")
tocsv.list_to_csv()