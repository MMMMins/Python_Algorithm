import time


def sort(num_list):
    start = time.time()
    for i in range(len(num_list)):
        min_index = i
        for j in range(i+1, len(num_list)):
            if num_list[j] < num_list[min_index]:
                min_index = j

        min_value = num_list[min_index]
        num_list[min_index] = num_list[i]
        num_list[i] = min_value
    print(f"선택정렬 소요시간 : {time.time() - start:.5f} sec")
    print(num_list)


