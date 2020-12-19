# part one

f = open("07.txt", "r")

bags = {}
bagpos = 0
total = 0


def searchgold(bag):
    if "shiny gold" in bags[bag]:
        return True
    for b in bags[bag]:
        if searchgold(b):
            return True
    return False


for l in f:
    bagpos = l.find("bag")
    key = l[:bagpos-1]  # "light red"
    values = []
    # "contain 1 bright white bag, 2 muted yellow bags."
    l = l[l.find("contain"):]

    while l.find(" ") != -1:
        l = l[l.find(" ")+1:]   # "1 bright white bag, 2 muted yellow bags."
        l = l[l.find(" ")+1:]   # "bright white bag, 2 muted yellow bags."
        bagpos = l.find("bag")
        value = l[:bagpos-1]  # "bright white"
        if value != "other":
            values.append(value)
        l = l[bagpos:]  # "bag, 2 muted yellow bags."

    bags[key] = values

f.close()

for bag in bags:
    if searchgold(bag):
        total += 1

print(total)

# part two

f = open("07.txt", "r")

bags = {}

def countbags(bag):
    number = len(bags[bag])
    if number == 0:
        return 0
    for b in bags[bag]:
        number += countbags(b)
    return number

for l in f:
    bagpos = l.find("bag")
    key = l[:bagpos-1]  # "light red"
    values = []
    # "contain 1 bright white bag, 2 muted yellow bags."
    l = l[l.find("contain"):]

    while l.find(" ") != -1:
        l = l[l.find(" ")+1:]   # "1 bright white bag, 2 muted yellow bags."
        amount = l[0]
        l = l[l.find(" ")+1:]   # "bright white bag, 2 muted yellow bags."
        bagpos = l.find("bag")
        value = l[:bagpos-1]  # "bright white"
        if value != "other":
            amount = int(amount)
            while amount > 0:
                values.append(value)
                amount -= 1

        l = l[bagpos:]  # "bag, 2 muted yellow bags."

    bags[key] = values
f.close()


print(countbags("shiny gold"))