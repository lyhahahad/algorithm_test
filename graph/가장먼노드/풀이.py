def solution(n, edge):
    answer = 0
    root = [1]
    queue = []
    visited_node = []
    enqueue(queue,root)
    while(queue_isNotEmpty(queue)):
        visiting_node = dequeue(queue)
        print(visiting_node)
        enqueue(queue, childs(edge, visiting_node, visited_node,queue))
        print(queue)
        visited_node.append(visiting_node)
        if(childsnodenum(edge, visiting_node, visited_node,queue)==0):
            print(1111111)
            answer+=1
        elif(answer>=1) : 
            answer=0
        # break
    return answer

def enqueue(queue,i):
    queue.extend(i)
    return

def dequeue(queue):
    return(queue.pop(0))

def queue_isNotEmpty(queue):
    if(len(queue)==0):
        return False
    return True

def childs(edge, visiting_node, visited_node,queue):
    child_list=[]
    for i in edge:
        if (visiting_node in i):
            for j in i:
                if(visiting_node != j and j not in visited_node and j not in queue):
                    child_list.append(j)
    return child_list

def childsnodenum(edge, visiting_node, visited_node,queue):
    result = 0
    for i in edge:
        if (visiting_node in i):
            for j in i:
                if(visiting_node != j and j not in visited_node and j not in queue):
                    result +=1
    return result


n=6
edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# for i in range(0,8):
#     print(edge.pop(0))
# print(edge)
print(solution(n,edge))