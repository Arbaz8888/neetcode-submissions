class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        nums.sort() #[-4,-1,-1,0,1,2]
        arr = []

        for i in range(len(nums)): #for each i [-4,-1,-1,0,1,2]
            l, r = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]: # checking curr != prev
                # i > 0 is saving us for first iteration where nums[i - 1] doesn't exist
                # prev l != curr l (else we'll get duplicate triplets)  
                continue # skip this iteration

            while l < r: # for each element one traversal
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    arr.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]: # prev l != curr l (else we'll get duplicate triplets)
                        l += 1
                    while l < r and nums[r] == nums[r+1]: # prev r != curr r (else we'll get duplicate triplets)
                        r -= 1

                elif total < 0:
                    l += 1
                
                else:
                    r -= 1
        return arr
                
#Complexity: O(n): for loop (i is iterating) * O(n) for each element one traversal
# Optimal Solution:
# TC: O(n^2)
# Total SC: Auxillary SC + output stored = 0 + O(k), where k is no. of triplet
# Auxillary SC means space used in algorithm logic: O(1)

# # Note: O(k) depends on size of array, if size of array is n then k = n^2 (in worst case), 
# bcoz triplet grows at the speed of n^2 




        