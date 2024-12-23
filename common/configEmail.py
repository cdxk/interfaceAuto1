import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from util import get_path,readConfig
from common.log import logs


class SendEmail():
    def send_attach(self,file_name):
        ReadConfig=readConfig.ReadConfig()
        msg_from=ReadConfig.get_config('EMAIL','from')
        pwd=ReadConfig.get_config('EMAIL','password')
        to=ReadConfig.get_config('EMAIL','to')
        message=MIMEMultipart()
        #发件人名字
        message['From']=Header('test <%s>'%msg_from)
        #收件人名字
        message['To']=Header('emilee <%s>'%to)
        #邮件标题
        subject='Python 自动化测试报告'
        file_path=os.path.join(get_path.getPath()+'data/'+file_name)
        message['Subject']=Header(subject,'utf-8')
        #邮件内容
        message.attach(MIMEText('这是自动化测试脚本邮件。。','plain','utf-8'))
        #邮件附件
        att=MIMEText(open(file_path,'rb').read(),'base64','utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中附件显示什么名字
        att["Content-Disposition"] = 'attachment; filename="data.xlsx"'
        message.attach(att)
        try:
            # 连接smtp服务器，明文/SSL/TLS三种方式，根据你使用的SMTP支持情况选择一种
            # 纯粹的ssl加密方式，通信过程加密，邮件数据安全
            #接收邮件服务器： imap.qq.com，使用SSL，端口号993；发送邮件服务器： smtp.qq.com，使用SSL，端口号465或587
            smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
            smtp.ehlo()
            smtp.login(msg_from, pwd)
            logs.info("--------发送邮件到%s"%to)
            smtp.sendmail(msg_from, to, message.as_string())
            print('success')


            # 普通方式，通信过程不加密
            # smtp = smtplib.SMTP(smtpHost,smtpPort)
            # smtp.ehlo()
            # smtp.login(username,password)


            # tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
            # 使用正常的smtp端口smtp = smtplib.SMTP(smtpHost, smtpPort)
            # smtp.set_debuglevel(True)
            # smtp.ehlo()
            # smtp.starttls()
            # smtp.ehlo()
            # smtp.login(username, password)

        except Exception as e :
            print(e)

if __name__=='__main__':
    SendEmail().send_attach('interfaces.xlsx')
