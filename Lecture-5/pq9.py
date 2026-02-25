nums=(1,2,3,4,5,67,8,9,5)
x=int(input("enter number:"))
idx=0
for val in nums:
    if(val==x):
        print("found at index:",idx)
        break
    idx+=1


