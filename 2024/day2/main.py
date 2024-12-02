grid = open("2024/day2/input.txt").read().splitlines()

rows1 = [list(map(int, row.split())) for row in grid]

def ifsave(a):
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) > 3 or abs(a[i] - a[i + 1]) < 1:
            return False
    return a == sorted(a) or a == sorted(a, reverse=True)

def p1(a):
    for i in range(len(a)):
        if ifsave(a[i]):
            return True
        else: return False
def p2(a):
    for i in range(len(a)):
        a1 = a[:i] + a[i + 1 :]
        if ifsave(a1):
            return True
    return False


safe_count = 0
safe_count_2=0
for row in rows1:
    if ifsave(row):
        safe_count+=1
    if ifsave(row) or p2(row):  
        safe_count_2 += 1



print(safe_count)
print(safe_count_2)
