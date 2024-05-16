# hashset cannot add multiple of the same numbers. Since we're checking if the array contains a duplicate we can
# just add each of the numbers in a set and then check if the number is or not in it.

# Time Complexity O(n) -> we just need to scan through the list of inputs once.
# Space Complexity O(n) -> the size of the hash set could be up to the size of the nums variable so it's O(n)

def containsDuplicate(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))
