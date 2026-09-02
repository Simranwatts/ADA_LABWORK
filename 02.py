from typing import List

class Sort:

    def merge_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0]
                          else right.pop(0))

        return result + left + right

    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)


# Driver Code
arr = list(map(int, input("Enter unsorted integers: ").split()))

s = Sort()

print("Original array:", arr)
print("Merge Sort:", s.merge_sort(arr.copy()))
print("Quick Sort:", s.quick_sort(arr.copy()))
