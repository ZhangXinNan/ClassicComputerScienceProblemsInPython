
import time
from typing import Dict
from functools import lru_cache
from typing import Generator
memo: Dict[int, int] = {0: 0, 1: 1}


def fib2(n: int) -> int:
    if n < 2:
        # print("\t", n)
        return n
    y = fib2(n-1) + fib2(n-2)
    # print("\t", n, y)
    return y


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:
        return n
    return fib4(n-2) + fib4(n-1)


def fib5(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


def fib6(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


def main(n):
    print(n)
    t0 = time.time()
    # y2 = fib2(n)
    t2 = time.time()
    # print(t2 - t0, y2)
    y3 = fib3(n)
    t3 = time.time()
    print(t3 - t2, y3)
    y4 = fib4(n)
    t4 = time.time()
    print(t4 - t3, y4)
    y5 = fib5(n)
    t5 = time.time()
    print(t5 - t4, y5)


if __name__ == '__main__':
    print(fib2(5))
    print(fib2(10))
    main(600)
    fib_list = []
    for i in fib6(50):
        fib_list.append(i)
        if len(fib_list) % 10 == 0:
            print(fib_list[-10:])

