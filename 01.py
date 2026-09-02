from typing import List

# Binary Search using Divide and Conquer
def search(nums: List[int], target: int) -> int:
    def binary_search(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid - 1)

    return binary_search(0, len(nums) - 1)


# Power Function using Divide and Conquer
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0

    if n < 0:
        return 1.0 / myPow(x, -n)

    half = myPow(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


# Driver Code
if __name__ == "__main__":

    nums = list(map(int, input(
        "Enter space separated integers: "
    ).split()))

    target = int(input("Enter target: "))

    index = search(nums, target)

    print("Index of", target, ":", index)

    x = float(input("\nEnter base (x): "))
    n = int(input("Enter exponent (n): "))

    result = myPow(x, n)

    print(f"{x}^{n} = {result}")
