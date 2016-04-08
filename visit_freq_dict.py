from column_index_map import *
import sys

from collections import defaultdict

def visit_frq(inp_data):
    visit = defaultdict(int)
    prev_id = ''
    fhand = open(inp_data)
    fhand.readline()
    count = 0
    total = 0

    for line in fhand:
        row_data =  line.strip().split(',')
        curr_id = row_data[PID_IDX]

        if prev_id != '' and curr_id != prev_id:
            total = total + 1
            print total

            if count >= 7:
                visit[7] = visit[7] + 1
            else:
                visit[count] = visit[count] + 1
            count = 0
        count += 1
        prev_id = curr_id
    return visit



print visit_frq('/Users/vikhyati/PycharmProjects/LengthOfStay/OSHPD_CHF_LOS.csv')

