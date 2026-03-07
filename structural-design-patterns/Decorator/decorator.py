from abc import ABC,abstractmethod
class Coffee(ABC):
    @abstractmethod
    def get_price(self):
        pass
class SimpleCoffee(Coffee):
    def get_price(self):
        return 25.0
class CoffeeDecorator(Coffee):
    def __init__(self,inner):
        self.inner=inner
class WhippedCreamCoffee(CoffeeDecorator):
    def __init__(self, inner):
        super().__init__(inner)
    def get_price(self):
        return self.inner.get_price()+25.0
class WhippedCreamColdCoffee(CoffeeDecorator):
    def __init__(self, inner):
        super().__init__(inner)
    def get_price(self):
        return self.inner.get_price()+25.0
    
if __name__ == "__main__":
    spl_coffee=WhippedCreamCoffee(SimpleCoffee())
    spl_coffee_price=spl_coffee.get_price()
    print(spl_coffee_price)