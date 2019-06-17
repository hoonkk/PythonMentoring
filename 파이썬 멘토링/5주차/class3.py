class Dog():
    def growl(self):
        print('멍멍')

class Cat():
    def growl(self):
        print('야옹')

cat = Cat()
dog = Dog()

cat.growl()
dog.growl()

cat = Dog()
cat.growl()