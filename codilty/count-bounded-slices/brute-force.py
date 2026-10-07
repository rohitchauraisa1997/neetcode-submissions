# ***** PERFORMANCE FAILS ****

def solution(K, arr):
    arr_len = len(arr)
    count = 0
    # max_val = arr[0]
    # min_val = arr[0]

    for i in range(arr_len):
        max_val = arr[i]
        min_val = arr[i]

        for j in range(i, arr_len):
            max_val = max(max_val, arr[j])
            min_val = min(min_val, arr[j])
            
            diff = max_val-min_val
            if diff <= K:
                count += 1
            else: 
              break

    return count
