// The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
// 9 1001 2
// 529 1000010001 4
// 20 10100 1
// 15 1111 0

def solution(N):
    binary = bin(N)
    binary = binary[2:]
    # print(binary)

    max_count = 0
    
    for index, char in enumerate(binary):
        if char == "1":
            count = 0
            if index+1 < len(binary):
                curr = index+1
                while curr < len(binary):
                    if binary[curr] == "0":
                        count+=1
                    else:
                        # only update max_count when 1 is encountered
                        max_count = max(count, max_count)
                        break
                    curr += 1
    
    # print(f"n ={N}, binary = {binary}, max_count = {max_count}")
    return max_count
            
