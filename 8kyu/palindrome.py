def is_palindrome(s):
    lowcase = s.lower()
    return lowcase == lowcase[::-1] #reverse menggunakan index
