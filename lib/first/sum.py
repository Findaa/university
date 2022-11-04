import time

def timer(n):
    start = time.time()
    i = int(0)
    r = int(0)

    while i < n + 1:
        r = r + i
        i = i + 1

    print(r)
    return time.time() - start

print(timer(int(input("Number: "))))
