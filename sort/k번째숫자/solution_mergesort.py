###
# merge sort
# 기본원리 : divide and conquer 방식으로 정렬한다.
# mid를 기준으로 계속 나누고 merge한다.
# 시간 복잡도 : T(n) = 2T(n/2) + θ(n)
# ###

def merge_sort(arr, f, l,k):
    # f = first index, l = last Index
    if (k==9):
        return
    print(f, ",", l)
    mid = 1 + (l-f)//2
    if(f < l):
        merge_sort(arr, f, mid-1,k+1)
        merge_sort(arr, mid, l,k+1)
        i = f
        j = mid
        while(i < mid):
            if arr[i] > arr[j]:
                arr = arr[:i]+arr[j:j+1]+arr[i:j]+arr[j+1:]
                j += 1
                i += 1
            else:
                i += 1
        print(arr)

# def merge(arr, f, mid, l):
#     i = f
#     j = mid
#     while(i<mid):
#         if arr[i]>arr[j]:
#             arr = arr[:i]+arr[j:j+1]+arr[i:j]+arr[j+1:]
#             j+=1
#             i+=1
#         else :
#             i+=1
#     print(arr)
#     return arr


print(merge_sort([5, 1, 2, 6, 3, 7, 4], 0, 6,0))

# def solution(array, commands):
#     answer = []
#     for i in range(len(commands)):
#         array_len = commands[i][1]-commands[i][0]+1
#         answer.append(merge_sort(array[commands[i][0]-1:commands[i][1]],0,array_len-1)[commands[i][2]-1])

# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(array, commands))
