word={}
word['one']="banana"
word['two']="banana"
if word['two'] in word['one']:
 print "The word",word['two'],"is in the word",word['one']
elif word['one'] in word['two']:
 print "The word", word['one'],"is in the word",word['two']
else:
 print "The word",word['two'],"is not in the word",word['one']
