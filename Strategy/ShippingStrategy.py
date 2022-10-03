from abc import ABC, abstractclassmethod


class Order():
    def __init__(self, value: int) -> None:
        self._value = value

    @property
    def value(self) -> int:
        return self._value


class ShippingStrategy(ABC):
    @abstractclassmethod
    def calculate(self, order: Order) -> float:
        pass


class FedexStrategy(ShippingStrategy):
    def calculate(self, order: Order) -> float:
        return 3.00 * order.value


class PostalStrategy(ShippingStrategy):
    def calculate(self, order: Order) -> float:
        return 5.00 * order.value


class CalculateShipping():
    def shipping_cost(self, order: Order, strategy: ShippingStrategy) -> float:
        return strategy.calculate(order)


my_order = Order(100)
calc_shipping = CalculateShipping()

fedex_strategy = FedexStrategy()
print('Fedex Strategy:', calc_shipping.shipping_cost(my_order, fedex_strategy))

postal_strategy = PostalStrategy()
print('Postal Strategy:', calc_shipping.shipping_cost(my_order, postal_strategy))
