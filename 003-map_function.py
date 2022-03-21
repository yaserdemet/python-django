letter1 = ["o" , "s" , "t" , "t"]
letter2 = ["n" ,"i" , "e" , "w"]
letter3 = ["e", "x" , "n" ,"o"]
x = map(lambda x, y, z : x+y+z , letter1 , letter2 , letter3)
print(*x)
