## I ##

s = input()
if set([x.isalnum() for x in s if x.isalnum()]): print(True)
else: print(False)
if set([x.isalpha() for x in s if x.isalpha()]): print(True)
else: print(False)
if set([x.isdigit() for x in s if x.isdigit()]): print(True)
else: print(False)
if set([x.islower() for x in s if x.islower()]): print(True)
else: print(False)
if set([x.isupper() for x in s if x.isupper()]): print(True)
else: print(False)

## discussions ##

'''
str = input()
print (any(c.isalnum()  for c in str))
print (any(c.isalpha() for c in str))
print (any(c.isdigit() for c in str))
print (any(c.islower() for c in str))
print (any(c.isupper() for c in str))
'''

'''
s = input()
for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(method(c) for c in s))
'''

'''
print("\n".join([str(any(i)) for i in (list(zip(*[[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in input()])))]))
'''