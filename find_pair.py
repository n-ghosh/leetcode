# HW problem: in O(n lg n) time, find a pais of integers in an array that sum to a given value

def FINDPAIR(A, x):
    A = sorted(A) 
    i=1
    j = len(A)
    while i < j:
        sum = A[i] + A[j]
        if sum == x:
            return True 
        elif sum < x:
            i=i+1 
        else: # sum > x
            j=j-1 
    return False