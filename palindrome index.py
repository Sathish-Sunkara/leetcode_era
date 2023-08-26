def is_palindrome(s):
    return s == s[::-1]

def palindrome_index(s):
    if is_palindrome(s):
        return -1

    n = len(s)
    for i in range(n // 2):
        j = n - i - 1
        if s[i] != s[j]:
            if is_palindrome(s[i:j]):
                return j
            elif is_palindrome(s[i+1:j+1]):
                return i
            return -1
    

    return -1

# Example usage
s = input("enter string")  # Enter the string
result = palindrome_index(s)
print(result)
