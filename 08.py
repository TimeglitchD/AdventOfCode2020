# part one

accumulator = 0
commands = []
position = 0
known = []

f = open("08.txt", "r")

for l in f:
    commands.append(l.rstrip())
f.close()

while position not in known:
    known.append(position)
    command = commands[position]
    if command[:3] == "jmp":
        position = position + int(command[4:])
    elif command[:3] == "acc":
        accumulator = accumulator + int(command[4:])
        position += 1
    elif command[:3] == "nop":
        position += 1

print(accumulator)


# part two

commands = []
comfix = 0


while(True):
    known = []
    commands = []
    f = open("08.txt", "r")
    for l in f:
        commands.append(l.rstrip())
    f.close()
    position = 0
    accumulator = 0

    if comfix == len(commands):
        break


    if commands[comfix][:3] == "jmp":
        commands[comfix] = "nop" + commands[comfix][3:]
    elif commands[comfix][:3] == "nop":
        commands[comfix] = "jmp" + commands[comfix][3:]

    while position not in known:
        known.append(position)
        if(position < len(commands)):
            command = commands[position]
            if command[:3] == "jmp":
                position += int(command[4:])
            elif command[:3] == "acc":
                accumulator += int(command[4:])
                position += 1
            elif command[:3] == "nop":
                position += 1
        else:
            print(accumulator)
    comfix += 1
