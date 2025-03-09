# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ans = []
   
        # edge case
        if (pairs == []):
            return []

        # pairs[:]: create a copy of pairs (by default, python passes by reference)
        ans.insert(0, pairs[:])

        for i in range(1, len(pairs)):
            hold = pairs[i]

            j = 1
            while i - j >= 0 and pairs[i-j].key > hold.key:
                pairs[i-j+1] = pairs[i-j]
                j+=1
            
            pairs[i-j+1] = hold

            ans.insert(i, pairs[:])

        return ans