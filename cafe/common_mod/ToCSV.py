import pandas as pd
from typing import Protocol

class ToCSVProtocol(Protocol):
    def list_to_csv(self) -> None:
        ...

class ToCSV(ToCSVProtocol):
    def __init__(self, list, list_name):
        self.list = list
        self.list_name =  list_name

    def list_to_csv(self):
        df = pd.DataFrame(self.list)
        df.to_csv(f'{self.list_name}.csv', index=None, encoding='utf-8-sig')