import os
from util import get_path
import configparser

pathDir=get_path.getPath()
config_path=os.path.join(pathDir,'config.ini')


class EditConfig():
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read(config_path, encoding='utf-8-sig')
    def edit_config(self,key,name,value):
        self.config.set(key,name,value)
        self.config.write(open(config_path,"r+",encoding='utf-8-sig'))

if __name__=='__main__':
     EditConfig().edit_config("CARDISPATCH","taskId","bbaa")


