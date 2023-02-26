import time
import random


def sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    end_time = time.time()
    return found, end_time - start_time


def ordered_sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    end_time = time.time()
    return found, end_time - start_time


def binary_search_iterative(a_list, item):
    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if a_list[mid] == item:
            found = True
        else:
            if item < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    end_time = time.time()
    return found, end_time - start_time


def binary_search_recursive(a_list, item):
    start_time = time.time()
    if len(a_list) == 0:
        end_time = time.time()
        return False, end_time - start_time
    else:
        mid = len(a_list) // 2
        if a_list[mid] == item:
            end_time = time.time()
            return True, end_time - start_time
        else:
            if item < a_list[mid]:
                return binary_search_recursive(a_list[:mid], item)
            else:
                return binary_search_recursive(a_list[mid + 1:], item)


def main():
    lists = {}
    for size in [500, 1000, 10000]:
        lists[size] = []
        for i in range(100):
            lists[size].append([random.randint(0, 100000) for i in range(size)])

    for size, arrs in lists.items():
        print(f"Size {size}:")
        for func in [sequential_search, ordered_sequential_search, binary_search_iterative, binary_search_recursive]:
            total_time = 0
            for a_list in arrs:
                a_list.sort()
                result, time_taken = func(a_list, -1)
                total_time += time_taken
            print(f"{func.__name__.replace('_', ' ').title()} took {total_time/100:.7f} seconds to run, on average.")

if __name__ == "__main__":
    main()