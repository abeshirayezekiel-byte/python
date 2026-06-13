class Parrot:
    species="bird" 
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("woo", 15)
# access the class attributes

print("Blu is a {}".format(blu.species))

print("Woo is also a {}".format(woo.species))

# access the instance attributes

print("{} is {} years old".format( blu.name, blu.age))

print("{} is {} years old".format( woo.name, woo.age))