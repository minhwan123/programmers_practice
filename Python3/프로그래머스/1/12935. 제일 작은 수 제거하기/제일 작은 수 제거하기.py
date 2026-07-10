def solution(arr):
    m = min(arr)
    
    if len(arr) > 2 :
        arr.remove(m)
    else : 
        arr = [-1]
    return arr