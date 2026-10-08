from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, animal_id: int, name: str, age: int) -> None:
        self.animal_id = animal_id
        self.name = name
        self.age = age

    @property
    @abstractmethod
    def animal_type(self) -> str:
        pass

    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    @property
    def animal_type(self) -> str:
        return "Собака"

    def make_sound(self) -> str:
        return "Гав-гав!"


class Cat(Animal):
    @property
    def animal_type(self) -> str:
        return "Кошка"

    def make_sound(self) -> str:
        return "Мяу!"


def main() -> None:
    dog = Dog(1, "Бобик", 4)
    cat = Cat(2, "Мурка", 3)

    print(dog.name, dog.make_sound())
    print(cat.name, cat.make_sound())


if __name__ == "__main__":
    main()
