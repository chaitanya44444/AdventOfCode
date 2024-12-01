l1=[]
l2=[]
solution=[]
with open("day1/input.txt") as file:
    for line in file:
        l2i, r2i= map(int, line.strip().split())

        l1.append(l2i)
        l2.append(r2i)
l1.sort(reverse = True)
l2.sort(reverse = True)
a=0
b=0
#part 1

for i in range(len(l1)):
    a+=abs(l1[i]-l2[i])
print(f"part 1 answer is {a}")

#part 2
for i in range(len(l1)):
    b+=l2.count(l1[i]) * l1[i]
print(f"answer for part 2: {b}")
