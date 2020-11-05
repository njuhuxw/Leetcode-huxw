def partition(nums, left, right):
    while True:
        while nums[left] < nums[right]:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            if left >= right:
                break
            left += 1

        while nums[left] < nums[right]:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            if left >= right:
                break
            right -= 1

    return left

# 快速排序
def quick_sort(nums, left, right):
    # k = len(nums) - k
    if left < right:
        pi=partition(nums,left,right)
        quick_sort(nums,left,pi-1)
        quick_sort(nums,pi+1,right)

    return nums

# 求第K大元素
#     def quick_sort(self, nums, k):
#         left = 0
#         right = len(nums) - 1
#         k = len(nums) - k
#
#         while left < right:
#             j = self.partition(nums, left, right)
#
#             if j == k:
#                 break
#             elif j < k:
#                 left = j + 1
#             else:
#                 right = j - 1
#         return nums[k]

nums = [3, 4, 2, 7, 8, 4, 1]
left = 0
right = len(nums) - 1
quick_sort(nums,left,right)
print(nums)

# k=3
# print(quick_sort(nums,k))




# class Solution:
#     def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
#         return self.quick_sort(nums, k)
#
#     def quick_sort(self, nums, k):
#         left = 0
#         right = len(nums) - 1
#         k = len(nums) - k
#
#         while left < right:
#             j = self.partition(nums, left, right)
#
#             if j == k:
#                 break
#             elif j < k:
#                 left = j + 1
#             else:
#                 right = j - 1
#         return nums[k]
#
#     def partition(self, nums, left, right):
#         i = left - 1
#         pivot = nums[right]
#
#         for j in range(left, right):
#             if nums[j] <= pivot:
#                 i += 1
#                 nums[i], nums[j] = nums[j], nums[i]
#
#         nums[i + 1], nums[right] = nums[right], nums[i + 1]
#
#         return i + 1
