import csv
import os
import json
from log_utils import logUtils

logger=logUtils.get_logger(__name__)

class DataUtils:
    @staticmethod
    def read_login_data_csv():
        """读取登录测试数据"""
        data_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"data","login_data.csv")
        data = []
        with open(data_path,encoding="utf_8") as f:
            reader=csv.DictReader(f)
            for row in reader:
                data.append({
                    "username":row["username"],
                    "password":row["password"]
                })
        return data

if __name__=='__main__':
    data=DataUtils.read_login_data_csv()
    print(data[0]['username'])