from typing import Protocol

class GetUrlsProtocol(Protocol):
    def access_site(self, url) -> str:
        ...


class GetinfoProtocol(Protocol):
    def get_info(self,shop_soup, name, na_wifi, address) -> str:
        ...

class GetCSVProtocol(Protocol):
    def list_to_csv(self,list, list_name) -> str:
        ...

def url_func(geturlsprotocol: GetUrlsProtocol):
    geturlsprotocol.access_site()

def info_func(getinfoprotocol: GetinfoProtocol):
    getinfoprotocol.get_info()

def info_func(getcsvprotocol: GetCSVProtocol):
    getcsvprotocol.list_to_csv()