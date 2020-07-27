"""
    1st approach:
    Time    
    Space   
"""
def f():
    pass

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Facebook Hacker Cup problems.
fRead = open("in.txt", "r")
fWrite = open("out.txt", "w")

t = int(fRead.readline())
for i in range(1, t + 1):
    n = int(fRead.readline())
    incoming = fRead.readline()
    outgoing = fRead.readline()
    res = f(n, incoming, outgoing)
    fWrite.write('Case #{}:\n'.format(i, res))

fWrite.close()