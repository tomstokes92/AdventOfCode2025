def part1(data: str) -> int:
    lines = data.strip().split('\n')
    dial_position = 50
    zero_check = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])

        # % 100 will round robin
        if direction == 'L':
            dial_position = (dial_position - clicks) % 100
        else: # direction R
            dial_position = (dial_position + clicks) % 100

        if dial_position == 0:
            zero_check += 1
    return zero_check
print(f"Part 1: {part1(open('Day1/input.txt').read())}")

def part2(data: str) -> int:
    lines = data.strip().split('\n')
    dial_position = 50
    zero_check = 0
    for line in lines:
        dial_direction = line[0]
        clicks = int(line[1:])
        # Move 1 click instead, starting with Left
        for _ in range(clicks):
            if dial_direction == 'L':
                dial_position = (dial_position - 1) % 100
            #Now Right    
            else:
                dial_position = (dial_position + 1) % 100
            #Zero Check    
            if dial_position == 0:
                zero_check += 1
    return zero_check
print(f"Part 2: {part2(open('Day1/input.txt').read())}")  