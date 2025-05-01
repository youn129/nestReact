import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
 
msg = MIMEMultipart('alternative')
내용 = """
<h4>황비!</h4>
<button>I Love U</button>
"""

part1 = MIMEText(내용, "html")
msg.attach(part1)
 
msg['Subject'] ="비비❤️"
msg['From'] = 'wjddbstlr11@naver.com'
msg['To'] = 'sunnysss@naver.com'
print(msg.as_string())
 
s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
s.starttls() #TLS 보안 처리
s.login( 'wjddbstlr11' , 'Kk90109324' ) #네이버로그인
s.sendmail( 'wjddbstlr11@naver.com', 'sunnysss@naver.com', msg.as_string() )
s.close()