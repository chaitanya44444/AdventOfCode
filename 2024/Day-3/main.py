import re

with open("2024/Day-3/input.txt") as file:
    data = file.read().replace('\n', '')

def multi(st):
    result = 0
    for i in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', st):
        result += int(i.group(1)) * int(i.group(2))
    return result

def p1(d):
    return multi(d)

print(f"part 1 answer is: {p1(data)}")
def p2(d):
    retval = 0
    enabled = True
    pattern = re.compile(r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")
    for instruction in pattern.finditer(d):
        i_type = instruction.groups()
        if i_type[4] == "don't":
            enabled = False
        elif i_type[3] == "do":
            enabled = True
        elif i_type[0] == "mul" and enabled:
            a,b = instruction.group(2,3)
            retval += int(a) * int(b)
    return retval

print(f"part 2 answer is: {p2(data)}")

