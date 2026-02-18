class Animal:
    def sound(self):
        print("Animal makes a sound")

class Cat(Animal):
    def climb(self):
        print("Cat is climbing the tree")

class Cow(Animal):
    def chew(self):
        print("Cow is chewing grass")

a = Animal()


mycat = Cat()
mycat.climb()
mycat.sound()


mycow = Cow()

