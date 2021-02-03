n = int(input())

for i in range(n):
    input()
    A = set(map(int, input().split()))
    input()
    B = set(map(int, input().split()))
    if A.issubset(B): print(True)
    else: print(False)