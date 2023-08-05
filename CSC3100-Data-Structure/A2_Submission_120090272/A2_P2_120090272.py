def merge_sort(data,start,end):
    if end > start:
        mid = int((start + end)/2)
        merge_sort(data,start, mid)
        merge_sort(data, mid+1, end)
        merge(data,start,end,mid)

def merge(data,start,end,mid):
    global num
    if start == mid:
        if data[start] > data[end]:
            num += 1
            data[start],data[end] = data[end],data[start]
        return 
    left_list = data[start:mid+1]
    right_list = data[mid+1: end+1]
    left_i = 0
    right_i = 0
    index = start
    left_len = len(left_list)
    right_len = len(right_list)

    while left_i < left_len and right_i < right_len:
        if left_list[left_i] <= right_list[right_i]:
            data[index] = left_list[left_i]
            left_i += 1
            index += 1
        else:
            data[index] = right_list[right_i]
            right_i += 1 
            index += 1
            num += left_len - left_i

    if left_i < left_len:
        data[index:end+1] = left_list[left_i:]
    if right_i < right_len:
        data[index:end+1] = right_list[right_i:]

n= int(input())
global num
num = 0
data = input().split(' ')
data = [ int(i) for i in data]
merge_sort(data, 0, n-1)
print(num)


