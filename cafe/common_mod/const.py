from enum import Enum

PATH = r"C:\repository\cafe\tool\chromedriver.exe"
URL_DOUTOR = "https://shop.doutor.co.jp/doutor/spot/list?category=01"
URL_STARBUCKS = "https://store.starbucks.co.jp/?nid=mm"
URL_STARBUCKS_BASE = "https://store.starbucks.co.jp/"
URL_TULLYS = "https://shop.tullys.co.jp/all"

class DOUTOR(Enum):
    SHOPS_CSS = ".w_7_searchresult_1_1-spot-name > a"
    NEXTPAGE_ID = "w_7_searchresult_1_1_searchmore"
    ATTR = "href"

class STARBUCKS(Enum):
    PULL_DOWN_CSS = ".selectbox"
    SHOP_ID_CSS = ".searching-result__item"
    ATTR = "data-store_id"

class TULLYS(Enum):
    SHOPS_CSS = "store__link"
    ATTR = "href"