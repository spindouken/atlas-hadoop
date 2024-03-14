#!/usr/bin/env python
import sys
"""
code to map the salaries.csv file in data/
to be implemented with reducer
"""


# add counter to iterable input stream (ex. data piped in) using enumerate
#   assigning each line to 'line'
#   and its corresponding line number to 'x'
for x, line in enumerate(sys.stdin):
    data = line.strip().split(",")  # strip() to remove whitespaces

    #  identify header indices and print before printing data per ids
    if x == 0:
        id_index = data.index("id")
        company_index = data.index("company")
        tyc_index = data.index("totalyearlycompensation")
        # print desired headers
        print("{}\t{},{}".format(data[id_index], data[company_index], data[tyc_index]))
        continue  # skip to printing id's data

    # print/consider the top x id values
    if x <= 70000:
        print("{}\t{},{}".format(data[id_index], data[company_index], data[tyc_index]))
    else:
        break
