def find_uniq(arr):
    # your code here
    for char in set(arr):
        if arr.count(char) == 1:
            return char
