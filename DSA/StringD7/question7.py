'''
Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Input: s = "ab#c", t = "ad#c"

Output: true

Explanation: Both s and t become "ac".

'''


def textEditor(s,t):


    def process_string(string):

        result = []

        for char in string:

            if char != '#':
                result.append(char)
            elif result:
                result.pop()
        
        return result
    


    return process_string(s) == process_string(t)



s = input("Enter the first string: ")

t = input("Enter the second string: ")

result = textEditor(s,t)

print(result)