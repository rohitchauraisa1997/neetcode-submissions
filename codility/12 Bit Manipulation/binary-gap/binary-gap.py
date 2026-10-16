"""
BinaryGap (Codility)

A binary gap within a positive integer N is any maximal sequence of consecutive
zeros that is surrounded by ones at both ends in the binary representation of
N.

For example, number 9 has binary representation 1001 and contains a binary gap
of length 2. The number 529 has binary representation 1000010001 and contains
two binary gaps: one of length 4 and one of length 3. The number 20 has binary
representation 10100 and contains one binary gap of length 1. The number 15 has
binary representation 1111 and has no binary gaps. The number 32 has binary
representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary
representation 10000010001 and so its longest binary gap is of length 5. Given
N = 32 the function should return 0, because N has binary representation
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].

My test values (N, binary, expected):
    9    1001        2
    529  1000010001  4
    20   10100       1
    15   1111        0
"""

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
            
