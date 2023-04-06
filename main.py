import random as num
import sort.selection as sel
import sort.insertion as ins

num_list = []
while len(num_list) < 1000:
    temp = num.randint(1,1000)
    if temp in num_list:
        continue
    else:
        num_list.append(temp)

print("1. 선택정렬 Selection")
print("2. 버블정렬 Bubble")
print("3. 삽입정렬 Insertion")
print("4. 퀵정렬 Quick")
print("5. 병합정렬 Merger")
print("6. 힙정렬 Heap")

choice = int(input("입력(그 외 종료) : "))
print(num_list)

if choice == 1:
    sel.sort(num_list)

elif choice == 3:
    ins.sort(num_list)