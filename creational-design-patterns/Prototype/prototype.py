from abc import abstractmethod,ABC
class Clonable(ABC):
    def clone(self):
        pass
class Circle(Clonable):
    def __init__(self,color,radius):
        self.color=color
        self.radius=radius
        self.pts=[1,2,4]
    def clone(self):
        return Circle(self.color,self.radius)
    def print_info(self):
        print(self.color)
        print(self.radius)
        print(self.pts)
class Rectangle(Clonable):
    def __init__(self,color,length,breadth):
        self.color=color
        self.length=length
        self.breadth=breadth
    def clone(self):
        return Rectangle(self.color,self.length,self.breadth)
    def print_info(self):
        print(self.color)
        print(self.length)
        print(self.breadth)
if __name__=="__main__":
    circle=Circle("red",10.0)
    clone_circle=circle.clone()
    clone_circle.radius=20.0
    circle.pts[0]=3
    circle.print_info()
    clone_circle.print_info()
    rectangle=Rectangle("blue",20.0,40.0)
    clone_rectangle=rectangle.clone()
