from random import shuffle
from icecream import ic

def max_sub(arr):
    '''
    για όλα τα ζεύγη ακεραίων j,k:  
    O(n^3)
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


if __name__ == "__main__":
    M = 3
    arr = list(range(-M, M + 1))
    shuffle(arr)
    print(" ".join(map(str, arr)))
    m, start_pos, end_pos = max_sub(arr)
    print(f"max={m} from={start_pos} to={end_pos}")
