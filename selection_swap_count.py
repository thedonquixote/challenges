class solution:

    def minSwaps(arr):
        n = len(arr)
        swaps = 0
        for i in range(n):
            for j in range(i, n):
                if arr[j] < arr[i]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    swaps += 1

        return arr, swaps


# Driver Code
arr = [8, 2, 3]
print(solution.minSwaps(arr))
