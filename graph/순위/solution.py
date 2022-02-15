def solution(n, results):
    answer = 0
    win=[set() for i in range(n)]
    lose=[set() for i in range(n)]

    for i in range(n) :
        win[results[i][0]-1].add(results[i][1])
        lose[results[i][1]-1].add(results[i][0])

# 아래 과정은 a->b b->c에서 a->c를 찾을 수 있는 풀이이다.
# [2,1], [3,2], [4,3], [5,4] 해당 result를 가질 때 오류가 발생한다.
# 이 부분에 dfs 적용하기.
# 인접 리스트로 dfs 구현하기.
    for i in range(n):
        for j in win[i]:
            win[i] = win[i].union(win[j-1])
        for k in lose[i]:
            lose[i] = lose[i].union(lose[k-1])

    for i in range(n):
        if(len(win[i].union(lose[i]))==n-1):
            answer +=1
    return answer

#space 
#time

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))