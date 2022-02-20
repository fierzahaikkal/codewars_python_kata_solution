def solution(num):
    list = []
    for i in range(0, num):
        if i%3 == 0 or i%5 == 0:
            list.append(i)
    return(sum(list))
