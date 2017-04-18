# replaces old links to glossario' with new  glossariolinks (CMS)
import fileinput

with open("oldNoteLinks.html", "rt") as fin:

    newLink = "../../glossario/index.html#faq_";
    oldLink = "http://web07.campus.fu-berlin.de/sibawaih/rom/popup/glossary/";
    htmlEndl = ".html\""

    contents = fin.read()
    if (contents.count(oldLink) != contents.count(htmlEndl + ">")):
        print ("Be carefull, links may get damaged!")
    print (contents.count(htmlEndl + ">"))
    print (contents.count(oldLink))

replacements = {oldLink : newLink, htmlEndl : "\""}

with open('oldNoteLinks.html') as infile, open('newNoteLinks.html', 'w') as outfile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        outfile.write(line)

#TODO print message if other "http://web07.campus.fu-berlin.de/sibawaih/" occurence found
