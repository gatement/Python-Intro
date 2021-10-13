class Pet():

    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"I'm a pet, my name is {self.name}.")

def main():
    pet = Pet("Wangwang")
    pet.describe()

main()
