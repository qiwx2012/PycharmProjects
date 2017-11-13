import smtplib
from email.mime.text import MIMEText
_user = "476364523@qq.com"
_pwd  = "khphmwkatltxbicj"
_to   = "675363987@qq.com"

msg = MIMEText("fdsdfasdfasdfasdfasfas")
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print ("Success!")
except smtplib.SMTPException:
    print ("Falied,%s"%('dfdfd'))