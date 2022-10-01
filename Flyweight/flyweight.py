class ComplexPizza(object):
    def __init__(self):
        pass

    def pizzas(self, pizza_name):
        return pizza_name


class PizzaFlavours(object):
    pizza_flavours = {}

    def __new__(cls, name, pizza_flavor_id):
        try:
            id = cls.pizza_flavours[pizza_flavor_id]
        except KeyError:
            id = object.__new__(cls)
            cls.pizza_flavours[pizza_flavor_id] = id
        return id

    def set_pizza_info(self, pizza_info):
        pg = ComplexPizza()
        self.pizza_info = pg.pizzas(pizza_info)

    def get_pizza_info(self):
        return self.pizza_info


if __name__ == '__main__':
    pizza_data = (('a', 1, 'Peperoni'), ('a', 2, 'Cheese'), ('b', 1, 'Pineapple'))
    pizza_flavour_objects = []
    for i in pizza_data:
        obj = PizzaFlavours(i[0], i[1])
        obj.set_pizza_info(i[2])
        pizza_flavour_objects.append(obj)

    for i in pizza_flavour_objects:
        print("id = " + str(id(i)))
        print(i.get_pizza_info())
