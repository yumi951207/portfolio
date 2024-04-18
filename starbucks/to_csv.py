import pandas as pd

class ToCSV(object):
    def __init__(self,list):
        self.list = list

    def list_to_csv(self):
        df = pd.DataFrame(self.list)
        df.to_csv('starbucks_list.csv',index=None,encoding='utf-8-sig')