with open('input.txt') as f:
    tobogganinput = [string.strip('\n') for string in f.readlines()]

def trees_cut(right=3, down=1):
    position_on_slope = 0
    trees_cut_counter = 0
    for slope_location_index in range(0, len(tobogganinput), down):
        slope = tobogganinput[slope_location_index]
        if slope[position_on_slope] == '#':
            trees_cut_counter += 1
        position_on_slope += right
        position_on_slope = position_on_slope % len(slope)

    return trees_cut_counter

### day 2 ###

def trees_cut_by_5_trajectories_multiplied():
    return trees_cut(1) * trees_cut(3) * trees_cut(5) * trees_cut(7) * trees_cut(1, 2)

print(trees_cut_by_5_trajectories_multiplied())











