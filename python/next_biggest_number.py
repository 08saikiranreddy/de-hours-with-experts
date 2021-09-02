#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.args[1])


def next_biggest_number(num):
    #TODO: Implement me!
    digits = list(map(int,str(num)))
    n = len(digits)
    for i in range(n-1,0,-1):
        if digits[i]>digits[i-1]:
            break
    if i==1 and digits[i]<=digits[i-1]:
        return -1
    x = digits[i-1]
    smalles = i
    for j in range(i+1,n):
        if digits[j]>x and digits[j]<digits[smalles]:
            smalles = j
    digits[smalles],digits[i-1] = digits[i-1],digits[smalles]
    x=0
    for j in range(i):
        x = x*10+digits[j]
    digits = sorted(digits[i:])
    for j in range(n-i):
        x = x*10+digits[j]
    return x

if __name__ == "__main__":
    main()



