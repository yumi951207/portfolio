from time import sleep
import const
from get_urls import GetUrls
from get_info_doutor import GetInfoDoutor
from to_csv import ToCSV

geturls = GetUrls(const.URL)
shop_urls = geturls.get_urls()
cafe_list = []
for url in shop_urls:
    cafe_dict = {}
    getinfodoutor = GetInfoDoutor(
        url,"h1","td:-soup-contains('FREE Wi-Fi')","tr.w_7_detail_2_2_5-spot-detail-row > td",
        "#w_7_detail_2_2_3-widget-body > table > tbody > tr:first-of-type > td > span")
    cafe_d = getinfodoutor.get_info()
    cafe_menu_d = getinfodoutor.get_menu()
    cafe_dict["都道府県"] = cafe_d[0]
    cafe_dict["店名"] = cafe_d[1]
    cafe_dict["Wifiの有無"] = cafe_d[2]
    cafe_dict["メニュー"] = cafe_menu_d

    cafe_list.append(cafe_dict)
sleep(3)

tocsv = ToCSV(cafe_list)
tocsv.list_to_csv()
