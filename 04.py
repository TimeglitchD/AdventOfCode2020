# part one

import string
f = open("04.txt", "r")

credentials = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False
}

valid = 0


def findInfo(x, info):
    if(x.find(info+":") != -1):
        credentials[info] = True # if found, turn true


for x in f:
    if(x == "\n"): # if line is newline, check passport and make new passport

        if False not in credentials.values(): # if only True in credentials
            valid += 1

        for i in credentials:
            credentials[i] = False # reset all values for next passport

    else:
        for i in credentials:
            findInfo(x, i)
else:
    if False not in credentials.values():
        valid += 1

print(valid)

f.close()


# part two

f = open("04.txt", "r")

credentials = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False
}


def findSpace(x, pos):
    space = x.find(" ", pos)
    if space == -1:
        space = x.find("\n", pos)
    if space == -1:
        return x[pos:]
    return x[pos:space]


def byr(x):
    pos = x.find("byr:")
    if(pos != -1):
        pos += 4
        val = findSpace(x, pos)
        if(len(val) == 4):                   # 4 digits check
            if all(c in string.digits for c in val):    # numbers check
                val = int(val)
                if(val >= 1920 and val <= 2002):    # value check
                    credentials["byr"] = True


def iyr(x):
    pos = x.find("iyr:")
    if(pos != -1):
        pos += 4
        val = findSpace(x, pos)
        if(len(val) == 4):                   # 4 digits check
            if all(c in string.digits for c in val):    # numbers check
                val = int(val)
                if(val >= 2010 and val <= 2020):    # value check
                    credentials["iyr"] = True


def eyr(x):
    pos = x.find("eyr:")
    if(pos != -1):
        pos += 4
        val = findSpace(x, pos)
        if(len(val) == 4):                   # 4 digits check
            if all(c in string.digits for c in val):    # numbers check
                val = int(val)
                if(val >= 2020 and val <= 2030):    # value check
                    credentials["eyr"] = True


def hgt(x):
    pos = x.find("hgt:")
    if(pos != -1):
        pos += 4
        val = findSpace(x, pos)
        if "in" in val:                         # inch
            inc = val.find("in")
            val = val[0:inc]
            if len(val) == 2:                  # 2 digits check
                if all(c in string.digits for c in val):    # numbers check
                    val = int(val)
                    if(val >= 59 and val <= 76):    # value check
                        credentials["hgt"] = True
        elif "cm" in val:                         # cm
            cm = val.find("cm")
            val = val[0:cm]
            if len(val) == 3:                   # 3 digits check
                if all(c in string.digits for c in val):    # numbers check
                    val = int(val)
                    if(val >= 150 and val <= 193):  # value check
                        credentials["hgt"] = True


def hcl(x):
    pos = x.find("hcl:")
    if(pos != -1):
        pos += 4
        val = findSpace(x, pos)
        
        if val[0] == "#":                                   # hastag check
            if len(val) == 7:                            # 6 digits check
                val = val[1:]
                if all(c in string.hexdigits for c in val):  # hex check
                    credentials["hcl"] = True


def ecl(x):
    eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pos = x.find("ecl:")
    if(pos != -1):
        pos += 4
        val = findSpace(x, pos)
        if val in eyes:                          # value check
            credentials["ecl"] = True


def pid(x):
    pos = x.find("pid:")
    if(pos != -1):
        pos += 4
        val = findSpace(x, pos)
        if len(val) == 9:                    # 9 digits check
            if all(c in string.digits for c in val):  # numbers check
                credentials["pid"] = True



valid = 0


for x in f:
    if(x == "\n"): # if line is newline, check passport and make new passport

        if False not in credentials.values(): # if only True in credentials
            valid += 1

        for i in credentials:  # reset all values for next passport
            credentials[i] = False

    else:
        x = x.rstrip()
        for i in credentials:   # check every value
            eval(i + "(x)")
else:
    if False not in credentials.values():
        valid += 1

f.close()
print(valid)
