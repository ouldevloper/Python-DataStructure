#herllo!232hsdh53%$^ahmed
# return  herllo
from pprint import pprint

def Solve(item):
    items = []
    l = len(item)-1
    index = 0
    while index <= l:
        subStr = ""
        i = 0
        while item[index+i].isalpha():
            print(item[index+i])
            subStr += item[index+i]
            i+=1
        else:
            i +=1
            print('-------------------------')
        if subStr!="":
            items.append(subStr)
        index += i
        if index >=len(item):
            break

    pprint(items)
Solve("herllo!232hsdh53%$^ahmed")