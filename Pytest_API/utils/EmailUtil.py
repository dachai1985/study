import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from Pytest_API.config.Conf import ConfigYaml

# 初始化邮件信息
class SendEmail:
    def __init__(self, smtp_server, email_from, password,email_to, email_subject, email_content,files=None):
        self.smtp_server = smtp_server
        self.email_from = email_from
        self.password = password
        self.email_to = email_to
        self.email_subject = email_subject
        self.email_content = email_content
        self.files = files

    # 发送邮件
    def send_email(self):
        try:
            # 构建邮件内容
            msg = MIMEMultipart()
            msg['From'] = self.email_from
            msg['To'] = self.email_to
            msg['Subject'] = self.email_subject
            # 邮件正文
            msg.attach(MIMEText(self.email_content, 'plain', 'utf-8'))
            # 添加附件
            if self.files:
                for file in self.files:
                    with open(file, 'rb') as f:
                        attach = MIMEText(f.read(), 'base64', 'utf-8')
                        attach["Content-Type"] = 'application/octet-stream'
                        attach["Content-Disposition"] = 'attachment; filename="{}"'.format(os.path.basename(file))
                        msg.attach(attach)

            # 连接到SMTP服务器
            smtp_obj = smtplib.SMTP_SSL(self.smtp_server, 25)
            # 登录邮箱
            smtp_obj.login(self.email_from, self.password)

            # 发送邮件
            smtp_obj.sendmail(self.email_from, self.email_to, msg.as_string())
            # 关闭连接
            smtp_obj.quit()
            print("邮件发送成功")
        except Exception as e:
            print("邮件发送失败：", e)

# 测试
if __name__ == '__main__':
    email_info = ConfigYaml().get_email_info()
    smtp_server = email_info['smtp_server']
    email_from = email_info['email_from']
    password = email_info['password']
    email_to = email_info['email_to']
    email_util = SendEmail(smtp_server, email_from, password, email_to, '测试邮件', '测试邮件内容')
    email_util.send_email()
