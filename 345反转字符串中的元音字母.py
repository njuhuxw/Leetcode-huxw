# 反思：
# ss = list(s)
# s = ''.join(ss)
# left<right is ok， but left<=right is false.

# 元音字符：a e i o u
def reverseVowels(s: str) -> str:
    ss = list(s)
    left = 0
    right = len(s) - 1
    special = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    while left < right:
        if ss[left] not in special:
            left += 1
        if ss[right] not in special:
            right -= 1

        if ss[left] in special and ss[right] in special:
            ss[left], ss[right] = ss[right], ss[left]
            left += 1
            right -= 1

    s = ''.join(ss)

    return s


s = "race a car"
print(reverseVowels(s))
