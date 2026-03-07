from abc import ABC,abstractmethod

class Menu(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def getItemCount(self):
        pass

class MenuItem(Menu):
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(f"--{self.name},{self.price}")
    def getItemCount(self):
        return 1
class SubMenu(Menu):
    def __init__(self,name):
        self.name=name
        self.menu_items:Menu=[]
    def add_item(self,item:Menu):
        self.menu_items.append(item)
    def display(self):
        print(self.name)
        for item in self.menu_items:
            item.display()
    def getItemCount(self) -> int:
        return sum(child.getItemCount() for child in self.menu_items)
if __name__ == "__main__":
    burger = MenuItem("Burger", 8.99)
    fries = MenuItem("Fries", 3.99)
    cola = MenuItem("Cola", 1.99)
    water = MenuItem("Water", 0.99)

    drinks = SubMenu("Drinks")
    drinks.add_item(cola)
    drinks.add_item(water)

    main_menu = SubMenu("Main Menu")
    main_menu.add_item(burger)
    main_menu.add_item(fries)
    main_menu.add_item(drinks)

    main_menu.display()
    print(f"\nTotal items: {main_menu.getItemCount()}")