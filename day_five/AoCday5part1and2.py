import math

with open('input.txt') as input:
    boarding_passes = input.read().split()

highest_ID = 0
seat_id_list = []

for boarding_pass in boarding_passes:
    row_lowest = 0
    row_highest = 127
    column_lowest = 0
    column_highest = 7

    for letter in boarding_pass[0:7]:
        if letter == 'B':
            row_lowest = math.ceil((row_highest + row_lowest) / 2)
        elif letter == 'F':
            row_highest = (row_highest + row_lowest) // 2


    row = row_lowest

    for letter in boarding_pass[7:10]:
        if letter == "L":
            column_highest = (column_lowest + column_highest) // 2
        else:
            column_lowest = math.ceil(((column_lowest + column_highest) / 2))
    column = column_lowest

    seat_ID = (8*row) + column
    seat_id_list.append(seat_ID)
    if seat_ID > highest_ID:
        highest_ID = seat_ID

print("Highest ID is: " + str(highest_ID))

sorted_list = sorted(seat_id_list)

index = 0
for id in sorted_list:
    if sorted_list[index] + 1 < sorted_list[index + 1]:
        print('My seat is:' + str(sorted_list[index] + 1))
        break
    index += 1


