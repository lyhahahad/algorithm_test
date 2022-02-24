#원리 : 남은 것 중 가장 작은 요소를 찾아 정렬된 부분의 가장 뒤에 합친다.
def selection_sort(arr,n):
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        array_len = commands[i][1]-commands[i][0]+1
        answer.append(selection_sort(array[commands[i][0]-1:commands[i][1]],array_len)[commands[i][2]-1]) 
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)