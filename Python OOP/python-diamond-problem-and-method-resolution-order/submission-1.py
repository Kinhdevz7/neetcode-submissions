class A:
    def print_method(self) -> None:
        print("A")

class B(A):
    def print_method(self) -> None:
        print("B")

class C(A):
    def print_method(self) -> None:
        print("C")

class D(B, C): 
    pass

# print Method Resolution Order (MRO) to determine which method to call when dealing with multiple inheritance.
print(D.__mro__)
# Do not change the code below
d = D()
d.print_method()
