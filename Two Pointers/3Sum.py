print((1,2) == (2,1))
print(sorted([3,1,2,3]))
print(set([1,2,3]) == set([3,2,1]))
a = set()
print(a)
# a.add( set([1,2,3]) )
print(a)

print({'a':2, 'b':2}=={'a':2, 'b':2})
a = [1,2,3]
b = [2,3,1]
print(a==b)
print(a==sorted(b))
# print(set([[1,2,3], [1,2,3]]))


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num1 = set()

        output = []
        for i in range(len(nums)-2):
            if nums[i] in num1:
                continue
            num1.add(nums[i])
            
            num2 = set()
            for j in range(i+1, len(nums)-1):
                if nums[j] in num2:
                    continue
                num2.add(nums[j])

                num3 = set()
                for k in range(j+1, len(nums)):        
                    if nums[k] in num3:
                        continue
                    num3.add(nums[k])
                    
                    if nums[i] + nums[j] + nums[k] == 0:
                        output.append(
                            sorted([ nums[i], nums[j], nums[k] ])
                        )
        
        # remove dup
        output = sorted(output)
        new_output = output[:1]
        for ans in output:
            if ans == new_output[-1]:
                continue
            new_output.append(ans)

        return new_output
# TLE

# a = {
#     'd1': {1:2, 2:4},
#     'd2': {}
# }
# print(''.join([1,3,4]))

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        visited = set()

        num1 = set()
        for i in range(len(nums)-2):
            if nums[i] in num1:
                continue
            num1.add(nums[i])
            
            num2 = set()
            for j in range(i+1, len(nums)-1):
                if nums[j] in num2:
                    continue
                num2.add(nums[j])

                num3 = set()
                for k in range(j+1, len(nums)):        
                    if nums[k] in num3:
                        continue
                    num3.add(nums[k])
                    
                    if nums[i] + nums[j] + nums[k] == 0:
                        needed = sorted([ str(nums[i]), str(nums[j]), str(nums[k]) ])
                        if (needed:=''.join(needed)) in visited:
                            continue
                        visited.add(needed)
                        output.append(
                            [ nums[i], nums[j], nums[k] ]
                        )

        return output
# still TLE
# this is a n*n*n solution, we need to at least cut it to n*n
print(sorted([-1,0,1,2,-1,-4,5,-5]))            


# 2 pointer
# easy to think of a n*n*n solution, we need to at least cut it to n*n

# [-4,-1,-1,0,1,2,5]
# [0,0,0,0]
# [-5, -4, -1, -1, 0, 1, 2, 5]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        nums = sorted(nums)
        num1 = set()
        for i in range(len(nums)-2):
            if nums[i] in num1:
                continue
            num1.add(nums[i])

            l = i+1
            r = len(nums)-1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    output.append([ nums[i], nums[l], nums[r] ])
                    while l < r and nums[l] == output[-1][1]:
                        l += 1
                    while l < r and nums[r] == output[-1][2]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return output
print(Solution().threeSum([-5, -4, -1, -1, 0, 0, 1, 2, 5, 5]))
