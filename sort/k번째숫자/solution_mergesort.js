function solution(array, commands) {
    var answer = [];
    merge(0,len(array)-1,array)
    return answer;
}

function mergesort(low, high, array){
    var mid;
    if(low<high){
        mid = (low+high)/2;
        mergesort(low, mid)
        mergesort(mid+1,high)
        merge(low,mid,high,array)
    }
}

function merge(low, mid, high, S){
    let i=low, j=mid+1, k=low, U = new Array(len(S));;
    while (i <= mid && j <= high) {
        if (S[i] < S[j]) {
            U[k] = S[i]; 
            i++;
            } 
        else {
            U[k] = S[j]; j++; 
            }
                k++;
        }
    if (i > mid){
        U.slice(k,high+1)=S.slice(j,high+1)
    }
    else{
        U.slice(k,high+1)=S.slice(i,mid)
    }
    U.slice(low,high+1)=S.slice(low,high+1)    
    return S
}