def maximum_subarray_bf(nums):
    maxSum = -math.inf
    for i in range(len(nums)):
        tsum = 0
        for j in range(i, len(nums)):
            tsum += nums[j]
            maxSum = max(maxSum, tsum)

    return maxSum

def maximum_subarray_crossing_sum(nums, l, m, h):
    pass

    curr = best_left_sum = best_right_sum = 0

    # Iterate from the middle to the beginning.
    for i in range(mid - 1, left - 1, -1):
        curr += nums[i]
        best_left_sum = max(best_left_sum, curr)

    # Reset curr and iterate from the middle to the end.
    curr = 0
    for i in range(mid + 1, right + 1):
        curr += nums[i]
        best_right_sum = max(best_right_sum, curr)

    # The best_combined_sum uses the middle element and
    # the best possible sum from each half.
    best_combined_sum = nums[mid] + best_left_sum + best_right_sum
    return best_combined_sum

def maximum_subarray_dc(nums, l, h):
    if l == h:
        return nums[l]
    
    m = (l + h) // 2
    return max(maximum_subarray_dc(num, l, m), maximum_subarray_dc(num, m + 1, h), maximum_subarray_dc(nums, l, m ,h))

if __name__ == '__main__':
    array = []
    import random
    for i in range(0,5):
    n = random.randint(1,30)


