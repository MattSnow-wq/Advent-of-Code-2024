# --- AoC 2024 - Day 2: Red Nosed Reports PART 2 --- #

# The Problem:
# Data input is a series of "reports" (one per line)
# Each report is made of a list of numbers called "levels"

# Reports are considered SAFE if:
# 1/ Levels are either ALL increasing or decreasing
# 2/ Any 2 adjacent levels differ by at least 1 and at most 3

# MODIFICATION: if any level is removed from an unsafe report and
# makes it a safe report, pass it as safe.

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
# Use the check from last time - if it passes, leave as is
# If it's unsafe, run a function to remove any individual "level"
# and recheck until safe or not safe

test_data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9] 
            ]

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

def modify_check(report):
    "Returns reports with one level missing"
    "Then runs modified check_safe"
    modified = []
    for i in range(0,len(report)):
        remaining = report[:i] + report[i+1:]
        modified.append(remaining)

    safe, unsafe = False, False

    for i in modified:
        if check_safe(i) == "UNSAFE":
            unsafe = True
        elif check_safe(i) == "SAFE":
            safe = True

    if safe:
        return "SAFE"
    else:
        return "FALSE"

# Let's run on some test data
# safe, unsafe = 0, 0
# for i in test_data:
#     if check_safe(i) == "SAFE":
#         safe += 1
#         pass
#     elif modify_check(i) == "SAFE":
#             safe += 1
#             pass
#     else:
#         unsafe += 1

# Let's run on the real stuff
safe, unsafe = 0, 0
for i in data:
    if check_safe(i) == "SAFE":
        safe += 1
        pass
    elif modify_check(i) == "SAFE":
            safe += 1
            pass
    else:
        unsafe += 1
print(safe,unsafe)
