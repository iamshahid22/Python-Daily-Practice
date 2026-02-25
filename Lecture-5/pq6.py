nums=(1,23,4,5,6,34,54,3,22)

x=int(input("enter number:"))

i=0
while i<len(nums):
    if(nums[i]==x):
        print("Founf at index",i)
        break
    else:
        print("finding...")
    i+=1
print("end loop")