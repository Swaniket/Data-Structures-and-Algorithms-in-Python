# An animal shelter, which holds only dogs & cats, operates on a strictly "FIFO" basis.
# People must adopt either the "Oldest" (based on arrival time) of all animals at the shelter,
# or they can select weather they would prefer a dog or a cat (and will recieve 
# the oldest animal of that type). They cannot select which specific animal they would like.

# Create a data structure to maintain this system and implement operations such as 
# enqueue(), dequeueAny(), deququeDog(), deququeCat()

class AnimalShelter:
    def __init__(self) -> None:
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        cat = self.cats.pop(0)
        return cat

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        dog = self.dogs.pop(0)
        return dog

    def dequeueAny(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result

if __name__ == "__main__":
    customQueue = AnimalShelter()

    customQueue.enqueue("Dog1", "Dog")
    customQueue.enqueue("Dog2", "Dog")

    customQueue.enqueue("Cat1", "Cat")
    customQueue.enqueue("Dog3", "Dog")

    customQueue.enqueue("Cat2", "Cat")

    print(customQueue.dequeueCat())
    print(customQueue.dequeueDog())

    print(customQueue.dequeueAny())