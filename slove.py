import numpy as np
import sys

def input_file(path):
    with open(path, "r") as f:
        # There is a blank between start and end [5 9]
        content = f.read().splitlines()
    return content

def output_file(cover):
    with open(sys.argv[2],"w") as f:
        f.write(cover)

# this fuction got help from Rishabh
def calc_coverage(time_list):
    coverage = 0
    old_start, old_end = time_list[0]
    for i in range(1, len(time_list)):
        start, end = time_list[i]
        if start < old_end:
            prev_end = max(end, old_end)
        else:
            coverage += (old_end - old_start)
            prev_start, prev_end = start, end
        if i == len(time_list) - 1:
            coverage += (prev_end - old_start)
    return coverage



'''
def get_coverage(num,time_list):
    axis = np.zeros(time_list[-1][1])
    for i in range(0,num):
        single = time_list[i]
        s = int(single[0])
        e = int(single[1])
        axis[s:e] += 1

    cover = 0
    for j in range(0,len(axis)):
        if axis[j] > 0:
            cover += 1
    return cover
'''

def get_overlap(time_list,index1,index2):
    single1 = time_list[index1]
    np.array(single)
    s1 = int(single1[0])
    e1 = int(single1[1])

    single2 = time_list[index2]
    np.array(single)
    s2 = int(single2[0])
    e2 = int(single2[1])

    overlap = min(e1, e2) - s2
    return overlap


def get_contribute(num,time_list):
    overlap = get_overlap(time_list,0,1)
    length = time_list[0][1] - time_list[0][0]
    index = 0
    contribution = length - overlap

    for i in range(1,num-1):
        overlap = get_overlap(time_list,i-1,i) + get_overlap(time_list,i,i+1)

        length = time_list[i][1] - time_list[i][0]

        if contribution > length - overlap:
            contribution = length - overlap

            index = i

        if contribution == 0:
            index = i
            break
    return index,contribution


# read input
read = input_file(sys.argv[1])

# clean input
num = int(read[0])
list = read[1:]

# sort the timeslot
sort_list = []
for i in list:
    single = i.split(" ", 1)
    sort_list.append([int(single[0]), int(single[1])])
sort_list.sort()

# get contribution and find out which one should be dismiss
index,contribution = get_contribute(num,sort_list)
sort_list.pop(index)

# get coverage
cover = calc_coverage(sort_list)
cover = str(cover)
# output file
output_file(cover)
