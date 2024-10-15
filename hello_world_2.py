greeting = "Hello"
firstName = "Jack"
lastName = "White"
exclamation_sign = "!"
white_space = " "
print(greeting + white_space + firstName + " " + lastName + exclamation_sign)
long_string = "This is the long string"
print(long_string)
whole_sentence = (greeting + white_space + firstName + " "
                  + lastName + exclamation_sign)
print(whole_sentence)
# Escaping
some_string = "I'm a programmer"
some_string2 = 'I\'m a programmer'
print(some_string)
print(some_string2)

another_string = 'I want to learn "Python" '
another_string2 = "I want to learn \"Python\" "
print(another_string)
print(another_string2)

string_with_new_lines = "Hello! \n My name is John "
print(string_with_new_lines)
string_with_new_lines2 = "Hello! \n  \rMy name is John "
print(string_with_new_lines2)

numbers = "1\t23456"
print(numbers)
