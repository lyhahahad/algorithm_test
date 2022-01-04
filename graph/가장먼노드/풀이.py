def solution(n, edge):
    answer = 0
    root = 1
    queue = []
    visited_node = []
    enqueue(queue,root)
    while(not queue_isEmpty(queue)):
        visiting_node = dequeue(queue)
        enqueue(queue, childs(edge, visiting_node, visited_node))
        visited_node.append(visiting_node)
        print(visiting_node)
        print(visited_node)
        if(childsnodenum(edge, visiting_node, visited_node)==0):
            answer+=1
        elif(answer>=1) : 
            answer=0
        print(answer)
    return answer

def enqueue(queue,i):
    queue.append(i)
    return

def dequeue(queue):
    return(queue.pop(0))

def queue_isEmpty(queue):
    if(len(queue)==0):
        return True
    return False

def childs(edge, visiting_node, visited_node):
    child_list=[]
    for i in edge:
        if (visiting_node in i):
            for j in i:
                if(visiting_node != j):
                    child_list.append(j)
    return child_list

def childsnodenum(edge, visiting_node, visited_node):
    result = 0
    for i in edge:
        if (visiting_node in i):
            for j in i:
                if(visiting_node != j):
                    result +=1
    return result


n=6
edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))