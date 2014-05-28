print("         Type a Quadratic Formula (ax^2+bx+c)")
print("                  =====================================")
print("                          But first we Have to do it the hard way")
print("  " + "Do you Agree?")
ans = "yes"
answer = input()
if answer == ans :
   print("Ok ,cool")
else :
   print("alas!!") 
   exit()
for i in ["========","=========","========"]:
    print(i)
   
print("............let's go ...............")
print("type the (-a- of ax ) number:")
a = float(input())
print("type the 'b' of bx number")
b = float(input())
print("Now , type the 'c' and to get the to solution if c=0 type 0")
c = float(input())
op1 = b**2-4*a*c
if op1 > 0 : 
   print("Delta equal = " + str(op1))
elif op1 == 0 : 
   print("The solution is :" + str(-1*b/2*a))
   exit()
else :
   op2 = (-1*b - op1**(1/2))/2*a
   op3= (-1*b + op1**(1/2))/2*a
   print("Delta is < 0  it has no Solutions in the Real numbers")
   print("Do you want Solution on Complex Numbers ?")
answer = input()
an = "yes"
if answer == an :
   print("First solution is : " + str(op2))
   print("Second solution is : " + str(op3))
else : 
   exit()
