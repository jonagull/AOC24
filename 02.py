with open('02.txt', 'r') as file:
    file = file.read()

rows = file.strip().split('\n')
data = [list(map(int, row.split())) for row in rows]
safeLevels = []    

def checkLevels(levels):
    filteredLevels = []

    #loop through levels and find which are actually sorted
    for i in range (len(levels)):
        level = levels[i]

        if checkIfSortedList(level):
            filteredLevels.append(level)

        problemDampener(level)

    #loop over filtered levels
    for l in range (len(filteredLevels)):
        fl = filteredLevels[l]

        if checkLevelIsSafe(fl) and fl not in safeLevels :
            safeLevels.append(fl)

    print('safelevel',safeLevels)
    print(len(safeLevels))

def checkIfSortedList(level):
        reversedLevel = level[::-1]
        if sorted(level) == level:
            print('level is sorted')
            return True
        elif sorted(reversedLevel) == reversedLevel:
            print('level is sorted')
            return True
        else: 
            print('level is sorted')
            return False
    

def problemDampener(level):
    copyLevel = level[:]  
    print(level)
    isSafe = False

    for x in range(len(level)):
        currentLevel = copyLevel[:]
        removed_element = currentLevel.pop(x)

        if checkLevelIsSafe(currentLevel) and checkIfSortedList(currentLevel):
            isSafe = True

        currentLevel.insert(x, removed_element)

    if isSafe and level not in safeLevels:
        safeLevels.append(level)
        print('added', level)


def checkLevelIsSafe(level):
    allowedDiffs = [1, 2, 3]
    lastIndex = len(level) - 1
    isSafe = True
     
    # print('level',level)

    #loop over level and check if the increment in allowed increments
    for x in range (len(level)):
        nextIndex = x + 1 
        if nextIndex > lastIndex:
            continue
        if x == lastIndex:
            continue

        number = level[x] 
        nextNumber = level[nextIndex]
        diff = number - nextNumber
        positiveDiff = abs(diff)

        if positiveDiff not in allowedDiffs:
            isSafe = False

    return isSafe

checkLevels(data)