# --- AoC 2024 - Day 2: Red Nosed Reports PART 1 --- #

# The Problem:
# Data input is a series of "reports" (one per line)
# Each report is made of a list of numbers called "levels"

# Reports are considered SAFE if:
# 1/ Levels are either ALL increasing or decreasing
# 2/ Any 2 adjacent levels differ by at least 1 and at most 3

# For the input, how many are safe?

# The Code:
# Read input file
with open("2024_day2_input.txt") as f:
    content = f.readlines()

# Convert each report into series of integers
data = []
for i in range(0,len(content)):
    report = []
    raw_report = content[i].split()
    for j in raw_report:
        report.append(int(j))

    data.append(report)

# General idea will be:
# Take the first entry and compare with next;
# If the size of this difference is 0 or greater than 3 then report is unsafe
# If not, then compare the sign of this difference to determine increase/decrease
# Keep track of increase and decrease as booleans

# If at any point in looking at a report both increase or decrease are True - unsafe

test_report = [9, 7, 6, 2, 1]
def check_safe(report):
    increase, decrease = False, False
    i = 0
    while i < len(report)-1:
        # Calculate difference in terms:
        diff = report[i+1] - report[i]
        
        # Checking this works:
        # print(report[i],report[i+1],diff)
        
        # Size of difference
        if diff == 0 or abs(diff) > 3:
            return "UNSAFE"
        
        # Increase or decrease
        if diff > 0:
            increase = True
        
        if diff < 0:
            decrease = True

        if increase and decrease:
            return "UNSAFE"
        
        else:
            i += 1

    return "SAFE"

safe = 0
unsafe = 0
for i in data:
    if check_safe(i) == "SAFE":
        safe += 1
    elif check_safe(i) == "UNSAFE":
        unsafe += 1

print(safe,unsafe)