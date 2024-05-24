class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

# Testing
def main():
    flying_fish = FlyingFish()
    
    # Call methods and observe outputs
    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()
    
    # Method Resolution Order (MRO)
    print(FlyingFish.mro())

if __name__ == "__main__":
    main()
