condition='false'
login={}
f=open('/tmp/loginInfo','r')
l=f.readlines()
for i in range(len(l)):
 s=l[i].split()
 print s
 login[s[0]]=s[1]
while (condition=='false'):
 inputusername=raw_input('Enter your username:')
 inputpassword=raw_input('Enter your password:')
 if inputusername in login:
  condition='true'
  if (inputpassword==login[inputusername]):
   print 'you are logged in'
  else:
   condition='false'
   print 'password does not exist'
 else: 
  print 'username does not exist' 
