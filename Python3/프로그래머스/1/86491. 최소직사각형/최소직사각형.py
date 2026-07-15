def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w, h in sizes:
        w_val = max(w, h)
        h_val = min(w, h)
        
        max_w = max(max_w, w_val)
        max_h = max(max_h, h_val)
            
    return max_w * max_h