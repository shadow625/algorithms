import sys
import random
def quick(nums,low,high):
	if low<high:
		pos=partition(nums,low,high)
		quick(nums,low,pos-1)
		quick(nums,pos+1,high)
		print repr(nums)
	
def partition(nums,low,high):
	print repr(nums[low:high+1])+"\t"+str(low)+"\t"+str(high)
	target=nums[high]
	pos=low-1
	for i in range(low,high):
		if nums[i]<=target:
			pos+=1
			exchange(nums,pos,i)
	exchange (nums,pos+1,high)
	return pos+1

def exchange(nums,n,l):
	mid=nums[n]
	nums[n]=nums[l]
	nums[l]=mid

def rando(x):
	answer=[]
	for i in xrange(1,21):
		answer.append(random.randint(0,x))
	return answer

quick(rando(100),0,19)
