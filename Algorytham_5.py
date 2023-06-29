def selection_sort_descending(my_list):
    length = len(my_list)
    for i in range(length):
        max_index = i
        for j in range(i + 1, length):
            if my_list[j] > my_list[max_index]:
                max_index = j

        my_list[i], my_list[max_index] = my_list[max_index], my_list[i]

    print(f"selection sort result: {my_list}")


test_list = [4, 2, 8, 1, 5, 9]

selection_sort_descending(test_list)


def bubble_sort_descending(my_list):
    length = len(my_list)
    for i in range(length):
        for j in range(0, length - i - 1):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list


test_list_2 = [64, 34, 25, 12, 22, 11, 90]

bubble_sorted_list = bubble_sort_descending(test_list_2)
print(f"bubble sort result: {test_list_2}")



def insertion_sort_descending(arr):
    for index in range(1, len(arr)):
        current_value = arr[index]
        j = index - 1
        while j >= 0 and current_value > arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = current_value
            j -= 1

    return arr


list_to_sort = [12, 11, 13, 5, 6]
sorted_list = insertion_sort_descending(list_to_sort)
print(f"insertion sort result: {sorted_list}")



def merge_sort_descending(my_array):
    if len(my_array) <= 1:
        return my_array

    middle = len(my_array) // 2
    left = merge_sort_descending(my_array[:middle])
    right = merge_sort_descending(my_array[middle:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged
#merged arr

arr = [10, 21, 9, 5, 3, 7]
sorted_arr = merge_sort_descending(arr)
print(f"merge sort result: {sorted_arr}")