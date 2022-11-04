import json
import sorts

def findJulianInUniques(data):
    pointer = 0
    for record in data:
        if (record == "Julian"):
            return pointer
        pointer = pointer + 1

def getNameByType(data, nameType):
    names = []
    for record in data:
        if (record[10] == nameType):
            names.append(record[11])
    names = [*set(names)]
    return names

def getUniqueNames(data, name):
    pointer = 0
    positions = []
    names = []
    
    for record in data:
        names.append(record[11])
        if record[11] == name:
            positions.append(pointer)

        pointer = pointer + 1
        uniqueNames = [*set(names)]

    print("Position of Julian: ")
    print(positions)
    print("Unique names: ")
    print(len(names))
    print("Julian amount: ")
    print(len(positions))

    return uniqueNames

def getJsonData():
    data = json.load(open('imiona.json'))
    return data['data']

def binarySearch(data, value):
    index = len(data) // 2
    print("***** BINARY SEARCH *****")
    if (data[index] == value):
        print("found")
        return index
    elif (data[index] > value):
        binarySearch(data[0:index])
        print("binary low")
    else:
        print("binary high")
        binarySearch(data[index:len(data)])


# getUniqueNames(getJsonData(), "Julian")
# getNameByType(getJsonData(), "HISPANIC")
print(findJulianInUniques(getUniqueNames(getJsonData(), "Julian")))
# print(sorts.bubble(getNameByType(getJsonData(), "HISPANIC")))
# print(binarySearch(sorts.bubble(getUniqueNames(getJsonData(), "Julian"))))
