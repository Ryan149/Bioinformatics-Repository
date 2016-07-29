condition1="false"
condition2="false"
truelogin="U53rNam3"
truepassword="pa55W0rd"
while condition1=="false":
 login = raw_input('Enter your username:')
 if (login==truelogin):
  break
  condition1="true"
 if (login!=truelogin):
  print "You have entered the incorrect username"
  condition1="false"
while condition2=="false":
  password = raw_input('Enter your password:')
  if (password==truepassword):
   break
   condition1="true"
  if (password!=truepassword):
   print "You have entered the incorrect password"
   condition1="false"
print "Good job! You logged in!"
