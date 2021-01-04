input = [int(x) for x in open('inputday1part1.txt').read().strip('\n').splitlines()]

print({x * y for x in input for y in input if x + y == 2020})
