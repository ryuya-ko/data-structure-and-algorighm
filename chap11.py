from collections import deque
# from chap10 import *

def main():
    # test1()
    test2()

def test1():
    D = deque()
    print(D)
    D.append('A')
    D.append('B')
    D.append('C')
    print(D)
    D.pop()
    D.popleft()
    print(D)

def test2():
    X = ((((), 111, ()), 11, ((), 122, ())), 1, (((), 121, ()), 12, ((), 122, ())))
    depth_first_search(X)
    breadth_first_search(X)

def depth_first_search(T):
    D = deque()
    if len(T) > 0:
        D.append(T)
        show(D)
    while len(D) > 0:
        L, a, R = D.pop()
        show(D)
        print(a, end=', ')
        show(D)
        if len(L) > 0:
            D.append(L)
        if len(R)> 0:
            D.append(R)
            show(D)
    print()


def breadth_first_search(T):
    D = deque()
    if len(T) > 0:
        D.append(T)
        show(D)
    while len(D) > 0:
        L, a, R = D.popleft()
        show(D)
        print(a, end=', ')
        if len(L) > 0:
            D.append(L)
        if len(R) > 0:
            D.append(R)
            show(D)
    print()


def show(D):
    print('[', end='')
    for (L, a, R) in D:
        print(a, end='<-')
    print(']')

if __name__ == "__main__":
    main()