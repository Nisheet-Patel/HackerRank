# I Write
'''
if __name__ == '__main__':
    N = int(input())
    ml = list()
    for i in range(N):
        argument = list(input().split()) 
        
        if argument[0] == "insert": ml.insert(int(argument[1]),int(argument[2]))
        elif argument[0] == "print": print(ml)
        elif argument[0] == "sort": ml.sort()
        elif argument[0] == "remove": ml.remove(int(argument[1]))
        elif argument[0] == "append": ml.append(int(argument[1]))
        elif argument[0] == "pop": ml.pop() 
        elif argument[0] == "reverse": ml.reverse() 
'''
#I Get
'''
n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        print(cmd)
        eval("l."+cmd)
    else:
        print(l)
'''