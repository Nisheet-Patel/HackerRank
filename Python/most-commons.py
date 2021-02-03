from collections import Counter

string = sorted(list(input()))
[print(*x) for x in Counter(string).most_common(3)]