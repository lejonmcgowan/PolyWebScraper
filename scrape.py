import urllib2
from bs4 import BeautifulSoup
webUrl = 'http://catalog.calpoly.edu/coursesaz/'
testPage = BeautifulSoup(urllib2.urlopen(webUrl).read());
testPage.prettify();

print 'received webpage info from \"' + testPage.title.string + '\"';
print 'list of major programs avalilable: '

table = testPage.find_all('a', class_="sitemaplink");

aeroTest = BeautifulSoup(webUrl + table[0].get('href'))

