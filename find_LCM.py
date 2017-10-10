#/usr/bin/env python


def minmax(a, b):
    x = min(a,b)
    y = max(a,b)
    return x, y

def factors(a, b):
    if a>1:
        if a%2==0:
            a = a/2
            if b%2==0 and b>1:
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
    else:

def read_number():
    while True:
        x = int(raw_input("please, enter number up 1: "))
        if x>1:
            return x

def main():
    x1 = read_number()
    x2 = read_number()
    a, b = minmax(x1, x2)



    factors(x1, x2)

main()

