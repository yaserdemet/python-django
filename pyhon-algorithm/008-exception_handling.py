#Using while loop and full try . except block,At this time, in addition to the previous program,
#Give the user three chances to enter an input, and whenever the user raises an exception, decrease the counter by 1 displaying 
#that "<warning message>, you have n right left. Try again!" If no exception raise, display a message : "Congrats! You've entered a valid input."
#In all circumstances, display a message : "Our fruits are always fresh!"

fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]
counter = 3
while counter > 0 : 
    try:
        print("u have {} rights.".format(counter))
        index = int(input("pick a index number"))
        print("your favourite fruit is" , fruits[index])
        
    except IndexError :
        counter -= 1
        print("Index error raised. You have {} right left.".format(counter))
    
    except ValueError :
        counter -= 1
        print(f"Value error rasied. You have {counter} right left")
        
    else : 
        print("Congrats ! u have entered a valid input.")
        
        break
    finally :
        print("Our fruit always fresh")
