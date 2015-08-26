import urllib2
from bs4 import BeautifulSoup
from CourseNode import CourseNode

webUrl = 'http://catalog.calpoly.edu'
testPage = BeautifulSoup(urllib2.urlopen(webUrl + "/coursesaz").read(), "html.parser");
testPage.prettify();

#print 'received webpage info from \"' + testPage.title.string + '\"';
#print 'list of major programs avalilable: '

table = testPage.find_all('a', class_="sitemaplink");

#print "going to " + table[0].get("href");

#aero = BeautifulSoup(urllib2.urlopen(webUrl + table[0].get("href")).read(), "html.parser");
#areocourses = aero.find_all(class_="courseblock");

aeroTest = BeautifulSoup(open("examplecourseblock.html"), "html.parser");



testNode = CourseNode();
testNode.createNode(aeroTest);

print testNode;

