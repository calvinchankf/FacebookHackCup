"""
    1st approach:
    Time    
    Space   
"""
def f(N, I, O):
    res = [N * ['N'] for _ in range(N)]
    for i in range(N):
        res[i][i] = 'Y'
        _i = i
        while _i - 1 >= 0:
            if O[_i] == 'Y' and I[_i-1] == 'Y':
                res[i][_i-1] = 'Y'
            else:
                break
            _i -= 1
        _i = i
        while _i + 1 < N:
            if O[_i] == 'Y' and I[_i+1] == 'Y':
                res[i][_i+1] = 'Y'
            else:
                break
            _i += 1
    
    final = []
    for sub in res:
        final.append(''.join(sub))

    return final

# a = 5
# b = 'YNNYY'
# c = 'YYYNY'
# print(f(a, b, c))

# a = 3
# b = 'NYY'
# c = 'YYN'
# print(f(a, b, c))

# a = 10
# b = 'NYYYNNYYYY'
# c = 'YYNYYNYYNY'
# print(f(a, b, c))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
fRead = open("travel_restrictions_input.txt", "r")
fWrite = open("travel_restrictions_output.txt", "w")

# t = int(raw_input())  # read a line with a single integer
t = int(fRead.readline())

for i in range(1, t + 1):
    # n = int(raw_input())
    # incoming = raw_input()
    # outgoing = raw_input()
    n = int(fRead.readline())
    incoming = fRead.readline()
    outgoing = fRead.readline()

    res = f(n, incoming, outgoing)

    # print("Case #{}:".format(i))
    # for s in res:
    #     print(s)
    fWrite.write('Case #{}:\n'.format(i))
    for s in res:
        fWrite.write('{}\n'.format(s))

fWrite.close()