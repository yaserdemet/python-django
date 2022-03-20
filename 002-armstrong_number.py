number = input("pls enter a number : ")
x = list(number)
digit  = len(x)
a = 0
for i in x :
    a += (int(i) ** digit)
if str(a) == number :
    print(" {} is a armstrong number".format(number))
elif str(a) != number:
    print("{} is  not a armstrong number".format(number))
else :
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

SOLUTION  JUST FOR 3 DIGITS NUMBERS :

x = int(input("pls enter 3 digit number : "))
a = (x) // 100
b = (x) // 10 % 10
c = (x) % 10

if (a ** 3 + b ** 3 + c ** 3) == (x):

    print("your number is astronout number ")


elif int(x) < 0 :

    print("do not use negatif number")


else:
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")

