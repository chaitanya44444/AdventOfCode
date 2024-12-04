data = open('2024/Day-4/input.txt').read().strip().split('\n')

p1=0
p2=0

for _ in range(len(data)):
    for i in range(len(data[0])):
        if i+3<len(data[0]) and data[_][i]=='X' and data[_][i+1]=='M' and data[_][i+2]=='A' and data[_][i+3]=='S':
            p1 += 1
        if _+3<len(data) and data[_][i]=='X' and data[_+1][i]=='M' and data[_+2][i]=='A' and data[_+3][i]=='S':
            p1 += 1
        if _+3<len(data) and i+3<len(data[0]) and data[_][i]=='X' and data[_+1][i+1]=='M' and data[_+2][i+2]=='A' and data[_+3][i+3]=='S':
            p1 += 1
        if i+3<len(data[0]) and data[_][i]=='S' and data[_][i+1]=='A' and data[_][i+2]=='M' and data[_][i+3]=='X':
            p1 += 1
        if _+3<len(data) and data[_][i]=='S' and data[_+1][i]=='A' and data[_+2][i]=='M' and data[_+3][i]=='X':
            p1 += 1
        if _+3<len(data) and i+3<len(data[0]) and data[_][i]=='S' and data[_+1][i+1]=='A' and data[_+2][i+2]=='M' and data[_+3][i+3]=='X':
            p1 += 1
        if _-3>=0 and i+3<len(data[0]) and data[_][i]=='S' and data[_-1][i+1]=='A' and data[_-2][i+2]=='M' and data[_-3][i+3]=='X':
            p1 += 1
        if _-3>=0 and i+3<len(data[0]) and data[_][i]=='X' and data[_-1][i+1]=='M' and data[_-2][i+2]=='A' and data[_-3][i+3]=='S':
            p1 += 1

        if _+2<len(data) and i+2<len(data[0]) and data[_][i]=='M' and data[_+1][i+1]=='A' and data[_+2][i+2]=='S' and data[_+2][i]=='M' and data[_][i+2]=='S':
            p2 += 1
        if _+2<len(data) and i+2<len(data[0]) and data[_][i]=='M' and data[_+1][i+1]=='A' and data[_+2][i+2]=='S' and data[_+2][i]=='S' and data[_][i+2]=='M':
            p2 += 1
        if _+2<len(data) and i+2<len(data[0]) and data[_][i]=='S' and data[_+1][i+1]=='A' and data[_+2][i+2]=='M' and data[_+2][i]=='M' and data[_][i+2]=='S':
            p2 += 1
        if _+2<len(data) and i+2<len(data[0]) and data[_][i]=='S' and data[_+1][i+1]=='A' and data[_+2][i+2]=='M' and data[_+2][i]=='S' and data[_][i+2]=='M':
            p2 += 1
print(f"Answer for part 1: {p1}")
print(f"Answer for part 2: {p2}")