# python 3


from celery import Celery
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import time

app = Celery('test', broker='pyamqp://guest@localhost//')

'''
to start delery worker : celery -A celery_test worker --loglevel=info
to start rabbitmq : first export path 
            export PATH=$PATH:/usr/local/sbin (or put into .bash_profile)
            cmd : rabbitmq-server
            url : http://localhost:15672/
            default user, pass : guest, guest
'''

@app.task
def send_email(subject, text_data = None, file_name = None):
    to_address = 'kumar.amardip8@gmail.com'
    import pdb;pdb.set_trace()
    #to_address = 'amardip.kumar@3pillarglobal.com, ankit.tyagi@3pillarglobal.com'
    body_mail_text =  text_data
    fromaddr = "amardip811@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = to_address
    msg['Subject'] = subject
    if file_name:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(file_name, "rb").read())
            # Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="file_comare.csv"')
            msg.attach(part)
            msg.attach(MIMEText("Hi,\n Please get the attachment."))
    else:
        body = "hi"
        msg.attach(MIMEText(body, 'html'))
    text = msg.as_string()
    try:
        s_mail=smtplib.SMTP(host='smtp.gmail.com', port=587)
        s_mail.ehlo()
        s_mail.starttls()
        s_mail.ehlo()
        s_mail.login('amardip811@gmail.com', 'Vicky@1234')
        s_mail.sendmail(fromaddr, to_address.split(','), text)
        return "done"
    except Exception as E:
        print ("no send")
        return R

if __name__ == '__main__':
    send_email("helo")
    print ("End")