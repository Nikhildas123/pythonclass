# class Animals:
#     def speak(self):
#         return "bow sound"
# class dog(Animals):
#     def speak(self):
#         return "woaf!!" 
# class cat(Animals):
#     def speak(self):
#         return "meow"
# def animal_sound(animal: Animal):
#     return animal.speak()
# dog=dog()
# cat=cat()
# print (animal_sound(dog))
# print(animal_sound(cat))

#duck

class Dog:
    def speak(self):
        print("woaf!!")
class Cat:
    def speak(self):
        print("meow")
class human:
    def speak(self):
        print("hellow")
def make_it_speak(obj):
    obj.speak()
for creature in [Dog(),Cat(),human()]:
    make_it_speak(creature)
            
