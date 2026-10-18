# pow() in double loses exactness for x*x > 2^53, so (long long)(pow(x,2)-4)/(x+2) may be x-3 for large addresses.
import random
random.seed(1)
for lo,hi in [(0x400000,0x4000000),(0x4000000,0x8000000),(0x8000000,0x80000000),(0x56000000,0x57000000)]:
    bad=0
    for _ in range(20000):
        x=random.randrange(lo,hi); q=int(float(x)*float(x)-4.0)//(x+2); bad+=q!=x-2
    print(hex(lo),hex(hi),'fraction giving s-1 instead of s:',bad/20000)
