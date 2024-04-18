from time import sleep
import const
from get_urls import GetUrls
from get_info import GetInfo
from to_csv import ToCSV

geturls = GetUrls(const.URL)
id_list = geturls.get_urls()
cafe_list = []
for id in id_list:
    shop_url = const.BASE_URL + f"detail-{id}/"
    getinfo = GetInfo(shop_url)
    cafe_dict = getinfo.get_info()
    cafe_list.append(cafe_dict)
    sleep(3)

tocsv = ToCSV(cafe_list)
tocsv.list_to_csv()
