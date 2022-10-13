class Solution: 
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            sorted = i
            for j in range(i+1, len(arr)):
                if arr[sorted] > arr[j]:
                    sorted = j
            arr[i], arr[sorted] = arr[sorted], arr[i]
                
        return arr 
