
# 1

class Car:

    def __init__(self, model_name, year_of_manufacture, manufacturer, engine_volume, car_color, price):
        self.model_name = model_name
        self.year_of_manufacture = year_of_manufacture
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.car_color = car_color
        self.price = price

    def car(self):
        print('Model name: ' + self.model_name)
        print('Year of manufacture: ' + self.year_of_manufacture)
        print('Manufacturer: ' + self.manufacturer)
        print('Engine volume: ' + self.engine_volume)
        print('Car color: ' + self.car_color)
        print('Price: ' + self.price)

    def update_new_price(self, new_price):
        self.price = new_price

    def update_car_color(self, new_car_color):
        self.car_color = new_car_color


car_new = Car(
    model_name='hyundai',
    year_of_manufacture='2023',
    manufacturer='South Korean',
    engine_volume='1.6',
    car_color='blue',
    price='20000'
    )

car_new.car()
car_new.update_new_price('18000')
car_new.update_car_color('red')
car_new.car()

# 2


class Book:

    def __init__(self, book_title, year_of_publication, publisher, genre, author, price):
        self.book_title = book_title
        self.year_of_publication = year_of_publication
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def book(self):
        print('Book title: ' + self.book_title)
        print('Year of publication: ' + self.year_of_publication)
        print('Publisher: ' + self.publisher)
        print('Genre: ' + self.genre)
        print('Author: ' + self.author)
        print('Price: ' + self.price)

    def update_new_price(self, new_price):
        self.price = new_price

    def update_publisher(self, new_publisher):
        self.publisher = new_publisher


book_new = Book(
    book_title='Martin Eden',
    year_of_publication='1909',
    publisher='The Pacific Monthly',
    genre='Drama',
    author='Jack London',
    price='300'
)

book_new.book()
book_new.update_new_price('275')
book_new.update_publisher('КСД')
book_new.book()

# 3


class Stadium:

    def __init__(self, stadium_name, opening_date, country, city, capacity):
        self.stadium_name = stadium_name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def stadium(self):
        print('Stadium name: ' + self.stadium_name)
        print('Opening date: ' + self.opening_date)
        print('Country: ' + self.country)
        print('City: ' + self.city)
        print('Capacity: ' + self.capacity)

    def update_new_capacity(self, new_capacity):
        self.capacity = new_capacity


capacity_new = Stadium(
    stadium_name='Metalist',
    opening_date='September 12, 1926',
    country='Ukraine',
    city='Kharkov',
    capacity='40003'
)

capacity_new.stadium()
capacity_new.update_new_capacity('40000')
capacity_new.stadium()
