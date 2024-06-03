
# 1

class Device:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class CoffeeMachine(Device):
    def __init__(self, name, color, series, time):
        Device.__init__(self, name, color)
        self.series = series
        self.time = time


class Blender(Device):
    def __init__(self, name, color, speed):
        Device.__init__(self, name, color)
        self.speed = speed


class MeatGrinder(Device):
    def __init__(self, name, color, material):
        Device.__init__(self, name, color)
        self.material = material


coffee_machine = CoffeeMachine('Coffee Machine', 'Red', 'XR', 15)
blender = Blender('Blender', 'Black', '12')
meat_grinder = MeatGrinder('MeatGrinder', 'Yellow', 'titanium')

print(f'Coffee Machine: {coffee_machine.name}, Color: {coffee_machine.color}, Series: {coffee_machine.series}, Time: {coffee_machine.time}')
print(f'Blender: {blender.name}, Color: {blender.color}, Speed: {blender.speed}')
print(f'Meat Grinder: {meat_grinder.name}, Color: {meat_grinder.color}, Material: {meat_grinder.material}')

# 2


class Ship:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


class Frigate(Ship):
    def __init__(self, name, speed, class_1):
        Ship.__init__(self, name, speed)
        self.class_1 = class_1


class Destroyer(Ship):
    def __init__(self, name, speed, class_2):
        Ship.__init__(self, name, speed)
        self.class_2 = class_2


class Cruiser(Ship):
    def __init__(self, name, speed, class_3):
        Ship.__init__(self, name, speed)
        self.class_3 = class_3


frigate = Frigate('Frigate', '20', 'Warship')
destroyer = Destroyer('Destroyer', '20', 'Warship')
cruiser = Cruiser('Cruiser', '32', 'Warship')

print(f'Frigate: {frigate.name}, Speed: {frigate.speed}, Class: {frigate.class_1}')
print(f'Destroyer: {destroyer.name}, Speed: {destroyer.speed}, Class: {destroyer.class_2}')
print(f'Cruiser: {cruiser.name}, Speed: {cruiser.speed}, Class: {cruiser.class_3}')


# 3


class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, flat):
        return self.area == flat.area

    def __ne__(self, flat):
        return self.area != flat.area

    def __gt__(self, flat):
        return self.price > flat.price

    def __lt__(self, flat):
        return self.price < flat.price

    def __ge__(self, flat):
        return self.price >= flat.price

    def __le__(self, flat):
        return self.price <= flat.price


flat_1 = Flat(50, 100000)
flat_2 = Flat(52, 101000)

print(f'The first apartment is equal to the second: {flat_1 == flat_2}')
print(f'The first apartment is not equal to the second: {flat_1 != flat_2}')
print(f'The first apartment is larger than the second: {flat_1 > flat_2}')
print(f'The first apartment is smaller than the second: {flat_1 < flat_2}')
print(f'The first apartment is greater than or equal to the second: {flat_1 >= flat_2}')
print(f'The first apartment is less than or equal to the second: {flat_1 <= flat_2}')


