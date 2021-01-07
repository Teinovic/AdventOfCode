with open('input.txt') as f:
    tobogganinput = [string.strip('\n') for string in f.readlines()]

def trees_cut(start=0, right=3, down=1):
    position_on_slope = 0
    trees_cut_counter = 0
    for slope_location_index in range(start, len(tobogganinput), down):
        slope = tobogganinput[slope_location_index]
        if slope[position_on_slope] == '#':
            trees_cut_counter += 1
        position_on_slope += right
        position_on_slope = position_on_slope % len(slope)

    return trees_cut_counter

print(trees_cut())
