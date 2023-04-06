import time

def sort(num_list):
    start = time.time()

    for i in range(1, len(num_list)):
        for j in range(i,0,-1):
            if num_list[j-1] > num_list[j]:
                # temp = num_list[j-1]
                # num_list[j-1] = num_list[j]
                # num_list[j] = temp
                num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
    print(f"{time.time() - start:.5f} sec")
    print(num_list)