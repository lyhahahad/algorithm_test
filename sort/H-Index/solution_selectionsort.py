#O(N^2)
def selection_sort(arr,n):
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index]<arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def solution(citations):
    answer = 0
    n = len(citations)
    citations = selection_sort(citations, n)
    for i in range(n):
        if citations[i]<i+1:
            break
        answer = i+1
    return answer


# 테스트 1 〉	통과 (6.96ms, 10.1MB)
# 테스트 2 〉	통과 (18.07ms, 10.2MB)
# 테스트 3 〉	통과 (14.83ms, 10.2MB)
# 테스트 4 〉	통과 (12.01ms, 10.2MB)
# 테스트 5 〉	통과 (19.25ms, 10.3MB)
# 테스트 6 〉	통과 (22.44ms, 10.3MB)
# 테스트 7 〉	통과 (3.30ms, 10.1MB)
# 테스트 8 〉	통과 (0.14ms, 10.1MB)
# 테스트 9 〉	통과 (0.70ms, 10.1MB)
# 테스트 10 〉	통과 (5.00ms, 10.2MB)
# 테스트 11 〉	통과 (26.34ms, 10.2MB)
# 테스트 12 〉	통과 (0.66ms, 10.1MB)
# 테스트 13 〉	통과 (23.46ms, 10.2MB)
# 테스트 14 〉	통과 (19.29ms, 10.2MB)
# 테스트 15 〉	통과 (25.77ms, 10.3MB)
# 테스트 16 〉	통과 (0.02ms, 10.2MB)