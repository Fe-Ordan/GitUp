print(" This is a small tool That helps you  know The Value of a resistor")
print(" What you have to Do is to Give the Color shown on the Resistor")
print("    from Left to right # in lower case # ")
print(" type the first color : ")
color1 = input()
print(" type the next Color (remember from left to right) : ")
color2 = input()
print(" Type Color Number 3 : ")
color3 = input()
black = 0
green = 5
brown = 1
red = 2
orange = 3
yellow = 4
blue = 6
violet = 7
grey = 8 
white = 9
list = {'black':'0','green':'5','yellow':'4','brown':'1','orange':'3','red':'2','blue':'6','violet':'7\
','grey':'8','white':'9'}
e  = str(list[color1]) + str(list[color2]) + '0'*int(list[color3])
print("the resistance is : " + e + "ohms")