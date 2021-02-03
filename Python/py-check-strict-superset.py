A = set(map(int, input().split()))
n = int(input())
NN = set()
for i in range(n): 
    for j in map(int, input().split()): NN.add(j)
print(A.issuperset(NN))