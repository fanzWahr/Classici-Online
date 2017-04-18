# iterates though html code and replaces old url with new references (to a footer which has to be created/text imported)
from __future__ import print_function
import string

OldClassici = open("Classici.html", "r")
modifiedClassici = OldClassici.read()
OldClassici.close()

OldLinkSubstring = "<a href=\"http://web07.campus.fu-berlin.de/sibawaih/rom/popup/Testo05/explain.html?LO=Testo05&amp;"

currentLinkNumber = 1
totalLinknumber = modifiedClassici.count(OldLinkSubstring)


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

for i in range(totalLinknumber):
    addedID = "_textNo=" + str(currentLinkNumber)
    footnoteID = "_linkNo=" + str(currentLinkNumber)

    #create new Reference for every Link
    NewUrlFirstSubstring = "<a name=\"" + str(addedID) + "\">"
    NewUrlSecondSubstring = "</a><a href=\"index.html#_"
    NewReferences = NewUrlFirstSubstring + NewUrlSecondSubstring

    modifiedClassici = string.replace(modifiedClassici, OldLinkSubstring, NewReferences,1)

    currentConcept= find_between(modifiedClassici, footnoteID + "\">", "</a>")

    #insert footnote
    footFrameBegin= "<p>"
    footFrameEnd= "</p>"
    footConcept = currentConcept
    content = "In der Fussnote"


    FootPartOne = "<a name=\"" + str(footnoteID) + "\">"
    FootPartTwo = "</a><a href=\"index.html#" + addedID + "\">" + footConcept + "</a>"

    FootnoteReference = footFrameBegin + str(currentLinkNumber) + " " + FootPartOne + FootPartTwo + "<br>" + content + footFrameEnd

    modifiedClassici += FootnoteReference

    currentLinkNumber += 1

print(modifiedClassici)

#f1=open('ClassiciUnfilled.html', 'w+')
#f1.write('This is a test')


