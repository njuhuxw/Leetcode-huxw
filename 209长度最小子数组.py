# 滑动窗口

def minSubArrayLen( s, nums) :
    if not nums:
        return 0

    left = 0
    right = 0
    ans = len(nums) + 1
    sum = 0

    while right < len(nums):
        print(ans)
        sum += nums[right]


        # 这个while要注意⚠️
        while sum >= s:
            ans = min(ans, right - left + 1)
            sum -= nums[left]
            left += 1

        # 这个right+=1的位置要注意⚠️，不能提前
        right += 1

    if ans > len(nums):
        return 0
    else:
        return ans


k=7
num=[2,3,1,2,4,3]
print(minSubArrayLen(k,num))