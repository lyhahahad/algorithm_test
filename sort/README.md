### 정렬 알고리즘 비교 분석<br>
https://www.geeksforgeeks.org/analysis-of-different-sorting-techniques/<br>

type|time Complexity best case|average|worst|Space Complexity<br>
Bubble|N|N^2|N^2|O(1)<br>
selection|N^2|N^2|N^2|O(1)<br>
insertion|N|N^2|N^2|O(1)<br>
Merge |NlogN|NlogN|NlogN|O(N)<br>
Quick |NlogN|NlogN|N^2|O(logN)<br>
Heap |NlogN|NlogN|NlogN|O(1)<br>
Radix |Nk|Nk|Nk|O(N + k)<br>
count|N + k|N + k|N + k|O(k)<br>
Bucket|N + k|N + k|N^2|O(N)<br>
<br>
Bubble,selection, insertion은 space Complexity가 O(1)으로 메모리 측면에서는 우수하지만 time Complexity는 O(N^2)으로 좋지 않다.<br>

# Insertion<br>
정렬되는 와중에 새로운 데이터가 들어와도 되는 정렬은 Insertion뿐이다. 정렬된 배열과 정렬되지 않은 배열을 분리하면서 진행하기 때문에 정렬되지 않는 쪽에 새로운 데이터를 추가하면 된다. 정렬이 완료된 정렬에서 진행할 때 가자 효율적<br>

# selection sort<br>
배열이 거의 정렬된 경우에는 selection sort를 사용하는 것이 가장 좋다. 
divide and conquer 방식을 사용한 알고리즘으로 merge와 quick가 있다.
같은 숫자가 나왔을 때 순서를 바꿀 수 있기 때문에 unstable하다.

# merge sort<br>
Merge는 time Complexity의 효율성을 올렸고 메모리 효율성은 줄었다. 즉 메모리를 더 써 time을 줄인 것이다. 비교 기반 정렬 알고리즘에서 유일하게 outplace를 사용한다.<br>
배열이 불규칙하고 메모리가 충분하다고 판단될 경우에는 merge sort를 사용하는 것이 좋다.<br>
# quick sort<br>
averagecase기준으로는 quick이 space도 비교적 덜쓰고 time은 같기 때문에 더 우수하다고 볼 수 있다. 같은 숫자가 나왔을 때 순서를 바꿀 수 있기 때문에 unstable하다. <br>
# heap sort<br>
가장 우수한 것은 in place heapsort이다.
메모리는 selection 등 space를 선택한 알고리즘과 같고 time은 메모리를 더 쓰면서 time효율성을 확보한 merge와 같다. 즉 어느하나 포기하지 않은 것이다. 다만 주어진 array를 heap자료 구조로 변경하는 heapify과정이 추가됐다. 같은 숫자가 나왔을 때 순서를 바꿀 수 있기 때문에 unstable하다.<br>

# Radix<br>
# count sort<br>
# bucket sort<br>

각각의 문제 모든 정렬로 다 풀어보고 효율성 직접 비교해보기.
