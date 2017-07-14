from urllib.parse import urlencode, urlparse, parse_qs
import bs4 as bs
import urllib.request

from lxml.html import fromstring
from requests import get

toquery = input("Enter a research subject: ")

raw = get("https://www.google.com/search?q=" + toquery).text
page = fromstring(raw)

for result in page.cssselect(".r a"):
    url = result.get("href")
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
    src = urllib.request.urlopen(url[0]).read()
    soup = bs.BeautifulSoup(src, 'lxml')
    with open(toquery + ".txt", "a") as fh:
    	for paragraph in soup.find_all('p'):
    		fh.write(paragraph.text)
