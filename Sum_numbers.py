def sum_numbers(string):
    #Empty List
    num = []
    #Splits the string by spaces
    for i in string.split():
        #Check is the split is a digit
        if i.isdigit():
            #add to the list the value of the string
            num.append(int(i)) #Has to get the int value of the string
    return sum(num)
print(sum_numbers('This is a test: 1 plus 2'))
