#读取excel数据
import os
from util import get_path
import xlrd
import openpyxl

class ReadExcel:
    # #xlrd读取数据开始
    # def read_excel(self,xlsname,sheetname):
    #     pathDir = get_path.getPath()
    #     read_path = os.path.join(pathDir,'data/' ,xlsname)
    #     print(read_path)
    #     cls=[]
    #     file=xlrd.open_workbook(read_path)
    #     sheet=file.sheet_by_name(sheetname)
    #     rows=sheet.nrows
    #     for i in range(rows):
    #         if sheet.row_values(i)[0]!=u'case_name':
    #             cls.append(sheet.row_values(i))
    #     return cls
    #
    # # xlrd读取数据结束
    #
    #openpyxl读取方法开始
    def __init__(self):
        self.filepath=''
        self.sheet=''

    def open_excel(self):#打开文件
        pathDir = get_path.getPath()
        read_path = os.path.join(pathDir, 'data/', self.filepath)
        workbook=openpyxl.load_workbook(read_path)
        return workbook
    def get_sheet(self):#获取表单
        sheet=self.open_excel()[self.sheet]
        return sheet
    def read_excel(self,filepath,sheet):#获取数据
        self.filepath=filepath
        self.sheet =sheet
        sheettable=self.get_sheet()
        rows=list(sheettable.rows)
        case_list=[]
        title_list=[]
        for title in rows[0]:
            title_list.append(title.value)
        i=1
        for row in rows[1:]:
            i=i+1
            cumvalue=sheettable["G"+str(i)].value
            # print(cumvalue)
            dic={}
            #过滤不需要执行的用例数据
            if cumvalue=='y':
                for idx, val in enumerate(row):
                    dic[title_list[idx]] = val.value
                case_list.append(dic)
        return case_list
    def write_excel(self,row,column,data):#写入数据
        sheet = self.get_sheet()
        sheet.cell(row,column).value=data

    def excel_save(self):#保存excel
        self.open_excel().save(self.filepath)

    def excel_close(self):#关闭excel

        self.open_excel().close()
    # openpyxl读取方法结束


if __name__=='__main__':
    #print(ReadExcel().read_excel('data.xlsx','caselist')[0][1])

    print(ReadExcel().read_excel(get_path.getPath()+'data/interfaces.xlsx','bi'))

