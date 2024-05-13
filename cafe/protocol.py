from typing import Protocol

class GetUrlsProtocol(Protocol):
    def access_site(self,url):
        ...


class GetinfoProtocol(Protocol):
    def get_info(self):
        ...