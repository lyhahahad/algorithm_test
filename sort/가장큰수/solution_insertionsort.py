def insertionsort(arr,n):
    for i in range(1,n):
        n = arr[i]
        for j in range(i):
            if int(n[0])>int(arr[j][0]):
                arr[i], arr[j] = arr[j], arr[i]
#보완

    return arr

def solution(numbers):
    answer = ''
    return answer

print(insertionsort([str(i) for i in [6, 10, 2]], 3))
print(insertionsort([str(i) for i in [3, 30, 34, 5, 9]],5))
