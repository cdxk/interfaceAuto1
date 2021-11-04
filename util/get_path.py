import os
#获取当前文件所在项目路径
def getPath():
    ##获取当前文件所在路径
    path=os.path.split(os.path.realpath(__file__))[0]
    return path[:-4]
if __name__=='__main__':
    getPath()