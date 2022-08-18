#Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# def func(string):
#     empty = []
#     [empty.append(1) if int(i) > 5 else empty.append(0) for i in string]
#     return "".join(str(i) for i in empty)

# func("123456789")



# ? Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

vovels = ['a', 'e', 'i', 'o', 'u']

def remove_vovels(string):
    return "".join(i for i in string if i not in vovels)

remove_vovels("hello mother fucker")