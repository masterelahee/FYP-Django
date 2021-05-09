import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
import time
import pathlib
import dropbox
import re
import os



def thisonetrust(scan_id,email,fixurl,url):
    ## HARDCODED FILE PATH, CHANGE THIS LATER
    # the source file
    # folder = os.path.join(BASE_DIR, '')
    print(scan_id)
    print(email)
    folder = pathlib.Path("./myapp/reports")    # located in this folder
    folder2=pathlib.Path("./myapp/pdf_reports")
    print(folder)
    scanID = scan_id
    print(scanID)
    filename = scanID + ".html.zip"         # file name
    filename2=fixurl+".pdf"
    filepath = folder / filename  # path object, defining the file
    filepath2 = folder2 / filename2 #pdf version
    print(filepath)

    # target location in Dropbox
    target = "/"              # the target folder
    targetfile = target + filename   # the target path and file name
    targetfile2 = target + filename2

    # Create a dropbox object using an API v2 key
    d = dropbox.Dropbox("ClkPn4pV_5sAAAAAAAAAAUm4ft1qOk4VNd77wioArPu7WbFxQBb1f7-UKZQPfaRB")
    print(d.users_get_current_account())
    # open the file and upload it
    try:
        with filepath.open("rb") as f:
        # upload gives you metadata about the file
        # we want to overwite any previous version of the file
            
            meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
            print(meta)
                #open pdf and upload it
        with filepath2.open("rb") as f:
            # upload gives you metadata about the file
            # we want to overwite any previous version of the file
            meta2 = d.files_upload(f.read(), targetfile2, mode=dropbox.files.WriteMode("overwrite"))
        # create a shared link
        link = d.sharing_create_shared_link(targetfile)
        link2 = d.sharing_create_shared_link(targetfile2)

        # url which can be shared
        dropbox_url = link.url
        dropbox_url2 = link2.url

        print(dropbox_url)

        #take scan id, call mediafire uploader and then get dl link to email to user
        time.sleep(10)
        # Create a multipart message
        msg = MIMEMultipart()
        body_part = MIMEText('Your report is ready, here is the link to download it: ' + dropbox_url + 'and here is the PDF report link: ' + dropbox_url2, 'plain')
        msg['Subject'] = 'TheBoyes web scanner scan report'
        msg['From'] = 'fypemail@yahoo.com' #change this to email used by us
        msg['To'] = email #change this to email input from user
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

    except IOError:
        print("File not accessible")