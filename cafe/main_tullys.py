from time import sleep
import sys
sys.path.append("./common_mod/")
sys.path.append("./tullys/")
import const
from GetUrlsTullys import GetUrlsTullys

getdriver = GetUrlsTullys(const.URL_TULLYS)
shop_urls = getdriver.access_site()