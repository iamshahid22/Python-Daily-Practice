class A:
    def show(self):
        print("A class")

class B:
    def display(self):
        print("B class")

class C(A, B):
    pass

c = C()
c.show()
c.display()