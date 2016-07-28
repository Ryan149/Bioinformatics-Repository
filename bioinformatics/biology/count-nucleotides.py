s="ATTCGATCT"
a=0
c=0
g=0
t=0
for i in range(len(s)):
 if (s[i]=="A"):
  a=a+1
 if (s[i]=="C"):
  c=c+1
 if (s[i]=="G"):
  g=g+1
 if (s[i]=="T"):
  t=t+1
z=a+c+g+t
print "The sequence of DNA", s, "has", z, "nucleotides."
print "There are", a, "A's in the string."
print "There are", c, "C's in the string."
print "There are", g, "G's in the string."
print "There are", t, "T's in the string."
print "A makes up", float(a)*100/float(z), "percent of the string."
print "C makes up", float(c)*100/float(z), "percent of the string."
print "G makes up", float(g)*100/float(z), "percent of the string."
print "T makes up", float(t)*100/float(z), "percent of the string."
