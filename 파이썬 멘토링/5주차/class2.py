class MyClass:
    def __init__(self):
        result = 0
    def add(self,a,b):
        self.result = a + b

a = MyClass()
b = MyClass()

a.add(3,4)
b.add(4,5)

print(a.result, b.result)
