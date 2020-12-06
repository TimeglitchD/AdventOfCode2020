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
        credentials[info] = True  # if found, turn True


for x in f:
    if(x == "\n"):  # if line is newline, check passport and make new passport

        if False not in credentials.values():  # if only True in credentials
            valid += 1

        for i in credentials:
            credentials[i] = False  # reset all values for next passport

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


def byr(val):
    if(len(val) == 4):                   # 4 digits check
        if all(c in string.digits for c in val):    # numbers check
            val = int(val)
            if(val >= 1920 and val <= 2002):    # value check
                return True
    return False


def iyr(val):
    if(len(val) == 4):                   # 4 digits check
        if all(c in string.digits for c in val):    # numbers check
            val = int(val)
            if(val >= 2010 and val <= 2020):    # value check
                return True
    return False


def eyr(val):
    if(len(val) == 4):                   # 4 digits check
        if all(c in string.digits for c in val):    # numbers check
            val = int(val)
            if(val >= 2020 and val <= 2030):    # value check
                return True
    return False


def hgt(val):
    if "in" in val:                         # inch
        inc = val.find("in")
        val = val[0:inc]
        if len(val) == 2:                  # 2 digits check
            if all(c in string.digits for c in val):    # numbers check
                val = int(val)
                if(val >= 59 and val <= 76):    # value check
                    return True
    elif "cm" in val:                         # cm
        cm = val.find("cm")
        val = val[0:cm]
        if len(val) == 3:                   # 3 digits check
            if all(c in string.digits for c in val):    # numbers check
                val = int(val)
                if(val >= 150 and val <= 193):  # value check
                    return True
    return False


def hcl(val):
    if val[0] == "#":                                   # hastag check
        if len(val) == 7:                            # 6 digits check
            val = val[1:]
            if all(c in string.hexdigits for c in val):  # hex check
                return True
    return False


def ecl(val):
    eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if val in eyes:                          # value check
        return True
    return False


def pid(val):
    if len(val) == 9:                    # 9 digits check
        if all(c in string.digits for c in val):  # numbers check
            return True
    return False


credentials = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

valid = 0
passport = ""
goodpass = True

def checkPassport():
    for i in credentials:   # check every value
        pos = passport.find(i+":")
        value = passport[pos+4:(passport.find(" ", pos+4))]
        if not eval(i + "(value)"):
            return False
    return True

for x in f:
    if(x == "\n"):  # if line is newline, check passport and make new passport

        goodpass = checkPassport()
        passport = ""
        if goodpass:  # if only True in credentials
            valid += 1
        goodpass = True

    else:
        passport += x.replace("\n", " ")

else:
    goodpass = checkPassport()
    passport = ""
    if goodpass:  # if only True in credentials
        valid += 1

f.close()
print(valid)
