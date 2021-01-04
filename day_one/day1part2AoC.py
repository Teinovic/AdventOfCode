input = [int(x) for x in open('inputday1.txt').read().strip('\n').splitlines()]

print({x * y * z for x in input for y in input for z in input if x + y + z == 2020})
