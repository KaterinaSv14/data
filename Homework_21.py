import pickle

file_name = 'country.dat'

country_1 = {
    'Ukraine': 'Kiev',
    'USA': 'Washington',
    'French': 'Paris',
    'Spain': 'Madrid',
    'Liechtenstein': 'Vaduz'
}


def data_1(country_):
    with open(file_name, 'wb') as file:
        pickle.dump(country_, file)


def data_2():
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f'File {file_name} not found.')
        return {}
    except pickle.PickleError:
        print(f'Error loading data from {file_name}.')
        return {}


def add(country):
    add_country = input('Enter the name of the new country: ')
    add_capital = input('Enter the capital of this country: ')
    country.update({add_country: add_capital})
    data_1(country)


def remove(country):
    remove_country = input('Enter the name of the country to delete: ')
    if remove_country in country:
        removed_capital = country.pop(remove_country, None)
        print('The country has been removed from the dictionary')
        data_1(country)
    else:
        print('Country not found')


def search(country):
    search_country = input('Enter the name of the country to search: ')
    search_capital = country.get(search_country)
    if search_capital is not None:
        print(f'The capital of {search_country} is {search_capital}')
    else:
        print('Country not found')


def edit(country):
    edit_country = input('Enter the name of the country to edit: ')
    capital = country.get(edit_country)
    if capital is not None:
        new_capital = input('Enter a new capital city: ')
        country.update({edit_country: new_capital})
        data_1(country)
        print('The name of the capital has been changed')
    else:
        print('Country not found')


def main():
    country_2 = data_2()

    while True:
        print('Menu:\n1.Add a country\n2.Remove a country\n3.Search for a country\n4.Edit the capital\n5.Exit')

        number = input('Enter your number: ')

        if number == '1':
            add(country_2)
        elif number == '2':
            remove(country_2)
        elif number == '3':
            search(country_2)
        elif number == '4':
            edit(country_2)
        elif number == '5':
            break

    data_1(country_2)


main()
