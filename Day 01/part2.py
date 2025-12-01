lines = []
position = 50
zeroes = 0

with open("input2.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())

print(lines)

def spin(start, move):
    direction = move[0]
    value = int(move[1:])

    if direction == 'L':
        result = start - value
    else:
        result = start + value
    
    crosses = abs(result // 100) 
    position = result % 100
    landed_zero = 1 if position == 0 else 0

    zero = crosses + landed_zero

    return zero, position

for line in lines:
    result = spin(position, line)
    zeroes = zeroes + result[0]
    position = result[1]
    
        
    print("Line: " + line + ", result: " + str(position))
    print("Zeroes:" + str(zeroes))
