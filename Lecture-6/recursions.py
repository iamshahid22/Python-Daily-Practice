#recursions is know n as fuction calls itself repeatedly

n=int(input("Enter a number:"))
#recursive function
def show(n):
    if(n==0):  #base case
        return
    print(n)
    show(n-1)
    print("END")

show(n)