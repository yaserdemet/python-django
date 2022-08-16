#Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def func(string):
    empty = []
    [empty.append(1) if int(i) > 5 else empty.append(0) for i in string]
    return "".join(str(i) for i in empty)

func("123456789")