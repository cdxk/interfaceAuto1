import requests
import json

class ConfigHttp():
    def __init__(self):
        self.headers={"content-type": "application/json; charset=UTF-8",
               "x-api-token": "T000000523f6df79-e44d-4803-8db2-757884389f59"}
    def send_get(self,url,header,data):
        result=requests.get(url=url,data=data,headers=header).json()
        res=json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)
        return res
    def send_post(self,url,header,data):
        #json.dumps(data)将python编码转换为json字符串
        result=requests.post(url=url,data=json.dumps(data),headers=header).json()
        res =json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
        return res
    def send_delete(self,url):
        result=requests.delete(url).json()
        res =json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
        return res

    def run_method(self,method,url,header,data):
        result=None
        if method=='get':
            result=self.send_get(url,header,data)
        elif method=='post':
            result = self.send_post(url, header,data)
        elif method=='delete':
            result = self.send_delete(url)
        else:
            print('method值不正确')
        return result

if __name__=='__main__':
    result=ConfigHttp().run_method('get','https://saleswork.crm3test.lwork.com/api/v1/platform/user/getCurUser?queryType=LEVEL_ALL','','')
    print(result)

