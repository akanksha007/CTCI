class AnimalShelter:
    def __init__(self):
        self.count = 0
        self.dog = list()
        self.cat = list()

    def enqueue(self, type):
        self.count += 1
        if type == 'dog':
            self.dog.append(self.count)
        else:
            self.cat.append(self.count)


    def dequeueAny(self):
        if not self.dog and not self.cat:
            print("AnimalShelter is empty")
        else:
            if self.dog[0] > self.cat[0]:
                print(self.cat[0])
                del self.cat[0]
            else:
                print(self.dog[0])
                del self.dog[0]

    def dequeueCat(self):
        if self.cat:
            print(self.cat[0])
            del self.cat[0]

    def dequeueDog(self):
        if self.dog:
            print(self.dog[0])
            del self.dog[0]


    def print_queue(self):
        print(*self.dog)
        print(*self.cat)

a = AnimalShelter()
for i in range(5):
    a.enqueue('dog')
    a.enqueue('cat')
a.print_queue()
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.dequeueAny()
a.dequeueDog()
a.dequeueDog()
a.print_queue()

