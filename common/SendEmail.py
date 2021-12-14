#导入发送邮件模块
import smtplib
#导入构造邮件模块
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from util import readConfig
from util import get_path
from email.mime.application import MIMEApplication
from common.log import logs

class SendEmail():
    def sendemail(self):
        msg_from = readConfig.ReadConfig().get_config("EMAIL", "from")
        msg_password = readConfig.ReadConfig().get_config("EMAIL", "authorizationcode")
        msg_to = readConfig.ReadConfig().get_config("EMAIL", "to")
        msg_content = readConfig.ReadConfig().get_config("EMAIL", "content")
        # 获取html文件内容
        f = open(get_path.getPath() + "result/report.html", "rb")
        send_html = f.read()
        f.close()

        msg = MIMEMultipart()
        msg.attach(MIMEText(send_html, 'html', 'utf-8'))
        msg['from'] = readConfig.ReadConfig().get_config("EMAIL", "from")
        msg['Subject'] = readConfig.ReadConfig().get_config("EMAIL", "subject")
        msg['To'] = readConfig.ReadConfig().get_config("EMAIL", "to")

        # 加附件
        # send_file=open(get_path.getPath()+"result/report.html","rb").read()
        att = MIMEText(send_html, 'HTML', 'UTF-8')
        att['Content-Type'] = 'application/octet-stream'
        att.add_header('Content-Disposition', 'attachment', filename="附件-自动化测试报告")
        msg.attach(att)

        try:
            s = smtplib.SMTP_SSL(readConfig.ReadConfig().get_config("EMAIL", "sendserver"),
                                 readConfig.ReadConfig().get_config("EMAIL", "port"))
            s.login(msg_from, msg_password)
            s.sendmail(msg_from, msg_to, msg.as_string())
            logs.info("=======邮件发送成功======")
            print("发送成功")
        except smtplib.SMTPException as e:
            logs.error("=======邮件发送失败======" + e)
            print(e)
        finally:
            s.quit()



if __name__=='__main__':
    SendEmail.sendemail()

