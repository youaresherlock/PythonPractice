#!/usr/bin/python
# -*- coding:utf-8 -*-
from typing import List


"""
[4, 2, 5]
[1, 4, 2, 5]
[3, 4, 2, 5]
当 nums[i] 破坏了数组的单调递增时，即 nums[i] < nums[i - 1]  时，为了让数组有序
我们发现一个规律（在上面三个例子中， nums[i] 都为 2， nums[i -1] 都为 4）：

如例①的情况，当 i = 1 ，那么修改 num[i- 1] ，不要动 nums[i] ，因为nums[i]后面的元素是啥我们还不知道呢，少动它为妙。
如例②的情况，当 i > 1 时，我们应该优先考虑把 nums[i - 1] 调小到 >= nums[i - 2] 并且 <= nums[i]。同样尽量不去修改 nums[i] ，理由同上。
如例③的情况，当 i > 1 且 nums[i] < nums[i - 2] 时，我们无法调整 nums[i - 1] ，我们只能调整 nums[i] 到 nums[i - 1] 。
"""


def check_possibility(nums: List[int]) -> bool:
    N = len(nums)
    count = 0
    for i in range(1, N):
        if nums[i] < nums[i - 1]:
            count += 1
            if i == 1 or nums[i] >= nums[i - 2]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]
    return count <= 1


if __name__ == '__main__':
    # nums = [4, 2, 5]
    # nums = [1, 4, 2, 5]
    nums = [3, 4, 2, 5]
    print(check_possibility(nums))