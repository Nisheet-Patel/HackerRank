n = int(input())
s = set(map(int, input().split()))

for i in range(int(input(":"))):
    fun = input().split()
    try: eval("s.{}({})".format(fun[0],fun[1]))
    except: eval("s.{}()".format(fun[0]))
print(sum(s))