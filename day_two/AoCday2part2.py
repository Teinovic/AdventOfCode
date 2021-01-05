r = open('inputday2.txt').read().splitlines()
transition_list = []
transition_list1 = []
transition_list2 = []

def towards_a_wanted_list(arg):
    for element in arg:
        x = element.split(':')
        transition_list.append(x)

x = towards_a_wanted_list(r)

for element1, element2 in transition_list:
    x, y = element1.strip(), element2.strip()
    transition_list1.append(x.split('-'))
    transition_list2.append(y)

wanted_list = list(zip(transition_list1, transition_list2))

valid_pass = 0

for key, value in wanted_list:
    first_position = int(key[0])
    second_position = int(key[1][0:2])
    letter_being_looked_for = key[1][-1]
    password_candidate = value
    if letter_being_looked_for == password_candidate[first_position-1] and \
        letter_being_looked_for != password_candidate[second_position-1]:
        valid_pass += 1
    if letter_being_looked_for != password_candidate[first_position-1] and \
        letter_being_looked_for == password_candidate[second_position-1]:
        valid_pass += 1

print(valid_pass)







#
# for key, value in x:
#     if key[2] == '-':
#         num_of_letters_lowest = int(key[0:2])
#         num_of_letters_highest = int(key[3:5])
#     elif key[1] == '-':
#         num_of_letters_lowest = int(key[0])
#         num_of_letters_highest = int(key[2:4])
#
#     letter_being_looked_for = key[-1]
#
#     if value.count(letter_being_looked_for) in range(num_of_letters_lowest, num_of_letters_highest + 1):
#         valid_passwords += 1
#     else:
#         invalid_passwords += 1
#
# print(valid_passwords, invalid_passwords)