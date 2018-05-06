class AnimalShelter():
    def __init__(self):
        self.order = 0
        self.cat = list()
        self.dog = list()
        self.cat_order_list = list()
        self.dog_order_list = list()


    def enqueue(self, type, name):
        self.order += 1
        if type == 'dog':
            d = Dog(name)
            self.dog.append(d)
            self.dog_order_list.append(self.order)
        else:
            c = Cat(name)
            self.cat.append(c)
            self.cat_order_list.append(self.order)

    def dequeueAny(self):
        if not self.dog and not self.cat:
            print("AnimalShelter is empty")
        else:
            if self.dog_order_list[0] > self.cat_order_list[0]:
                print(self.cat[0].name)
                del self.cat[0]
                del self.cat_order_list[0]
            else:
                print(self.dog[0].name)
                del self.dog[0]
                del self.dog_order_list[0]

    def dequeueCat(self):
        print(self.cat[0].name)
        del self.cat[0]
        del self.cat_order_list[0]


    def dequeueDod(self):
        print(self.dog[0].name)
        del self.dog[0]
        del self.dog_order_list[0]



class Cat():
    def __init__(self, name):
        self.name = name

class Dog():
    def __init__(self, name):
        self.name = name


a = AnimalShelter()
a.enqueue('dog', 'd1')
a.enqueue('cat', 'c1')
a.enqueue('dog', 'd2')
a.enqueue('cat', 'c2')
a.enqueue('dog', 'd3')
a.enqueue('cat', 'c3')
a.enqueue('cat', 'c4')
a.enqueue('dog', 'd4')
a.enqueue('cat', 'c5')
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.dequeueCat()
a.dequeueDod()
