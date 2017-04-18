import string
import re

with open("ClassiciUnfilled.html", "r") as f:
    classiciUnfilled = f.read()

NOTE = open("Note.html", "r")
note= NOTE.read()
NOTE.close()

def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index(last, start )
        return s[start:end]
    except ValueError:
        return ""

note_scheme = "</a><a href=\"index.html"
totalNoteNumber = classiciUnfilled.count(note_scheme) / 2

ClassiciFinal = classiciUnfilled

#pipe to classici with Footnotes

listOfClassiciConcepts = []

#adds Classici footnoteconcepts to list
x = 1
while x <= totalNoteNumber:
    numberOfTheLink = x
    classici_foot_begin_ID = "</a><a href=\"index.html#_textNo=" + str(numberOfTheLink) + "\">"
    classici_foot_end = "</a><br />"

    classici_foot_note_concept = find_between(ClassiciFinal, classici_foot_begin_ID, classici_foot_end)
    t = classici_foot_note_concept
    listOfClassiciConcepts.append(classici_foot_note_concept)
    x += 1

noteEnumerated = note
listOfFootnoteConcepts = []
listOfFootnoteTexts= []

#note to enumerated output.
z = 1
while z <= totalNoteNumber:
    noteEnumerated = noteEnumerated.replace("<p align=\"\">", "The " + str(z) +"th-Link",1)
    noteEnumerated = noteEnumerated.replace("title\">", "title" + str(z) + "\">",1)
    z = int(z)
    z +=1

y = 1
while y <= totalNoteNumber:
    foot_note_text = find_between(noteEnumerated, "The " + str(y) +"th-Link", "</p>" )
    listOfFootnoteTexts.append(foot_note_text)
    listOfFootnoteConcepts.append(find_between(noteEnumerated, "title" + str(y) + "\">", "<\h1>" )) #TODO for Control
    y += 1

numberOfTheLink = 0
while numberOfTheLink < totalNoteNumber:
    foot_note_text = listOfFootnoteTexts[int(numberOfTheLink)]
    numberOfTheLink += 1
    classici_foot_note_ID = "textNo=" + str(numberOfTheLink) + "\">" + listOfClassiciConcepts[numberOfTheLink - 1] + "</a><br />"
    ClassiciFinal = ClassiciFinal.replace(classici_foot_note_ID, classici_foot_note_ID + foot_note_text, 1)
    ClassiciFinal = ClassiciFinal.replace("In der Fussnote", "")
    concept_classic = listOfClassiciConcepts[int(numberOfTheLink-1)]#TODO for control
    note_concept = listOfFootnoteConcepts[int(numberOfTheLink-1)]
  #  if not(note_concept  == concept_classic):
   #     print note_concept + " (Classici) vs. " + concept_classic

#for i in listOfClassiciConcepts: # warum dieser output?
 #   print [i]

#print "check above"

print ClassiciFinal


