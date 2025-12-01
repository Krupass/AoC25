lines = []
position = 50
zeroes = 0

with open("input1.txt", "r", encoding="utf-8") as file:
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
    
    position = result % 100

    return position

for line in lines:
    position = spin(position, line)
    if position == 0:
        zeroes = zeroes + 1
    print("Line: " + line + ", result: " + str(position))

print("Zeroes:" + str(zeroes))