
def lists(dictionary_1, dictionary_2):
    dictionary = (set(dictionary_1.keys()) & set(dictionary_2.keys()))
    return dictionary


products_1 = {'strawberries': 10, 'apple': 10}
products_2 = {'banana': 10, 'strawberries': 10, 'cherry': 10, 'apple': 10}

products = lists(products_1, products_2)
print(products)
