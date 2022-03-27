import random  
x = random.randint(1,100)

right_guess = 5

while right_guess > 0:
    
    guess = int(input("guess a number"))
    
    print("sayı giriniz : " , guess)
    right_guess -= 1
    
    if guess < x:
        print("sayıyı yükselt")
        
    elif guess > x:
        print("sayıyı düşür")
        
    elif x == guess:
        print("tahminiz doğru")
    
if right_guess < 1 :
    print("hakkınız bitmiştir")
