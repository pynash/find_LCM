#/usr/bin/env python


def minmax(a, b):
    x = min(a,b)
    y = max(a,b)
    return x, y

def factors(a=1, b=1):
    if (a>1) and (b>1):
        if (a%2==0) and (b%2==0):
            return a/2, b/2, 2
        elif (a%2==0) and (b%2!=0):
            return a/2, b, 2
        elif (a%2!=0) and (b%2==0):
            if (b%a==0):
                return a/a, b/a, a
            else:
                return a, b/2, 2
        elif (a%2!=0) and (b%2!=0):
            if (b%a==0):
                return a/a, b/a, a
            else:
                return a/a, b, a
    elif (a>1) and (b==1):
        if (a%2==0):
            return a/2, b, 2
        else:
            return a/a, b, a
    elif (a==1) and (b>1):
        if (b%2==0):
            return a, b/2, 2
        else:
            return a, b/b, b
    else:
        return a, b, 1


def read_number():
    while True:
        x = int(raw_input("please, enter number up 1: "))
        if x>1:
            return x

def main():
    a = read_number()
    b = read_number()
    x1, x2 = minmax(a, b)

    lcm = []

    while True:
        x1, x2, x3 = factors(x1, x2)
        lcm.append(x3)
        if ((x1==1) and (x2==1)):
            break
    y = 1
    for i in range(len(lcm)):
        y *= lcm[i]
    print y, "IS LCM"

main()

