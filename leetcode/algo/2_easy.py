def search(items, value: int):
  hight = len(items)-1
  low   = 0
  while hight >= low :
    index = (hight+low)//2
    #print("index: %d, low: %d, Hight: %d, item: %d, value: %d" %(index, low, hight, items[index], value))
    if items[index] == value:
      return True
    elif items[index] > value :
      hight = index-1
    else:
      low = index+1
  return False

def SolveUsingNativeFunction(strArr):
  outputItems = []
  arr1 = strArr[0].split(',')
  arr2 = strArr[1].split(',')
  for item in arr1:
    if arr2.count(item)>0:
      print(item, end=', ')
  print()


def FindIntersection(strArr):
  outputItems = []
  arr1 = list(map(int, strArr[0].split(',')))
  arr2 = list(map(int, strArr[1].split(',')))
  for item in arr1:
    if search(arr2, item):
      outputItems.append(str(item))
  return ",".join(outputItems)




# input = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
input = ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
# keep this function call here 
#print(FindIntersection(input))
print(SolveUsingNativeFunction(input))
