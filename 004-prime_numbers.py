def  asal_Sayı(sayı1 , sayı2):              #function for getting prime numbers among 2 numbers
    for i in range (sayı1 , sayı2+1):
        if i > 1 : 
            for j in range (2,i):
                if i % j == 0 :
                    break
            else:
                print(i)
        
asal_Sayı(20,30)
