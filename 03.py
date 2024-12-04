import re
lol = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open('03.txt', 'r') as file:
    file = file.read()

def findGroups(input):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(pattern, input)

def extractNumbers(groups):
    return [list(map(int, re.findall(r"\d{1,3}", group))) for group in groups]

def multiplyNumbers(numbers):
    return numbers[0] * numbers[1]

def sumNumbers(list):
    lol = []
    for i in range (len(list)):
        # print(list[i])
        lol.append(multiplyNumbers(list[i]))
    
    return sum(lol)

groups = findGroups(file)
listOfNumbers = extractNumbers(groups)
total = sumNumbers(listOfNumbers)

print(total)
