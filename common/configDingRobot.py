import requests
import json
from common.log import logs

# 钉钉机器人Webhook地址，发送内容关键字必须包含"测试""报告""结果"
webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=542bc33b5ad85760478b86fc7d22d3c5baae006a5c30d5461b87a8a093af57ea'

# 构造请求头
headers = {
    'Content-Type': 'application/json'
}

# 构造请求体
data = {
    "msgtype": "text",
    "text": {
        "content": "这是一条来自Python脚本的钉钉测试报告消息！"
    }
}

# 发送请求
response = requests.post(webhook_url, headers=headers, data=json.dumps(data))

# 检查响应
if response.status_code == 200:
    print('消息发送成功！')
    logs.info("推送钉钉消息成功")
else:
    print('消息发送失败，错误码：', response.status_code)
    print('错误信息：', response.text)
    logs.info("推送钉钉消息失败，原因：%s"%response.text)
