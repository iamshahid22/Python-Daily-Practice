tuple=(1,4,9,16,25,36,49,64,81,100)

i=0
while i<len(tuple):
    print(tuple[i])
    i+=1

#user searching a number
nums=(1,4,9,16,25,36,49,64,81,100)

x=int(input("enter a number:"))

i=0
while i<len(nums):
    if(nums[i]==x):
        print("Found at index", i)
    i+=1
