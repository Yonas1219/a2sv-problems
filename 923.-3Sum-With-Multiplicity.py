class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10**9+7
        c = Counter(arr)
        keys = sorted(c)
        N = len(keys)
        output = 0
        for i, num1 in enumerate(keys):
            j,k = i, N-1
            T = target-num1
            while j<=k:
                num2, num3 = keys[j],keys[k]
                if num2 + num3 < T:
                    j+=1
                elif num2 + num3 > T:
                    k-=1
                else:
                    if i<j<k:
                        output += c[num1]*c[num2]*c[num3]
                    elif i == j<k:
                        output += c[num1]*(c[num2]-1)/2*c[num3]
                    elif i<j == k:
                        output += c[num1]*c[num2]*(c[num3]-1)/2
                    else:
                        output += c[num1]*(c[num2]-1)*(c[num3]-2)/6
                    j+=1
                    k-=1
        return int(output%mod)
                        
                        

                        
                
