import time
import timeit


def get_less(arr, pivot):
    less = []

    for i in arr:
        if i[1] == pivot[1] and i[2] == pivot[2] and i[0] < pivot[0]:
            less.append(i)
        elif i[1] == pivot[1] and i[2] < pivot[2]:
            less.append(i)
        elif i[1] > pivot[1]:
            less.append(i)
    return less


def get_greater(arr, pivot):
    greater = []

    for i in arr:
        if i[1] == pivot[1] and i[2] == pivot[2] and i[0] > pivot[0]:
            greater.append(i)
        elif i[1] == pivot[1] and i[2] > pivot[2]:
            greater.append(i)
        elif i[1] < pivot[1]:
            greater.append(i)
    return greater


def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = get_less(arr[1:], pivot)
    greater = get_greater(arr[1:], pivot)
    return quicksort(less) + [pivot] + quicksort(greater)


def get_data_from_file():
    with open('input.txt', 'r') as f:
        data_from_file = f.readlines()
        data_list = []

        for data in data_from_file:
            data = data.strip().split()

            if len(data) > 1:
                data[1], data[2] = int(data[1]), int(data[2])
                data_list.append(data)

    return data_list


def main():
    data = get_data_from_file()
    sorted_data = quicksort(data)

    for i in sorted_data:
        print(i[0])

if __name__ == '__main__':
    main()