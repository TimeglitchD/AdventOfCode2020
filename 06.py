# part one

total = 0
group = ""
import string

f = open("06.txt", "r")

for l in f:
    if(l == "\n"): # if line is newline, group ends
        total += len(list(set(list(group)))) # add number of letters in list to total
        group = ""
    else:
        l = l.rstrip()
        group += l
        
total += len(set(list(group))) # add number of letters in list to total

f.close()
print(total)


# part two

import string

total = 0
no = []
import string

f = open("06.txt", "r")

for l in f:
    if(l == "\n"): # if line is newline, group ends
        total += (26-len(set(no))) # add number of letters in list to total
        no = []
    else:
        l = l.rstrip()
        for c in string.ascii_lowercase:
            if c not in l:
                no.append(c) # add missing letters from each person in group to list
else: # if end of file, group ends
    total += (26-len(set(no))) # add number of letters in list to total


f.close()
print(total)