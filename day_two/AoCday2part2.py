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


