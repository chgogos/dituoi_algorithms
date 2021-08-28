from random import shuffle
from icecream import ic

def max_sub(arr):
    '''
    
    O(n^2) 
    '''
    n = len(arr)
    m = 0
    start_pos, end_pos = 0, 0
    for j in range(n):
        for k in range(j, n):
            s = 0
            for i in range(j, k):
                s += arr[i]
            # ic(s, j, k)
            if s > m:
                m = s
                start_pos = j
                end_pos = k - 1
    return m, start_pos, end_pos


