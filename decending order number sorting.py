import time
import time
from itertools import count
for i in count ():
    def sort(nums):
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums[j]<nums[j+1]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp


    nums=[]
    length=int(input("enter the length of list\n"))
    for i in range(length):
        nums.append(int(input("Enter element\n")))
    print("Unsorted list is ", nums)
    sort(nums)
    print("processing \n please wait...")
    time.sleep(6)
    print("decending order sorted list is ", nums)
    time.sleep(6.0)