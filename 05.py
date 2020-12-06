def getCurrentID(l):
    row = l[:7].replace("F", "0")
    row = "0b" + row.replace("B", "1")
    column = l[7:].replace("L", "0")
    column = "0b" + column.replace("R", "1")

    return int(row, 2) * 8 + int(column, 2)

# part one

f = open("05.txt", "r")

highestID = 0

for l in f:
    currentID = getCurrentID(l.rstrip())
    if highestID < currentID:
        highestID = currentID

f.close()
print(highestID)


# part two

def find_missing(lst): 
    start = lst[0] 
    end = lst[-1] 
    missing = sorted(set(range(start, end + 1)).difference(lst)) 
    return missing[0]


f = open("05.txt", "r")

passes = []

for l in f:
    passes.append(getCurrentID(l.rstrip()))

f.close()

passes.sort()
print(find_missing(passes))
