# Write a program which can filter even numbers in a list by using
# filter function The list is: [1,2,3,4,5,6,7,8,9,10].

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(evenNumbers)


# Write a program which can map() to make a list whose 
# elements are square of elements in [1,2,3,4,5,6,7,8,9,10]

li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print(squaredNumbers)


# Write a program which can map() and filter() 
# to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]


li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)
