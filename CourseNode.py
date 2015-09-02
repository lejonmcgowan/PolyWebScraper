import string
from bs4 import BeautifulSoup


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
        filter(lambda x: x in string.printable, courseblocktitle.p.string)
        courseblocktitle = courseblocktitle.p.string.encode('utf-8').strip().split();
        self.courseMajor = courseblocktitle[0];
        print courseblocktitle  # .rpartition(". ")[1];
        self.courseNumber = int(courseblocktitle[1].rpartition(". ")[1]);
        self.courseName = " ".join(courseblocktitle[2:]);

        self.numUnits = int(soupString.find('p', class_="courseblockhours").string.split()[0]);

        courseextendedwrap = soupString.find('div', class_="courseextendedwrap");
        wrapParagraphs = courseextendedwrap.find_all('p');
        self.termsOffered = wrapParagraphs[0].string.rpartition(": ")[1];
        for hyperlink in soupString.find_all('a', class_='bubblelink code'):
            self.prerequisites.append(hyperlink.string);

        self.description = soupString.find('div', class_="courseblockdesc");

    def __str__(self):
        printList = [];
        printList.append(self.courseMajor + " " + str(self.courseNumber) + ": " + self.courseName);
        printList.apprend("");
        printList.append(self.description);
        return "\n".join(printList);
