# --- AoC 2024 - Day 1: Historian Hysteria PART 2 --- #

# The Problem:
# 2 Lists of numbers, find the "similarity score"
# number n in left list x frequency in right list
# Sum of similarity score

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

# Tracking similarity
# Use Counter to summarise the right list as a frequency of entries
from collections import Counter
rcnt = Counter(r)

# Access the frequency of int. n by using rcnt[n]
s = []
for i in l:
    sim = i * rcnt[i]
    s.append(sim)

print("Similarity score: " + str(sum(s)))