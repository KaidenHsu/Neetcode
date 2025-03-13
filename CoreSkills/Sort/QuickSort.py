# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def partition(self, arr, lo, hi):
        pivot = arr[hi].key

        i = lo - 1
        for j in range(lo, hi):
            if arr[j].key < pivot:
                i += 1 # in increases first
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i+1], arr[hi] = arr[hi], arr[i+1]
        return i+1            

    def quickSortHelper(self, arr, lo, hi):
        if lo < hi:
            pi = self.partition(arr, lo, hi)
            self.quickSortHelper(arr, lo, pi-1)
            self.quickSortHelper(arr, pi+1, hi)

        return arr

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs)-1)