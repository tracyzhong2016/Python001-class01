# coding: utf-8
from abc import ABCMeta,abstractmethod

class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self,animal):
        if animal in self.animals:
            return self.animals[animal]
        else:
            self.animals.append(animal)
            self.__dict__[type(animal).__name__] = animal

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, type, size, character):
        self.type = type
        self.size = size
        self.character = character

    @property
    def is_beast(self):
        if self.type=='食肉类型' and self.character=='性格凶猛' and (self.size=='中' or self.size=='大'):
            return True
        else:
            return False
class Cat(Animal):
    bar=True
    def __init__(self,name,type, size, character):
        super(Cat,self).__init__(type,size,character)
        self.name = name
    @property
    def is_pet(self):
        return not self.is_beast
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
