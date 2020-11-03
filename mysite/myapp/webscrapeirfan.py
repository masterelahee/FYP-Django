import mechanize
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import html2text
import requests
#import cloudscraper
class linkergetter(web):
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
    # Browser
    br = mechanize.Browser()

    #cloudscraper

if __name__ == "__main__":
    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    br.addheaders = [('User-agent', 'Chrome')]

    # scraper = cloudscraper.create_scraper()
    # print scraper.get("https://tryhackus-theboyes.ml").text

    thelink=web
    # The site we will navigate into, handling it's session
    br.open(thelink)

    # View available forms
    for f in br.forms():
        print (f)

    # Select the second (index one) form (the first form is a search query box)
    br.select_form(nr=0)

    # User credentials
    br.form['email'] = 'admin@admin.com'
    br.form['password'] = 'password'

    # Login
    br.submit()

    # getpage= requests.get('https://tryhackus-theboyes.ml/admin')

    # getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

    # all_links= getpage_soup.findAll('a')

    # for link in all_links:
    #     print (link)
    # print(br.open('https://tryhackus-theboyes.ml/admin/clients').read())



    br.set_cookiejar(cj)
    print(cj)

    visit(br,thelink)
    bar=visited_links.copy()
    for e in bar:
        visit(br,e)

    print(list(visited_links))
    return list(visited_links)
