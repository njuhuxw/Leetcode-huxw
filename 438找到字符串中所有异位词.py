import itertools

def findAnagrams(s: str, p: str):
    slist = list(s)
    plist = list(p)
    print(slist)
    print(plist)

    length = len(plist)
    left, right = 0, length - 1
    ans = []

    while right < len(slist):
        if slist[left] in


    return ans



# 超时！
# def findAnagrams(s: str, p: str):
#     slist = list(s)
#     plist = list(p)
#
#     length = len(plist)
#     left, right = 0, length - 1
#     ans = []
#
#     p_all = list(itertools.permutations(plist, length))  # plist的全排列
#     print(p_all)
#
#     while right < len(slist):
#         # 判断s的字串是否在p的全排列中
#         sub_s = tuple(slist[left:right + 1])
#
#         if sub_s in p_all:
#             ans.append(left)
#
#         left += 1
#         right += 1
#     return ans

s = "abab"
p = "aa"

print(findAnagrams(s, p))
