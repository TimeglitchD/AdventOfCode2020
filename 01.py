# part one

list1 = []

f = open("01.txt", "r")
for x in f:
    x.rstrip()
    num = int(x)
    list1.append(num)

f.close()

count = 0
maxlen = len(list1)
found = False

for i in list1:
    if found:
        break
    for j in list1:
        if found:
            break
        if(i+j == 2020):
            print(i*j)
            found = True


# part two

list1 = []

f = open("01.txt", "r")
for x in f:
    x.rstrip()
    num = int(x)
    list1.append(num)

f.close()

count = 0
maxlen = len(list1)
found = False

for i in list1:
    if found:
        break
    for j in list1:
        if found:
            break
        for h in list1:
            if found:
                break
            if(i+j+h == 2020):
                print(i*j*h)
                found = True
