# --- AoC 2024 - Day 1: Historian Hysteria PART 1 --- #

# The Problem:
# 2 Lists of numbers, match the smallest in each and find difference
# Repeat for all the numbers in the lists

# The Code:
# Read input file
with open("2024_day1_input.txt") as f:
    content = f.readlines()

# Seperate data
raw = []
for i in content:
    raw.append(i.split())

# Seperate into L and R list as ints
l, r = [], []
for x in raw:
    l.append(int(x[0]))
    r.append(int(x[1]))

# Organise list by size
l.sort()
r.sort()

print(l)
print(r)

# Work out difference for entries:
d = []
for i in range(0,len(l)):
    diff = abs(l[i]-r[i])
    d.append(diff)

print(d)
print("sum: " + str(sum(d)))
