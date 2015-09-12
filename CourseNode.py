import string
from bs4 import BeautifulSoup


def getCourseFromUnicode(unicodeCourse):
    field = str(filter(lambda x: x in string.ascii_letters, unicodeCourse))
    number = int(filter(lambda x: x in string.digits, unicodeCourse))
    return field + " " + str(number)



class CourseNode(object):
    courseMajor = "";
    courseNumber = -1;
    courseName = "";
    numUnits = -1;
    termsOffered = [];
    prerequisites = [];
    reccommended = [];
    description = "";

    def createNode(self, soupString):  # soupNode should be a navigatable string
        # print soupString;
        courseblocktitle = soupString.find("div", class_="courseblocktitle")
        courseblocktitle = courseblocktitle.p.string.encode('utf-8').strip().split();

        self.courseMajor = filter(lambda x: x in string.ascii_letters, courseblocktitle[0])
        courseblocktitle[0] = filter(lambda x: x in string.digits,courseblocktitle[0])  # this should get the number out of the string

        self.courseNumber = int(courseblocktitle[0]);
        self.courseName = " ".join(courseblocktitle[1:]);

        self.numUnits = int(soupString.find('div', class_="courseblockhours").string.split()[0]);

        courseextendedwrap = soupString.find('div', class_="courseextendedwrap");

        wrapParagraphs = courseextendedwrap.find_all('p');
        self.termsOffered = wrapParagraphs[0].string.rpartition(": ")[1]
        for hyperlink in soupString.find_all('a', class_='bubblelink code'):
            self.prerequisites.append(getCourseFromUnicode(hyperlink.string))

        self.description = soupString.find('div', class_="courseblockdesc").p.string
        self.description = filter(lambda x: x in string.printable, self.description)

    def __str__(self):
        printList = []
        printList.append(self.courseMajor + " " + str(self.courseNumber) + ": " + self.courseName)
        printList.append(self.description)
        printList.append("Prerequisites: " + str(self.prerequisites))
        return "\n".join(printList)
