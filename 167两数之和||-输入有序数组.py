# 双指针

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1
    sum = numbers[left] + numbers[right]

    while sum != target:
        if sum < target:
            left += 1
        else:
            right -= 1

        sum = numbers[left] + numbers[right]

    return [left + 1, right + 1]


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))

# 双撞指针：125、344、345、11