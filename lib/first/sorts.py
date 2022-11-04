import random
import time

def randoms(size):
    i = 0
    numbers = []
    while i < size:
        numbers.append(random.random())
        i = i + 1
    print(numbers)
    return numbers


def properRandoms(size):
    numbers = random.sample(range(0, 100), size)
    print(numbers)
    return numbers

def bubble(data):
    start = time.time()
    n = len(data)

    while n > 1:
        for i in range(1, n):
            if data[i] < data[i - 1]:
                tmp = data[i]
                data[i] = data[i - 1]
                data[i - 1] = tmp

        n = n - 1
    end = (time.time() - start)
    print(end)
    return data

def main():
    data = properRandoms(10)
    print("***** Randoms *****")
    print(data)
    print("***** Bubble *****")
    bubble(data)
    print(data)

main()