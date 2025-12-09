import timeit

def slow_function():
    data = list(range(1000))
    total = 0
    for i in data:
        for j in range (20):
            if i % 2 == 0:
                total += i
                break
    return total

def fast_function():
    data = list(range(1000))
    total = 0

    for x in data:
        if x % 2 == 0:
            total += x

    return total

if __name__ == "__main__":
    slow_time = timeit.timeit(slow_function, number=100)
    fast_time = timeit.timeit(fast_function, number=100)

    print(f"Slow function time: {slow_time}")
    print(f"Fast function time: {fast_time}")