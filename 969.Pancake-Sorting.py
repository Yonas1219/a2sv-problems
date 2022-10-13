class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        output=[]
        m=len(A)
        f=len(A)-1
        for j in A:
            for i in range(len(A)):
                if A[i]==m:
                    A[:i+1]=A[i::-1]
                    output.append(len(A[:i+1]))
                    A[:f+1]=A[f::-1]
                    output.append(len(A[:f+1]))
                    m-=1
                    f-=1
        return output
