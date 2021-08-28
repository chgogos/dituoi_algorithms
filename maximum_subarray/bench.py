import time
import random

from max_sub1 import max_sub as max_sub_cube


def array_generator(n, m, seed=None):
    """επιστροφή λίστας n τυχαίων ακεραίων στο διάστημα [-m,m]"""
    if seed:
        random.seed(seed)
    return [random.randint(-m, m) for _ in range(n)]


if __name__ == "__main__":
    arr = array_generator(1000, 10, 6174)
    t0 = time.time()
    m, s, e = max_sub_cube(arr)
    elapsed_time = time.time() - t0
    print(f"max={m} {s}-{e} {elapsed_time:.2f}sec")