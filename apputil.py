

# add code below ...

    """
    Check whether a given string is a palindrome.
    This function ignores case and non-alphanumeric characters.
    
    :param word: The input string to check
    :return: True if the string is a palindrome, False otherwise
    """
def palindrome(word):
    cleaned = ""
    for char in word.lower():
        if char.isalnum():   # keeps letters and numbers only
            cleaned += char
    return cleaned == cleaned[::-1]

palindrome("racecar")       
palindrome("Nurses Run")
palindrome("Sit on a potato pan, Otis.")
palindrome("hello")


    """
    Check whether a string contains balanced parentheses.
    
    :param sequence: A string that may contain parentheses
    :return: True if parentheses are balanced, False otherwise
    """
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

parentheses("((blah)()()())")
parentheses("(((())blee))")
parentheses("(()hello((())()))")
parentheses("((((((())")
parentheses("()))")
