def compute_lct(A, s):
    from itertools import combinations
    
    # Check if the dimension of s equals the number of rows of A
    if len(s) != A.nrows():
        raise ValueError("The dimension of s should equal the number of rows of A.")

    d = A.ncols()  # Dimension of the ambient space
    n = A.nrows()  # Number of hyperplanes
    def codim(W):
        return d - W.dimension()
    def s_function(W):
        # Compute sum of s_j for all hyperplanes H_j containing W
        return sum(s[j] for j in range(n)
                   if all(vector(A[j, :]).dot_product(v) == 0
                          for v in W.basis()))

    # Calculate all intersections
    intersections = []
    for r in reversed(range(1, n + 1)):
        for comb in combinations(range(n), r):
            submatrix = A[list(comb), :]
            intersection = submatrix.right_kernel()
            intersections.append(intersection)
    
    # Remove duplicate intersections
    L = list(uniq(intersections))
    
    # Compute lambda as the minimum of codim(W) / s_function(W)
    lambda_min = min(codim(W) / s_function(W) for W in L)
    
    # Filter intersections where lambda achieves its minimum
    min_lambda_intersections = [W for W in L
                                if codim(W) / s_function(W) == lambda_min]
    
    # Calculate the maximum length of a chain of intersections
    def longest_chain_length(L):
        if not L:
            return 0
        
        lengths = [1] * len(L)
        
        for i in range(len(L)):
            for j in range(i):
                if all(v in L[i] for v in L[j].basis()):
                    lengths[i] = max(lengths[i], lengths[j] + 1)
        
        return max(lengths)
    
    m = longest_chain_length(min_lambda_intersections)
    
    return lambda_min, m
