class Solution(object):
	def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in xrange(length-2): #[8]
			if nums[i]>0: break #[7]
			if i>0 and nums[i]==nums[i-1]: continue #[1]

			l, r = i+1, length-1 #[2]
			while l<r:
				total = nums[i]+nums[l]+nums[r]

				if total<0: #[3]
					l+=1
				elif total>0: #[4]
					r-=1
				else: #[5]
					res.append([nums[i], nums[l], nums[r]])
					while l<r and nums[l]==nums[l+1]: #[6]
						l+=1
					while l<r and nums[r]==nums[r-1]: #[6]
						r-=1
					l+=1
					r-=1
		return res



#this is the answer from caikehe and all the comments below

#the main idea is to iterate every number in nums.
#we use the number as a target to find two other numbers which make total zero.
#for those two other numbers, we move pointers, l and r, to try them.

#l start from left to right
#r start from right to left

#first, we sort the array, so we can easily move i around and know how to adjust l and r.
#if the number is the same as the number before, we have used it as target already, continue. [1]
#we always start the left pointer from i+1 because the combination has already tried. [2]

#now we calculate the total
#if the total is less than zero, we need it to be larger, so we move the left pointer. [3]
#if the total is greater than zero, we need it to be smaller, so we move the right pointer. [4]
#if the total is zero, bingo! [5]
#we need to move the left and right pointers to the next different numbers, so we do not get repeating result. [6]

#we do not need to consider i after nums[i]>0, since sum of positive will be always greater than zero. [7]
#we do not need to try the last two, since there are no rooms for l and r pointers.
#You can think of it as The last two have been tried by all others. [8]

