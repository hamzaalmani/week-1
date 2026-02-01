

# add code below ...

def palindrome(word):
    cleaned = ""
    for char in word.lower():
        if char.isalnum():   # keeps letters and numbers only
            cleaned += char
    return cleaned == cleaned[::-1]

print("Palindrome tests:")
print("racecar:", palindrome("racecar"))
print("Nurses Run:", palindrome("Nurses Run"))
print("Sit on a potato pan, Otis.:", palindrome("Sit on a potato pan, Otis."))
print("hello:", palindrome("hello"))



def parentheses(sequence):
    count = 0
    for i in sequence:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:      
            return False
    return count == 0

print("Parentheses tests:")
print("((blah)()()()):", parentheses("((blah)()()())"))
print("(((())blee)):", parentheses("(((())blee))"))
print("(()hello((())())):", parentheses("(()hello((())()))"))
print("((((((()):", parentheses("((((((())"))
print("())):", parentheses("()))"))
