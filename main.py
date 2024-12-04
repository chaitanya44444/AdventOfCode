import os


for i in range(6,25):

    with open(f"2024/Day-{i}/main.py", 'w') as fp:
        fp.write(f"data = open('2024/Day-{i}/input.txt').read().strip().split('\\n')")
        
