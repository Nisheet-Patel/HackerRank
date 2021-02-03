from string import ascii_lowercase as al

def print_rangoli(size):
    rows = []
    for i in range(size-1,-1,-1):
        row = []
        for j in al[i:size][::-1]:
            row.append("-".join(j))
        rows.append("-".join(row+row[::-1][1:]))
    print("\n".join([x.center(len(rows[size-1]),'-') for x in rows]))
    print("\n".join([x.center(len(rows[size-1]),'-') for x in rows[::-1][1:]]))    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

'''
import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print(L)
print('\n'.join(L[:0:-1]+L))
'''