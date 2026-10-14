"""
GenomicRangeQuery (Codility - Prefix Sums)

A DNA sequence can be represented as a string consisting of the letters A, C, G and T,
which correspond to the types of successive nucleotides in the sequence. Each nucleotide
has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact
factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form:
What is the minimal impact factor of nucleotides contained in a particular part of the given
DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N
characters. There are M queries, which are given in non-empty arrays P and Q, each consisting
of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of
nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:
* The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice),
  whose impact factors are 3 and 2 respectively, so the answer is 2.
* The part between positions 5 and 5 contains a single nucleotide T, whose impact factor
  is 4, so the answer is 4.
* The part between positions 0 and 6 (the whole string) contains all nucleotides, in
  particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:
    def solution(S, P, Q)
that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q
consisting of M integers, returns an array consisting of M integers specifying the consecutive
answers to all queries.

For example, given S = CAGCCTA and P, Q as above, the function should return [2, 4, 1].

Write an efficient algorithm for the following assumptions:
* N is an integer within the range [1..100,000];
* M is an integer within the range [1..50,000];
* each element of arrays P and Q is an integer within the range [0..N - 1];
* P[K] ≤ Q[K], where 0 ≤ K < M;
* string S consists only of upper-case English letters A, C, G, T.
"""


# ---------------------------------------------------------------------------
# Approach 1: Brute force (my first attempt) -- correct, but fails performance
# ---------------------------------------------------------------------------
def solution_brute(input_string, P, Q):
    impact_dict = {"A": 1, "C": 2, "G": 3, "T": 4}

    res = []
    for i in range(len(P)):
        # ⚠️ Slice end is Q[i]+1 because Q is inclusive and Python slices are exclusive.
        # ⚠️ Slicing also copies the substring, which is an extra O(len) per query.
        dna_sequence = input_string[P[i]:Q[i] + 1]

        # Scan the whole range for the min impact factor
        min_nucleotide_val = float('inf')
        for dna_nucleotide in dna_sequence:
            min_nucleotide_val = min(min_nucleotide_val, impact_dict[dna_nucleotide])
            # (could break early once it hits 1, but the worst case is still the same)

        res.append(min_nucleotide_val)

    return res

# ⚠️ Why it fails: each query scans up to N chars, so the total is O(N * M).
#    Worst case 100,000 * 50,000 = 5 billion ops. TLE.
# Time: O(N * M), Space: O(N) for the slice


# ---------------------------------------------------------------------------
# Approach 2: Prefix counts per nucleotide -- O(N + M)
# ---------------------------------------------------------------------------
# Key idea: the answer only depends on WHICH nucleotides appear in the range,
# not where. With only 4 types, precompute running counts for each one. Then
# "is there an A in [p, q]?" is a single subtraction.
def solution(S, P, Q):
    n = len(S)

    # prefix[c][i] = count of nucleotide c in S[0:i] (the first i chars)
    # ⚠️ Size n+1 with prefix[c][0] = 0, so the range count is a clean subtraction.
    prefix = {c: [0] * (n + 1) for c in "ACGT"}

    for i, ch in enumerate(S):
        # Carry forward all 4 counts, then bump the current char
        for c in "ACGT":
            prefix[c][i + 1] = prefix[c][i]
        prefix[ch][i + 1] += 1

    res = []
    for p, q in zip(P, Q):
        # Count of c in S[p..q] inclusive = prefix[c][q+1] - prefix[c][p]
        # ⚠️ q+1, not q. Q is inclusive, prefix is exclusive.
        # Check in impact order: the first one present is the minimum.
        if prefix["A"][q + 1] - prefix["A"][p] > 0:
            res.append(1)
        elif prefix["C"][q + 1] - prefix["C"][p] > 0:
            res.append(2)
        elif prefix["G"][q + 1] - prefix["G"][p] > 0:
            res.append(3)
        else:
            res.append(4)  # ⚠️ No A/C/G means it must be all T. No need to check.

    return res

# Trace for S = "CAGCCTA", query (2, 4) -> "GCC":
#   A: prefix[5] - prefix[2] = 1 - 1 = 0  -> no A
#   C: prefix[5] - prefix[2] = 3 - 1 = 2  -> answer 2
#
# Time: O(N + M)  (4*N to build + O(1) per query)
# Space: O(N)


if __name__ == "__main__":
    S, P, Q = "CAGCCTA", [2, 5, 0], [4, 5, 6]
    print(solution_brute(S, P, Q))  # [2, 4, 1]
    print(solution(S, P, Q))        # [2, 4, 1]