# SwimMixin class
class SwimMixin:
    def swim(self):
        print("The creature swims!")

# FlyMixin class
class FlyMixin:
    def fly(self):
        print("The creature flies!")

# Dragon class inheriting from SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

# Testing the Dragon's abilities
def main():
    # Instantiate a Dragon object
    draco = Dragon()

    # Demonstrate abilities
    draco.swim()
    draco.fly()
    draco.roar()

if __name__ == "__main__":
    main()
