from abc import ABC, abstractmethod


class AbstractProductA(ABC):

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class AbstractProductB(ABC):

    @abstractmethod
    def useful_function_b(self) -> str:
        pass


class AbstractFactory(ABC):
    
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass


    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcretProductA(AbstractProductA):

    def useful_function_a(self) -> str:
        return "The result of the product a"


class ConcretProductB(AbstractProductB):

    def useful_function_b(self) -> str:
        return "The result of the product b"


class ConcreteFactory(AbstractFactory):

    def create_product_a(self) -> AbstractProductA:
        return ConcretProductA()

    def create_product_b(self) -> AbstractProductB:
        return ConcretProductB()


def client_code(factory: AbstractFactory) -> None:
   product_a = factory.create_product_a()
   product_b = factory.create_product_b()

   print(product_a.useful_function_a())
   print(product_b.useful_function_b())


if __name__ == "__main__":
    client_code(ConcreteFactory())