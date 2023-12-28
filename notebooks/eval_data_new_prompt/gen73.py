def smallest_change(arr):
    ans = 0
    for i in range(len(arr) // 2):
        if arr[len(arr) - i - 1]!= arr[i]:
            ans += 1
    return ans