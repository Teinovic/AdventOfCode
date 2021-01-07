with open('input.txt') as f:
    tobogganinput = f.read().splitlines()

extended_toboggan = []
b = 1

for string in tobogganinput:
    a = string * b
    extended_toboggan.append(a)
    b += 1

trees_hit = 0
steps = 0
for string in extended_toboggan:
    if string[steps] == '#':
        trees_hit += 1
    steps += 3

print(trees_hit)












# from boltons import iterutils
#
# toboggan_sublists = iterutils.chunked(tobogganinput, 11)
#
# trees_hit = 0
#
# for sublist in toboggan_sublists:
#     steps = 0
#     for line in sublist:
#         if line[steps] == '#':
#             trees_hit += 1
#             print('You hit a tree!')
#         else:
#             print('Tree dodged!')
#         steps += 3
#
# print(trees_hit)






#
# steps = 0
# treeshit = 0
#
#
# for line in tobboganinput:
#
#         if line[0 + steps] == '#':
#             treeshit += 1
#
#         steps += 3
#
# print(treeshit)
