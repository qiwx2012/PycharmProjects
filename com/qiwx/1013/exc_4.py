import re
line ='Cats are smarter than dogs'
machObj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if machObj:
    print("group",machObj.group(0))
    print("group1",machObj.group(1))
    print("group2",machObj.group(2))
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))

