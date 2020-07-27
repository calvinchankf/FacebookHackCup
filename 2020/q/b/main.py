"""
    1st approach:
    Time    
    Space   
"""
def f(N, S):
    na = 0
    nb = 0
    for c in S:
        if c == 'A':
            na += 1
        elif c == 'B':
            nb += 1
    half = N//2
    if na < half or nb < half:
        return False
    return True

# a = 3
# b = 'BAB'
# print(f(a, b))

# a = 3
# b = 'BBB'
# print(f(a, b))

# a = 5
# b = 'AABBA'
# print(f(a, b))

# a = 7
# b = 'BAAABAA'
# print(f(a, b))

# a = 11
# b = 'BBBAABAAAAB'
# print(f(a, b))

# a = 11
# b = 'BABBBABBABB'
# print(f(a, b))

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