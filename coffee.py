starting_list = input().split()
number_of_commands = int(input())

for commandes in range(number_of_commands):
    commands = input().split()

    if commands[0] == "Include":
        starting_list.append(commands[1])

    elif commands[0] == "Remove":
        first_or_last = commands[1]
        number = int(commands[2])

        if first_or_last == "first":
            starting_list = starting_list[number:]
        elif first_or_last == "last":
            starting_list = starting_list[:-number]

    elif commands[0] == "Prefer":
        index1 = int(commands[1])
        index2 = int(commands[2])
        if index1 < len(starting_list) and index2 < len(starting_list):
            starting_list[index1], starting_list[index2] = starting_list[index2], starting_list[index1]

    elif commands[0] == "Reverse":
        starting_list.reverse()

print("Coffees:")
print(" ".join(starting_list))
