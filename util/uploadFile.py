#上传文件返回存储路径
from common import configHttp
from util import readExcel
from util import readConfig,readExcel,geturl,get_path
from common.log import logs
from requests_toolbelt import MultipartEncoder
import requests,random

case=None
class UploadFile:
    def __init__(self,sheet):
        print("UploadFile开始。。。")
        global case
        if case == None:
            case = readExcel.ReadExcel().read_excel(get_path.getPath() + 'data/interfaces.xlsx', sheet)
        logs.info("UploadFile开始。。。")

    #获取具体的接口用例
    def getInterface(self,name):
        for n in case:
            if n['name']==name:
                return n

    def upload(self,interfaceName):
        interdata = self.getInterface(interfaceName)
        files =eval(interdata['param'])
        headers=eval(interdata['header'])
        multiencode=MultipartEncoder(
            files,
            boundary='------'+ str(random.randint(1e28, 1e29 - 1)))
        headers['Content-Type']=multiencode.content_type
        result= requests.post(url=interdata['interface'],data=multiencode,headers=headers)
        print(result.content)
        return result


if __name__=='__main__':
    UploadFile("产量波动分析").upload("上传文件")
