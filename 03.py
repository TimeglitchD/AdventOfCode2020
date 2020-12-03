# part one

f = open("03.txt", "r")
position = 0
first = True
counter = 0
for l in f:
    if first:
        l.rstrip()
        first = False
        continue
    l.rstrip()
    position += 3
    pos = position % (len(l)-1)
    if l[pos] == "#":
        counter += 1

print(counter)
f.close()

# part two

def traverse(right, down):
    f = open("03.txt", "r")
    position = 0
    skip = down+1
    counter = 0

    for l in f:
        if (skip > 1):
            skip -= 1
            continue
        else:
            skip = down
        
        l.rstrip()
        position += right
        pos = position % (len(l)-1)

        if l[pos] == "#":
            counter += 1
        

    f.close()
    return counter

result = traverse(1, 1)
result *= traverse(3, 1)
result *= traverse(5, 1)
result *= traverse(7, 1)
result *= traverse(1, 2)

print(result)


