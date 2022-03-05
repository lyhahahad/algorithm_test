#O(N^2)
def insertionsort(arr,n):
    for i in range(1,n):
        n = arr[i]
        for j in range(i):
            if n>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def solution(citations):
    answer = 0
    n = len(citations)
    citations = insertionsort(citations, n)
    for i in range(n):
        if citations[i]<i+1:
            break
        answer = i+1
    return answer

# 테스트 1 〉	통과 (8.78ms, 10.2MB)
# 테스트 2 〉	통과 (24.33ms, 10.1MB)
# 테스트 3 〉	통과 (20.09ms, 10.2MB)
# 테스트 4 〉	통과 (14.38ms, 10.1MB)
# 테스트 5 〉	통과 (24.58ms, 10.1MB)
# 테스트 6 〉	통과 (28.93ms, 10.2MB)
# 테스트 7 〉	통과 (4.29ms, 10.2MB)
# 테스트 8 〉	통과 (0.15ms, 10.2MB)
# 테스트 9 〉	통과 (0.51ms, 9.99MB)
# 테스트 10 〉	통과 (6.19ms, 10.2MB)
# 테스트 11 〉	통과 (35.48ms, 10.1MB)
# 테스트 12 〉	통과 (0.96ms, 10.3MB)
# 테스트 13 〉	통과 (28.65ms, 10.2MB)
# 테스트 14 〉	통과 (24.13ms, 10.1MB)
# 테스트 15 〉	통과 (31.08ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)