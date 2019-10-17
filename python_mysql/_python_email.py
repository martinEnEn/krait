import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendmail(cwIsOpen,krestecIsOpen,motorIsOpen):
    # 第三方 SMTP 服务
    mail_host = "smtp.exmail.qq.com"  #设置服务器
    mail_user = "ruye.ma@vanmilk.com"    #用户名
    mail_pass = ""   #密码
    sender = 'ruye.ma@vanmilk.com'
    receivers = ['mandalahua@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    text = 'CW是否打开:'+cwIsOpen+"\nkrestec是否打开:"+krestecIsOpen+"\nmotor是否打开:"+motorIsOpen
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("Vista开关监控", 'utf-8')
    message['To'] = Header("adm", 'utf-8')

    subject = 'Vista开关监控'
    message['Subject'] = Header(subject, 'utf-8')


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")