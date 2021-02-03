input()
A = set(map(int,input().split()))
N = input()
for i in range(int(N)):
    fun = input().split()
    B = set(map(int,input().split()))
    eval("A.{}(B)".format(fun[0]))

print(sum(A))