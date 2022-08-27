# # ? Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# def func(string):
#     empty = []
#     [empty.append(1) if int(i) > 5 else empty.append(0) for i in string]
#     return "".join(str(i) for i in empty)

# func("123456789")

#  ! ===============================================

# # ? Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

# vovels = ['a', 'e', 'i', 'o', 'u']

# def remove_vovels(string):
#     return "".join(i for i in string if i not in vovels)

# remove_vovels("hello mother fucker")


#  ! ===============================================

# ? Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# def get_sum(a,b):
#     if a == b:
#         return a
#     x = sum(range(a,b+1)) if a < b else sum(range(b,a+1))
#     return x
# get_sum(19,9)


#  ! ===============================================


# def dublicate(arr) :
#     empty = []
#     second = []
#     for i in arr : 
#         empty.append(int(i))
#         arr.remove(int(i))
#         if (int(i) in arr ) and (int(i) in empty):
#             second.append(int(i))
        
        
#     return second

# dublicate([1,1,2,2,3,9,9,10,"10"])     

#  ! ===============================================


# ? Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL), multiplied by the integer at the last inde


def even_last(arr): 
    total = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            total += arr[i]
        elif len(arr) == 0:
            total = 0
        elif i == 0:
            total += arr[0]
            
    if total > 0:
        return total * arr[-1]
    else:
        return 0


#  ? ===============================================

def combine(*args) : 
    my_new = {}
    for i in args:
        for j in i.keys():
            if j in my_new.keys():
                my_new[j] += i[j]
            else :
                my_new[j] = i[j]
    return my_new

print(combine({"a": 10,"b": 20, "c": 30} , {"a": 3, "c": 6, "d": 3 , "b": 10}))



# ? ==============================================


# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

def get_middle(s):
    empty = ""
    for i in s:
        if len(s) % 2  == 0:
            empty += s[int(len(s) / 2 -1) ] + s[int(len(s) / 2 )]
            
        elif len(s) % 2 == 1:
            empty += s[int(len(s) / 2  )]
        
        elif len(s) ==1:
            empty += s[0]
            
        return empty
get_middle("testing")
