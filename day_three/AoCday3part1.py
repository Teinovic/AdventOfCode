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
