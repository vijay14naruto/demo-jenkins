def is_palindrome(text):
    return text == text[::-1]

# Example usage
word = "madam"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
