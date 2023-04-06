import time


def sort(num_list):
    start = time.time()
    mergesort(num_list, 0, len(num_list))
    print(f"병합정렬 소요시간 : {time.time() - start:.5f} sec")
    print(num_list)

def mergesort(num_list, left, right):
    if left < right:
        mid = int((left + right) / 2)

        mergesort(num_list, left, mid)
        mergesort(num_list, mid+1, right)
        merge(num_list, left, mid+1, right+1)


def merge(num_list, left, mid, right):
    left_list = num_list[left:mid]
    right_list = num_list[mid:right]

    i, j, k = 0, 0, left
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            num_list[k] = left_list[i]
            i += 1
        else:
            num_list[k] = right_list[j]
            j += 1
        k += 1

    while i < len(left_list):
        num_list[k] = left_list[i]
        k += 1
        i += 1

    while j < len(right_list):
        num_list[k] = right_list[j]
        k += 1
        j += 1
