# Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

# A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard).
# The word will always be a string consisting of only letters from a to z.
# Write a program which returns True if it's a comfortable word or False otherwise.

x = set(input('Pls enter your word: '))
left_hand = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v'}
right_hand= {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm'}
print((x - left_hand != set()) and (x - right_hand != set()))
