def solution(n, edge):
    answer = 0
    #다리
    edge
    #시작점
    root = 1
    #다음 방문할 곳 넣을 큐
    queue = []
    #이미 방문한 곳 넣을 리스트
    visited_node = []
    #root 넣고 시작.
    enqueue(root)
    while(queue.isNotEmpty){
        visiting_node = dequeue()
        #visited_node에 있는 노드는 제외하고 enqueue 진행.
        enqueue(queue, childs(edge, visiting_node))
        visited_node.append(visiting_node)
        #depth를 표시할 만한 요소가 필요하다.
        #더 이상 childs가 없는 노드가 나오면 result에 +1을 한다.
        #만약 result가 1이상인 상황에서 그뒤에 childs가 enqueue 된다면 result를 0으로 바꾼다.
        if(visited_node.childsnodenum==0){
            answer+=1
        }
        if(answer>=1 and childsnode.num>0){
            answer=0
        }
    } 
    return answer

def enqueue(queue,i):
    queue.extend(i)
    return

def dequeue(queue):
    return(queue.pop(0))

def queue_isEmpty(queue):
    if(queue.length()==0):
        return True
    return false

# 방문한 노드의 자식 노드
# 이미 방문한 노드들은 제외.
def childs(edge, visiting_node):
    
# 방문한 노드의 자식 노드 숫자.
def childsnodenum(edge, visiting_node):
    return childs.length()