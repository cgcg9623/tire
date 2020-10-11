import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


# 보내는 사람 정보
me = "cgcg9623@gmail.com"
my_password = "joyjoy88!"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
emails = ["cgs9623@nate.com", "chlrbtjs122@naver.com"]

for you in emails:

    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "뉴스공유"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "ㅎㅇㅎㅇ"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 메일 보내고 서버 끄기
    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    msg.attach(part)
    s.sendmail(me, you, msg.as_string())
s.quit()