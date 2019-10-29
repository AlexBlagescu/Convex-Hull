import math
filename = 'date.in'
myList = []
with open(filename) as f:
    line = f.readline().split()
    n = int(line[0])
    while line:
        line = f.readline().split()
        if line:
            line[0] = int(line[0])
            line[1] = int(line[1])
            myList.append(line)
firstPoint = myList[0]
for list in myList:
    if list[1] < firstPoint[1]:
        firstPoint = list
    elif list[1] == firstPoint[1]:
        if list[0] < firstPoint[0]:
            firstPoint = list
myList.remove(firstPoint)
cnt = 0
for list in myList:
    a = list[0] - firstPoint[0]
    b = math.sqrt((firstPoint[0] - list[0]) ** 2 + (firstPoint[1] - list[1]) ** 2)
    alfa = math.acos(a/b)
    list.append(round(alfa, 4))
    list.append(round(b, 4))
    myList[cnt] = list
    cnt += 1
myList.sort(key = lambda x: (x[2], x[3]) )
firstPoint.append(0)
firstPoint.append(0)
myStack = [firstPoint, myList[0], myList[1]]
myList.remove(myList[0])
myList.remove(myList[0])
i = 2
for list in myList:
    i += 1
    myStack.append(list)
    det =  myStack[i-2][0] * myStack[i-1][1] + myStack[i-1][0] * myStack[i][1] + myStack[i-2][1] * myStack[i][0] - myStack[i][0] * myStack[i-1][1] - myStack[i-2][1] * myStack[i-1][0] - myStack[i][1] * myStack[i-2][0]
    while det < 0 and i > 2:
        myStack.pop(i-1);
        i -= 1
        det = det =  myStack[i-2][0] * myStack[i-1][1] + myStack[i-1][0] * myStack[i][1] + myStack[i-2][1] * myStack[i][0] - myStack[i][0] * myStack[i-1][1] - myStack[i-2][1] * myStack[i-1][0] - myStack[i][1] * myStack[i-2][0]
reversedMyList = reversed(myList)
for list in reversedMyList:
    if list[2] == myStack[i][2]:
        det = myStack[0][0] * myStack[i][1] + myStack[i][0] * list[1] + myStack[0][1] * list[0] - list[0] * myStack[i][1] - list[1] * myStack[0][0] - myStack[0][1] * myStack[i][0]
        if det == 0 and list not in myStack:
            myStack.append(list)
print(len(myStack))
for elem in myStack:
    print(elem[0], end = ' ')
    print(elem[1])
