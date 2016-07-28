import re
line={}
line['1']="my name is 433-33-3456"
line['2']="433-33-3456 is not a good number"
line['3']="433-33-3456"
line['4']="aaac dc dd d cdc"
line['5']="123 22 2222"
line['6']="123a22-34567"
line['7']="3474-22-2222"
line['8']="123-11-1111"
line['9']="999-10-1111"
line['10']="222-7.-3454"
line['11']="22 2 2 2 22 323232 2 3 23 2 32 323 23  23 23 23 02-232-2323"
for i in range(0,12):
 match=re.findall(\A\d{3}-\d{2}-\d{4}\Z,line[i])
 if match:
  print match
