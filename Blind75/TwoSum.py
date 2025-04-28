# time complexity = O(n*log(n))
def binarySearch(arr: list[int], target: int, low: int, upp: int):
    mid = (low+upp)//2

    if mid == low and arr[mid] != target:
        return -1
    
    if mid == upp-1 and arr[mid] != target:
        return -1
    
    a = mid%len(arr)
    b = mid//len(arr)+1 if a != 0 else mid//len(arr)
    val = arr[a]+arr[b]

    if val == target:
        return mid

    if val < target:
        binarySearch(arr, target, mid+1, upp)
    elif val > target:
        binarySearch(arr, target, low, mid)
    
def twoSum(self, nums: list[int], target: int) -> list[int]:
    # O(n*log(n))
    nums.sort()

    # Perform binary search on the n^2,
    # 2-dimensional array O(log(n^2)) = O(log(n))
    # x axis: i, y axis: j
    

    # return i = x, j = y


def main():
    arr = [1, 2, 3]
    res = binarySearch(arr, 11, 0, pow(len(arr), 2))
    
    if res == -1:
        print("Not Found")
    else:
        a = res%len(arr)
        b = res//len(arr)+1 if a != 0 else mid//len(arr)
        print(a, b)



if __name__ == "__main__":
    main()