def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s = ["h", "e", "l", "l", "o"]
print(reverseString(s))

# 反思：有趣之处在于，它不需要返回，而且其需要在原地进行反转
