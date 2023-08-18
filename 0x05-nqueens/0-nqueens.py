#!/usr/bin/python3
"""N Queens Problem solution"""
import sys


def NQueens(n):
    a = []
    b = []
    c = []
    i = 0

    def queens(n, i, a, b, c):
        if i < n:
            for j in range(n):
                if j not in a and i+j not in b and i-j not in c:
                    yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
        else:
            yield a

    solutions = queens(n, i, a, b, c)
    for solution in solutions:
        group = []
        for i in range(n):
            sub = []
            sub.append(i)
            sub.append(solution[i])
            group.append(sub)
        print(group)


if __name__ == "__main__":
    N = sys.argv[1]
    NQueens(int(N))
