import yaml
import os


class ReadData():
    def __init__(self,filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename

    def read_data(self):
        with open(self.filename,"r",encoding="utf-8")as f:
             return yaml.load(f)
#
# if __name__ == '__main__':
#     list=[]
#     for data in ReadData("login_data.yaml").read_data().values():
#         list.append(
#             (data.get("username"), data.get("password"), data.get("expect_result"), data.get("expect_toast")))
#     print(list)

