# forgot the neg in arr
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # find the start
        i = len(numbers)-1
        while numbers[i] >= target:
            i -= 1

        # assume we have an exact one answer
        r = i
        l = i - 1

        while True:
            if numbers[r]+numbers[l] == target:
                return [l+1, r+1]
            # mv left only
            elif numbers[r]+numbers[l] > target and l > 0:
                l -= 1
            # reset right and left
            elif numbers[r]+numbers[l] > target and l == 0:
                r -= 1
                l = r-1



        l, r = 0, 1
        while True:
            if numbers[l]+numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l]+numbers[r] < target:
                r += 1
# Runtime Error
# IndexError: list index out of range
#     while numbers[i] >= target:
# Line 5 in twoSum (Solution.py)
#     ret = Solution().twoSum(param_1, param_2)
# Line 54 in _driver (Solution.py)
#     _driver()
# Line 65 in <module> (Solution.py)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) -1
        l = r -1

        while True:
            if numbers[r]+numbers[l] == target:
                return [l+1, r+1]
            elif numbers[r]+numbers[l] > target:
                if l > 0: # mv left only
                    l -= 1
                elif l == 0: # reset right and left
                    r -= 1
                    l = r-1
            else: # reset right and left
                r -= 1
                l = r-1
# Time Limit Exceeded


# given the constraint of exactly one solution
# you can simply ignore the dup nums

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) -1
        l = r -1

        while True:
            # ignore the dup nums
            if r > 0 and numbers[r] == numbers[r-1] != 0:
                r -= 2
                l = r-1
                continue
            elif l > 0 and numbers[l] == numbers[l-1] != 0:
                l -= 2
                continue

            if numbers[r]+numbers[l] == target:
                return [l+1, r+1]
            elif numbers[r]+numbers[l] > target:
                if l > 0: # mv left only
                    l -= 1
                elif l == 0: # reset right and left
                    r -= 1
                    l = r-1
            else: # reset right and left
                r -= 1
                l = r-1
# failed at 
# numbers =
# [1,2,3,4,4,9,56,90]
# target =
# 8


# given the constraint of exactly one solution
# you can simply ignore the dup nums except the num==target/2

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) -1
        l = r -1

        while True:
            # ignore the dup nums
            if r > 0 and numbers[r] == numbers[r-1]:
                if numbers[r] == target/2:
                    return [r, r+1]
                r -= 2
                l = r-1
                continue
            elif l > 0 and numbers[l] == numbers[l-1]:
                if numbers[l] == target/2:
                    return [l, l+1]
                l -= 2
                continue

            if numbers[r]+numbers[l] == target:
                return [l+1, r+1]
            elif numbers[r]+numbers[l] > target:
                if l > 0: # mv left only
                    l -= 1
                elif l == 0: # reset right and left
                    r -= 1
                    l = r-1
            else: # reset right and left
                r -= 1
                l = r-1
# Time Limit Exceeded
