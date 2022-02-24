#원리 : 우측배열에서 하나하나 가져와 좌측 배열은 sorted된 상태로 만든다.
def insertionsort(arr,n):
    for i in range(1,n):
        n = arr[i]
        for j in range(i):
            if n<arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        array_len = commands[i][1]-commands[i][0]+1
        answer.append(insertionsort(array[commands[i][0]-1:commands[i][1]],array_len)[commands[i][2]-1]) 
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.1MB)