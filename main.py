class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setname(self,name1):
        self.__name = name1

    def setage(self,age1):
        self.__age = age1

    def say(self):
        print(f"Я {self.__name}, мені {self.__age} років")


misha = Person("Misha", 28)
misha.setname("Misha Sahan")
misha.setage(29)
misha.say()
