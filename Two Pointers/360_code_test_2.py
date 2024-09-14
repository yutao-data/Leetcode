def longest_valid_interval(n, heights):
    def calc_max_length(arr):
        max_length = 1
        current_length = 1
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] >= 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        return max(max_length, current_length)

    max_length = calc_max_length(heights)

    for i in range(n):
        original_height = heights[i]

        if i > 0:
            heights[i] = heights[i - 1] + 1
            max_length = max(max_length, calc_max_length(heights))

        if i < n - 1:
            heights[i] = heights[i + 1] - 1
            max_length = max(max_length, calc_max_length(heights))

        heights[i] = original_height

    return max_length


T = int(input())

for _ in range(T):
    n = int(input())
    heights = list(map(int, input().split()))

    result = longest_valid_interval(n, heights)
    print(result)