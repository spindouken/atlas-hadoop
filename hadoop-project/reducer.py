#!/usr/bin/env python
import sys

top_salaries = []

# process lines from the std input
for line in sys.stdin:
    # skip the header or any improperly formatted lines
    try:
        # split the line into id, company, and totalyearlycompensation
        id, rest = line.strip().split("\t")
        company, salary = rest.split(",")
        salary = float(salary)  # convert the salary to float
    except ValueError:
        # skip lines if line format is off
        continue

    # add line's record to the array
    top_salaries.append((salary, id, company))

    # sort in descending order and slice top 10 salaries from list
    top_salaries = sorted(top_salaries, reverse=True)[:10]

# print the sorted top 10 salaries
print("id\tSalary\tcompany")
for salary, id, company in top_salaries:
    print("{}\t{}\t{}".format(id, salary, company))
