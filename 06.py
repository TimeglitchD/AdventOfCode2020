# part one

total = 0
yes = []
import string

f = open("06.txt", "r")

for l in f:
    if(l == "\n"): # if line is newline, group ends
        total += len(yes) # add number of letters in list to total
        yes = []
    else:
        l = l.rstrip()
        for c in l:
            if c not in yes:
                yes.append(c) # add unique letters to list
else: # if end of file, group ends
    total += len(yes) # add number of letters in list to total
    yes = []

f.close()
print(total)

# part two

import string

total = 0
yes = list(string.ascii_lowercase)
no = []
import string

f = open("06.txt", "r")

for l in f:
    if(l == "\n"): # if line is newline, group ends
        total += len(yes) # add number of letters in list to total
        yes = list(string.ascii_lowercase)
        no = []
    else:
        l = l.rstrip()
        for c in yes:
            if c not in l:
                no.append(c) # add missing letters from each person in group to list
        for c in no:
            if c in yes:
                yes.remove(c) # remove all the letters from missing letter list from the total list
else: # if end of file, group ends
    total += len(yes) # add number of letters in list to total

f.close()
print(total)