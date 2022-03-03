def insertionsort(arr,n):
    for i in range(1,n):
        n = arr[i]
        for j in range(i):
            if n<arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def solution(citations):
    answer = 0
    n = len(citations)
    citations = insertionsort(citations, n)
    for i in range(n):
        if citations[i]>n-i:
            break
        if citations[i] == n-i:
            answer = n-i
    return answer