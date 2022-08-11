from enum import Enum

class CartStatus(Enum):
    deactivate = 0
    activate = 1

class OrderStatus(Enum):
    deactivate = 0
    notPaid = 1
    paid = 2
    shipping = 3

class ProductStatus(Enum):
    deactivate = 0
    activate = 1

class UserStatus(Enum):
    deactivate = 0
    activate = 1

class ProductCategory(Enum):
    keyboard = 0
    earphone = 1
    mouse = 2
    desktop = 3


if __name__ == '__main__':
    print(UserStatus.deactivate.value)