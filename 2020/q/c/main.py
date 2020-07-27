from collections import defaultdict

"""
    1st approach:
    Time    
    Space   
"""
def f(N, P, H):
    ht = defaultdict(list)
    cands = []
    for i in range(N):
        p, h = P[i], H[i]
        ht[p].append((h, 1))
        ht[p-h].append((h, -1))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Facebook Hacker Cup problems.
fRead = open("alchemy_input.txt", "r")
fWrite = open("alchemy_output.txt", "w")

t = int(fRead.readline())
for i in range(1, t + 1):
    n = int(fRead.readline())
    s = fRead.readline()
    res = 'Y' if f(n, s) == True else 'N'
    fWrite.write('Case #{}: {}\n'.format(i, res))

fWrite.close()