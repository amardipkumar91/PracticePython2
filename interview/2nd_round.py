#---- Observer Design Pattern ---------
# class Subscriber(object):
#     def __init__(self, name):
#         self.name = name
    
#     def update(self, message):
#         print ("hi hello")

# class Publisher(object):
#     def __init__(self):
#         self.subscribers = set()
    
#     def register(self, name):
#         self.subscribers.add(name)
    
#     def dispatch(self, message):
#         for sub in self.subscribers:
#             sub.update(message)

# pub = Publisher()
# obj1 = Subscriber("A")
# obj2 = Subscriber("A")
# obj3 = Subscriber("A")
# pub.register(obj1)
# pub.register(obj2)
# pub.register(obj3)
# pub.dispatch("hi")

#------ Singleton Design pattern------

# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]

# class Test(metaclass=Singleton):
#     def __init__(self, a):
#         self.a = a
#     def foo(self):
#         print (self.a)

# obj = Test("hi")
# print (id(obj))
# obj1 = Test("hello")
# print (id(obj1))


#------ Decorator Design Pattern----
class Component():
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component):
    _component: Component = None
    def __init__(self, component : Component) -> None:
        self._component = component
    
    @property
    def component(self) -> str:
        return self._component
    
    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"

class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"

def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")

if __name__ == '__main__':
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print ("\n")

    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    client_code(decorator2)



    



