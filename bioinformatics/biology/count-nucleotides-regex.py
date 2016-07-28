import re

s="ATTCGATCT"

s= re.sub('A',' ',s)
print s
print len(s)-s.count(' ')
