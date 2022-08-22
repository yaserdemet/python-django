# # ? Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# def func(string):
#     empty = []
#     [empty.append(1) if int(i) > 5 else empty.append(0) for i in string]
#     return "".join(str(i) for i in empty)

# func("123456789")



# # ? Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

# vovels = ['a', 'e', 'i', 'o', 'u']

# def remove_vovels(string):
#     return "".join(i for i in string if i not in vovels)

# remove_vovels("hello mother fucker")




# ? Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

def get_sum(a,b):
    if a == b:
        return a
    x = sum(range(a,b+1)) if a < b else sum(range(b,a+1))
    return x
get_sum(19,9)