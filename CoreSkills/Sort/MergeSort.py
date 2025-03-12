# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # conquer (base cases)
        if (len(pairs) <= 1):
            return pairs
        
        if (len(pairs) == 2):
            if (pairs[1].key < pairs[0].key):
                pairs[0], pairs[1] = pairs[1], pairs[0]
            return pairs
        
        # divide
        mid = len(pairs)//2 # integer + floor()
        list1 = self.mergeSort(pairs[:mid])
        list2 = self.mergeSort(pairs[mid:])

        # merge
        mergedList = []

        i, j = 0, 0
        while (i < len(list1) and j < len(list2)):
            if list1[i].key <= list2[j].key:
                mergedList.append(list1[i])
                i += 1
            else:
                mergedList.append(list2[j])
                j += 1
        
        while (i < len(list1)):
            mergedList.append(list1[i])
            i += 1
        
        while (j < len(list2)):
            mergedList.append(list2[j])
            j += 1


        return mergedList