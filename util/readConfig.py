#读取config.ini配置文件信息
import os
from util import get_path
import configparser

pathDir=get_path.getPath()
config_path=os.path.join(pathDir,'config.ini')


class ReadConfig():
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(config_path, encoding='utf-8-sig')
    def get_config(self,key,name):
        value=self.config.get(key,name)
        return value

if __name__=='__main__':
    print(ReadConfig().get_config('HTTP','scheme'))


