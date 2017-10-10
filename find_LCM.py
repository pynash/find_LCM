#/usr/bin/env python


def minmax(a, b):
    x = min(a,b)
    y = max(a,b)
    return x, y

def factors(a, b):
    if a%2==0:
        a = a/2
        if b%2==0:
            b = b/2
            print a, b
            # return a, b, 2
        else:
            print a, b, 2
            # return a, b, 2
    else:
        if b%a==0:
            b = b/a
            c = a
            a = a/a
            print a, b
            # return a, b, c

def main():
    x1 = int(raw_input("please, enter the First Number: "))
    x2 = int(raw_input("please, enter the Second Number: "))
    a, b = minmax(x1, x2)

    factors(x1, x2)

main()

