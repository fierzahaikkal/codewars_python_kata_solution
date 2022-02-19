def solution(roman):
    roman_query = roman_query = {'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    s = 0
    answer = 0
    n = len(roman)
    for i in range(n-1, -1, -1):
        if roman_query[roman[i]] >= s :
            answer += roman_query[roman[i]]
        else:
            answer -= roman_query[roman[i]]
        s = roman_query[roman[i]]
    return answer
