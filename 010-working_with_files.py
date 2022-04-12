# working with files.
with open("rumi.txt" , "r" , encoding="utf-8") as file:
    print(file.readline())
    print(file.readline())      #satır satır okuma


with open("rumi.txt" , "r" , encoding="utf-8") as file:
    print(file.read(21))    #21 karakter okunur
    print(file.tell())
    file.seek(0)        #seek(0) ile dosyanın başına gider
    print(file.tell())



with open("fishes.txt", "r") as file:
    print(file.readlines()) # dosyanın her satırını liste şeklinde okur.



with open("fishes.txt", "r") as file:
    x = file.readlines()
    for i in x :
        print(i)


with open("dummy_file.txt" , "w" , encoding= "utf-8") as file:
    
    file.write("this is first line of my text.")
with open("dummy_file.txt" , "r" , encoding= "utf-8") as file:
    print(file.read())  


fruits = ['Banana', 'Orange', 'Apple', 'Strawberry', 'Cherry']
with open("fruit.txt" , "w" , encoding= "utf-8") as file:
    for i in fruits:
        file.write(i + "\n")
        
with open("fruit.txt" , "r") as file:
        
    print(file.read())


counter = 0
with open("istiklal.txt" , "w" , encoding = "utf-8") as mozz:
    for i in lines:
        counter += 1
        if counter % 4 == 0:
            mozz.write(i + "\n")
        else : 
            mozz.write(i)
with open("istiklal.txt" , "r" , encoding="utf-8") as mozz:
    print(mozz.read())
