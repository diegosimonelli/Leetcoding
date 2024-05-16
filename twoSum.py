# # brute force approach.

# Time Complexity: O(n^2) -> because I have two nested loops iterating over the list

# Space Complexity: O(1) -> because I'm not using any additional data structures that grow with the size of the input.
# the only space used is for a few variables, which are constant regardless of the size of the input.

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]
            

# better approach with hashmaps (dictionaries). Time complexity: O(n)
def twoSum(nums, target):
    prevMap = {} # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))