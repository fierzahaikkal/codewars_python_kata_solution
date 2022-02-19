def well(x):
    #your code here
    value = x.count('good')
    if value == 0 :
        return "Fail!"
    elif value < 3:
        return "Publish!"
    else:
        return "I smell a series!"
