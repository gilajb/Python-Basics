class Dog:
    def __init__(self, breed , color , age):
        self.breed = breed
        self.color = color
        self.age = age

    def speak(self):
        print("Dog barks")

dog1 = Dog("Bulldog", "Brown", 3)
print(dog1.breed, dog1.color ,dog1.age)

dog2 = Dog("German Shepherd", "Black", 4)
print(dog2.breed, dog2.color ,dog2.age)

dog3 = Dog("Chihuahua", "White", 2)
print(dog3.breed, dog3.color ,dog3.age)
