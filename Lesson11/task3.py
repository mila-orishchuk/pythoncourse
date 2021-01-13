'''
Product Store

Write a class Product that has three attributes:

    type
    name
    price

Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case they can’t
perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain
type of product, etc.

Also, the ProductStore class must have the following methods:

    add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
    set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name).
    The discount must be specified in percentage
    sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error.
    It also increments income if the sell_product method succeeds.
    get_income() - returns amount of many earned by ProductStore instance.
    get_all_products() - returns information about all available products in the store.
    get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


'''


class Product:

    def __init__(self, category, name, price, discount=0):
        self.category = category
        self.name = name
        self.price = price
        self.amount = 0
        self.discount = discount

    def add_amount(self, amount):
        if self.amount + amount < 0: # check is enough
            raise Exception(f'Not enough of {self.name}')
        self.amount += amount

    def set_discount(self, discount):
        self.discount = discount

    def get_hash(self):
        return self.category + self.name


class ProductStore:
    def __init__(self, premium=30):
        self.premium = premium
        self.products = {}
        self.income = 0

    def add(self, product: Product, amount: int):
        hash = product.get_hash()
        if hash not in self.products.keys():
            self.products[hash] = product

        self.products[hash].add_amount(amount)

    def find(self, key, value):
        return list(filter(lambda product: getattr(product, key) == value, self.products.values()))

    def set_discount(self, identifier, percent, identifier_type='name'):
        products = self.find(identifier_type, identifier)
        for product in products:
            self.products[product.get_hash()].set_discount(percent)

    def sell_product(self, product_name, amount):
        products = self.find('name', product_name)
        if len(products) == 1:
            product = products.pop()
            self.products[product.get_hash()].add_amount(-amount)
            self.income += product.price * \
                (1 + self.premium / 100) * (1 - product.discount / 100)
        elif len(products) > 1:
            raise Exception('ambiguous category')
        else:
            raise Exception('could not find')

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products.values()

    # def get_amount(self, product_name):
    #     products = self.find('name', product_name)
    #     if not products:
    #         raise Exception('could not find')
    #     return products[0].amount

    def get_product_info(self, product_name):
        products = self.find('name', product_name)
        if not products:
            raise Exception('could not find')
        return (products[0].name, products[0].amount)


if __name__ == '__main__':
    try:
        p = Product('Sport', 'Football T-Shirt', 100)
        p2 = Product('Food', 'Ramen', 1.5)
        s = ProductStore()
        s.add(p, 10)
        s.add(p2, 300)
        s.sell_product('Ramen', 10)
        assert s.get_product_info('Ramen') == ('Ramen', 290)
    except Exception as e:
        print(e)
