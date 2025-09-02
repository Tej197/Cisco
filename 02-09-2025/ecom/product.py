

class Product:
    def __init__(self, id, name, description, category, tags, stock, price):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.tags = tags
        self.stock = stock
        self.price = price

    def __str__(self):
        return f"(id={self.id}, name={self.name}, description={self.description}, category={self.category}, tags={self.tags}, stock={self.stock}, price={self.price})"
    def __repr__(self):
        return self.__str__()

'''
mobile_iphone = Product(
    id=1,
    name="iPhone 13",
    description="Latest Apple iPhone with A15 Bionic chip",
    category="Electronics",
    tags=["smartphone", "apple", "ios"],
    stock=50,
    price=999.99
)

mobile_samsung = Product(
    id=2,
    name="Samsung Galaxy S21",
    description="Flagship Samsung phone with excellent camera",
    category="Electronics",
    tags=["smartphone", "samsung", "android"],
    stock=30,
    price=799.99
)

print(mobile_iphone)
print(mobile_samsung)

'''