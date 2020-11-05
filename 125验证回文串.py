def isPalindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s.lower()))
    print(s)
    return True if s == s[::-1] else False

# # 正则方法一：
# import re  # 正则表达式
#
#
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         import re
#         ss = re.sub('[:,` ;.@!?#$%^&*\(\)_+=\-\[\]\{\}\\\|\'\"\<\>]', '', s.lower())  # 把这些替换为空格
#         return ss[::-1] == ss
#
#
# # 正则方法二：
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         import re
#         s = re.sub('[^a-z0-9]', '', s.lower())
#         return s[::-1] == s
