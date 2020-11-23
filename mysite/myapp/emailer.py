import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
from mediafire import (MediaFireApi, MediaFireUploader)
import time

def thisonetrust(scan_id):
    api = MediaFireApi()
    uploader = MediaFireUploader(api)
    session = api.user_get_session_token(email='fypemail@yahoo.com', password='iamusingastrongpassword',app_id='42511')

    # API client does not know about the token
    # until explicitly told about it:
    api.session = session
    # scan_id = 'wefwefwefwef' #replace this part with the scanner id from the arachni scanner  

    fd = open('D:/Desktop/FYP/FYP-Django/mysite/' + scan_id + '.html.zip', 'rb')
    time.sleep(10)
    result = uploader.upload(fd, scan_id + '.html.zip', folder_key='tje4eo1vl6m83') #returns a json object
    time.sleep(10)
    print(api.file_get_info(result.quickkey))
    result_object = api.file_get_info(result.quickkey)
    print(result_object["file_info"]["filename"])
    print(result_object["file_info"]["links"]["normal_download"]) #returns the download link

    mf_link = result_object["file_info"]["links"]["normal_download"]

    #take scan id, call mediafire uploader and then get dl link to email to user

    # Create a multipart message
    msg = MIMEMultipart()
    body_part = MIMEText('Your report is ready, here is the link to download it: ' + mf_link, 'plain')
    msg['Subject'] = 'Python scan report'
    msg['From'] = 'fypemail@yahoo.com'
    msg['To'] = 'irfanelahee6@gmail.com'
    # Add body to email
    msg.attach(body_part)

    # Create SMTP object
    session = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    session.starttls() #enable security
    # Login to the server
    session.login('fypemail@yahoo.com', 'driqnfsefylmmlwq')

    # Convert the message to a string and send it
    session.sendmail(msg['From'], msg['To'], msg.as_string())
    print("Mail sent")
    session.quit() #closes email session after done

    # sender_address = 'fypemail@yahoo.com'
    # sender_pass = 'driqnfsefylmmlwq'
    # receiver_address = 'jasonling9199@gmail.com'