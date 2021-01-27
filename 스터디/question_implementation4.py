import sys


def direction(d, i):
    if i == 'L':
        if d == 'L':
            return 'D'
        elif d == 'R':
            return 'U'
        elif d == 'U':
            return 'L'
        elif d == 'D':
            return 'R'
    if i == 'D':
        if d == 'L':
            return 'U'
        elif d == 'R':
            return 'D'
        elif d == 'U':
            return 'R'
        elif d == 'D':
            return 'L'


N = int(input())
K = int(input())

apples = []
for _ in range(K):
    x, y = map(int, input().split())
    apples.append([x-1, y-1])

L = int(input())
moves = []
for _ in range(L):
    X, C = input.split()
    moves.append((int(X), C))

body = [[0, 0]]
dir = 'R'
time = 0

for move in moves:
    for i in range(move[0]):
        time += 1
        nowr, nowc = body[-1][0], body[-1][1]
        if dir == 'R':
            newr, newc = nowr, nowc+1
        elif dir == 'L':
            newr, newc = nowr, nowc-1
        elif dir == 'U':
            newr, newc = nowr-1, nowc
        elif dir == 'D':
            newr, newc = nowr+1, nowc

        if newr not in range(N) or newc not in range(N):
            print(time)
            sys.exit()
        if [newr, newc] in body:
            print(time)
            sys.exit()

        body.append([newr, newc])

        if [newr, newc] not in apples:
            body.pop(0)
        else:
            apples.remove([newr, newc])

    dir = direction(dir, move[1])
