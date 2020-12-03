# part one

f = open("02.txt", "r")

counter = 0

for l in f:
    mini = int(l[:l.index("-")])
    maxi = int(l[(l.index("-")+1):l.index(" ")])
    letter = l[(l.index(" ")+1):l.index(":")]
    password = l[(l.index(":")+2):]

    amount = password.count(letter)
    if(amount >= mini and amount <= maxi):
        counter += 1

print(counter)
f.close()


# part two

f = open("02.txt", "r")

counter = 0

for l in f:
    one = int(l[:l.index("-")])
    two = int(l[(l.index("-")+1):l.index(" ")])
    letter = l[(l.index(" ")+1):l.index(":")]
    password = l[(l.index(":")+2):]

    if((letter == password[(one-1)]) ^ (letter == password[(two-1)])):
        counter += 1

print(counter)
f.close()
