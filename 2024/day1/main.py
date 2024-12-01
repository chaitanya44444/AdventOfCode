l1=[]
l2=[]
with open("AdventOfCode/2024/day1/input.txt") as file:
    for line in file:
        l2i, r2i= map(int, line.strip().split())

        l1.append(l2i)
        l2.append(r2i)
l1.sort(reverse = True)
l2.sort(reverse = True)
a=0
b=0
#part 1
print("answer for part 1:",str(sum(abs(l1[i] - l2[i]) for i in range(len(l1))) ))


#part 2
print("Answer for part 2:", sum(l2.count(l1[i]) * l1[i] for i in range(len(l1))))