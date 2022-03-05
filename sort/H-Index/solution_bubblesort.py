#O(N^2)
def bubble_sort(arr,n):
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]<arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def solution(citations):
    answer = 0
    n = len(citations)
    citations = bubble_sort(citations, n)
    for i in range(n):
        if citations[i]<i+1:
            break
        answer = i+1
    return answer

# 테스트 1 〉	통과 (13.92ms, 10.2MB)
# 테스트 2 〉	통과 (37.93ms, 10.3MB)
# 테스트 3 〉	통과 (35.57ms, 10.2MB)
# 테스트 4 〉	통과 (25.08ms, 10.2MB)
# 테스트 5 〉	통과 (37.96ms, 10.2MB)
# 테스트 6 〉	통과 (48.61ms, 10.1MB)
# 테스트 7 〉	통과 (7.00ms, 10.3MB)
# 테스트 8 〉	통과 (0.22ms, 10.2MB)
# 테스트 9 〉	통과 (0.81ms, 10.1MB)
# 테스트 10 〉	통과 (9.59ms, 10.1MB)
# 테스트 11 〉	통과 (65.61ms, 10.1MB)
# 테스트 12 〉	통과 (2.85ms, 10.2MB)
# 테스트 13 〉	통과 (46.86ms, 10.2MB)
# 테스트 14 〉	통과 (41.92ms, 10.2MB)
# 테스트 15 〉	통과 (48.03ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)