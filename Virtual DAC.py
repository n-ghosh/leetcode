# Virtual DAC

# no, this is a binary converter..
def virtDAC(num):
    n = 0
    for i in range(7, 0, -1):
        if (num / 2 != 0):
            n += 10**i
    return n


x = 1023

print(virtDAC(x))