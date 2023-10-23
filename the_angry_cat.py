price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
type_of_items = input()
left_side = 0
right_side = 0

if type_of_items == "cheap":
    for index in range(0, entry_point):
        if price_ratings[index] < price_ratings[entry_point]:
            left_side += price_ratings[index]
    for index in range(entry_point + 1, len(price_ratings),1):
        if price_ratings[index] < price_ratings[entry_point]:
            right_side += price_ratings[index]


elif type_of_items == "expensive":
    for index in range(0, entry_point):
        if price_ratings[index] >= price_ratings[entry_point]:
            left_side += price_ratings[index]

    for index in range(entry_point + 1, len(price_ratings),1):
        if price_ratings[index] >= price_ratings[entry_point]:
            right_side += price_ratings[index]

if right_side <= left_side:
    print(f"Left - {left_side}")
else:
    print(f"Right - {right_side}")


