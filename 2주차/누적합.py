nums = [3, 5, 1, 4, 2]

acc_nums = [0]
for num in nums:
    acc_nums.append(acc_nums[-1]+num)

print(acc_nums)
# [0, 3, 8, 9, 13, 15]

from itertools import accumulate

nums = [3, 5, 1, 4, 2]
acc_nums = [0] + list(accumulate(nums))

print(acc_nums)