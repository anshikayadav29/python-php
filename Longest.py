def longest_subarray_sum_k(arr, k):
    prefix_sum = {}
    curr_sum = 0
    max_len = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == k:
            max_len = i + 1

        if (curr_sum - k) in prefix_sum:
            max_len = max(max_len, i - prefix_sum[curr_sum - k])

        if curr_sum not in prefix_sum:
            prefix_sum[curr_sum] = i

    return max_len


# Example usage
arr = [10, 5, 2, 7, 1, 9]
k = 15
print("Length of longest subarray:", longest_subarray_sum_k(arr, k))
