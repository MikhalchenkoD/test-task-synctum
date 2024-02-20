def binary_search(arr, item, low, high):
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_rotation_index(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess > arr[high]:
            low = mid + 1
        else:
            high = mid

    return low


def broken_search(nums, target) -> int:
    rotation_index = find_rotation_index(nums)

    if rotation_index == 0:
        return binary_search(nums, target, 0, len(nums) - 1)
    elif target >= nums[0]:
        return binary_search(nums, target, 0, rotation_index - 1)
    else:
        return binary_search(nums, target, rotation_index, len(nums) - 1)


# def test():
#     arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
#     assert broken_search(arr, 19) == 0
#
#
# test()


def get_data_from_file():
    with open('input.txt', 'r') as f:
        data_from_file = f.readlines()
        data_list = []
        count = 0

        for data in data_from_file:
            data = data.strip()

            if count == 1:
                data_list.append(int(data))
            elif count == 2:
                nums = []
                for i in data.split():
                    nums.append(int(i))
                data_list.append(nums)
            count += 1

    return data_list


def main():
    data = get_data_from_file()
    result = broken_search(data[1], data[0])

    return result



print(main())