from abc import ABC, abstractmethod
from dataclasses import dataclass


class PetSystemError(Exception):
    pass


class EntityNotFoundError(PetSystemError):
    pass


class DuplicateEntityError(PetSystemError):
    pass


class Animal(ABC):
    def __init__(
        self,
        animal_id: int,
        name: str,
        age: int,
        owner_id: int
    ) -> None:
        self.animal_id = animal_id
        self.name = name
        self.age = age
        self.owner_id = owner_id

    @property
    @abstractmethod
    def animal_type(self) -> str:
        pass

    @abstractmethod
    def make_sound(self) -> str:
        pass

    def to_dict(self) -> dict:
        return {
            "animal_id": self.animal_id,
            "name": self.name,
            "age": self.age,
            "owner_id": self.owner_id,
            "animal_type": self.animal_type,
        }


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


class Bird(Animal):
    @property
    def animal_type(self) -> str:
        return "Птица"

    def make_sound(self) -> str:
        return "Чик-чирик!"


@dataclass
class Owner:
    owner_id: int
    name: str
    phone: str


class Repository:
    def __init__(self) -> None:
        self._items: dict[int, object] = {}

    def create(self, item: object, item_id: int) -> None:
        if item_id in self._items:
            raise DuplicateEntityError(
                f"Объект с ID {item_id} уже существует."
            )
        self._items[item_id] = item

    def get(self, item_id: int) -> object:
        if item_id not in self._items:
            raise EntityNotFoundError(
                f"Объект с ID {item_id} не найден."
            )
        return self._items[item_id]

    def get_all(self) -> list[object]:
        return list(self._items.values())

    def update(self, item_id: int, item: object) -> None:
        if item_id not in self._items:
            raise EntityNotFoundError(
                f"Объект с ID {item_id} не найден."
            )
        self._items[item_id] = item

    def delete(self, item_id: int) -> None:
        if item_id not in self._items:
            raise EntityNotFoundError(
                f"Объект с ID {item_id} не найден."
            )
        del self._items[item_id]


class PetManagementSystem:
    def __init__(self) -> None:
        self.owners = Repository()
        self.animals = Repository()

    def add_owner(self, owner: Owner) -> None:
        self.owners.create(owner, owner.owner_id)

    def add_animal(self, animal: Animal) -> None:
        self.owners.get(animal.owner_id)
