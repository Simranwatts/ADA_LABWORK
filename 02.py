from typing import List

class Sort:

    # Merge Sort using Divide and Conquer
    def merge_sort(self, arr: List[int]) -> List[int]:

        if len(arr) <= 1:
            return arr.copy()

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self._merge(left, right)

    # Merge two sorted arrays
    def _merge(self, left: List[int],
               right: List[int]) -> List[int]:

        result = []
        i = j = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    # Quick Sort using Divide and Conquer
    def quick_sort(self, arr: List[int]) -> List[int]:

        if len(arr) <= 1:
            return arr.copy()

        pivot = arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return (self.quick_sort(left)
                + middle
                + self.quick_sort(right))


# Driver Code
if __name__ == "__main__":

    arr = list(map(int, input(
        "Enter unsorted integers: "
    ).split()))

    sorter = Sort()

    print("Original array:", arr)

    print("Merge Sort:",
          sorter.merge_sort(arr))

    print("Quick Sort:",
          sorter.quick_sort(arr))
