# part one

f = open("05.txt", "r")

highestID = 0

for l in f:
    l = l.rstrip()
    row = "0b"
    column = "0b"
    for c in l:
        if(c == "F"):
            row += "0"
        if(c == "B"):
            row += "1"
        if(c == "L"):
            column += "0"
        if(c == "R"):
            column += "1"

    currentID = int(row, 2) * 8 + int(column, 2)

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
    l = l.rstrip()
    row = "0b"
    column = "0b"
    for c in l:
        if(c == "F"):
            row += "0"
        if(c == "B"):
            row += "1"
        if(c == "L"):
            column += "0"
        if(c == "R"):
            column += "1"

    currentID = int(row, 2) * 8 + int(column, 2)
    passes.append(currentID)

f.close()

passes.sort()
print(find_missing(passes))
