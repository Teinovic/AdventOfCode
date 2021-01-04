input = [int(x) for x in open('inputday1part1.txt').read().strip('\n').splitlines()]


solution = []
for num in input:
    for num_two in input:
        if num + num_two == 2020:
            solution.append(num * num_two)

print(set(solution))