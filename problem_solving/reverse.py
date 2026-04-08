#Reverse words in a string

def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

# get user input
user_input = input("Enter a string: ")
# reverse the words in the input string
reversed_string = reverse_words(user_input)
# print the reversed string
print("Reversed string:", reversed_string)

