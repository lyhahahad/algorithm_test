def solution(n, results):
    answer = 0
    win=[set() for i in range(n)]
    lose=[set() for i in range(n)]
    print(win)
    print(lose)
    # seperate win, lose results
    #o(len(results))
    for i in range(n) :
        win[results[i][0]-1].add(results[i][1])
        lose[results[i][1]-1].add(results[i][0])
    print(win)
    print(lose)
    for i in range(n):
        print(i)
        for j in win[i]:
            print(win[j-1])
            win[i].union(win[j-1])
        for k in lose[i]:
            print(lose[k-1])
            lose[i].union(lose[k-1])

    for i in range(n):
        if(len(win[i].union(lose[i]))==n-1):
            print(i+1)
            answer +=1
    print(win)
    print(lose)
    return answer

#space 
#time
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))