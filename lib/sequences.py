#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1
    fib_seq = []

    for _ in range(length):
        fib_seq.append(a)
        a, b = b, a + b

    print(fib_seq)