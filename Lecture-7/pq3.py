word=input("Enter word:")

def check_for_word():
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find(word)!=-1):
             print("Found")
        else:
             print("Not Found")

check_for_word()