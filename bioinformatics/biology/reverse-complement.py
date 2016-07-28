s="ATTGCGATGCTA"
z={}
for i in range(len(s)):
 if (s[i]=="A"):
  z[i]="U"
 if (s[i]=="C"):
  z[i]="G"
 if (s[i]=="G"):
  z[i]="C"
 if (s[i]=="T"):
  z[i]="A"
print s
for i in range(len(z)):
 print z[i],
