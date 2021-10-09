import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(user_name, email, reset_code):
    '''
    send reset code email
    '''
    # set host and receiver
    host_name = "smtp.gmail.com"
    host_port = 465
    sender_email = '3900forgenius@gmail.com'
    sender_password = 'forGenius100'
    receivers = [email]

    # email info
    Title = 'Reset Code Sent!'
    subject = 'Here is your Reset Code ' + reset_code

    message = MIMEText(subject, 'plain', 'utf-8')
    message['From'] = Header("3900forGenius", 'utf-8')
    message['To'] =  Header(user_name, 'utf-8')
    message['Subject'] = Header(Title, 'utf-8')

    server = smtplib.SMTP_SSL(host_name, host_port)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email,receivers,message.as_string())
    server.quit()
