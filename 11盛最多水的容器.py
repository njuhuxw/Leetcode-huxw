# 双指针
# key：找到判决条件
def maxArea(height) -> int:
    left = 0
    right = len(height) - 1
    ans = 0

    while left < right:
        temp = (right - left) * min(height[left], height[right])
        ans = max(ans, temp)

        # 每一次移动短板
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return ans


h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(h))
