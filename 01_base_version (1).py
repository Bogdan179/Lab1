"""
Лабораторная работа №1.
Предметная область: домашние животные.

Реализовано:
- объектно-ориентированная модель предметной области;
- более 10 классов;
- наследование и полиморфизм;
- аннотации типов;
- CRUD для владельцев, животных и ветеринарных записей;
- встроенные и собственные исключения;
- сохранение и загрузка данных в JSON и XML.
"""

from __future__ import annotations

import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import Any


# =========================
# Собственные исключения
# =========================

class PetSystemError(Exception):
    """Базовое исключение системы домашних животных."""


class EntityNotFoundError(PetSystemError):
    """Объект с указанным идентификатором не найден."""


class ValidationError(PetSystemError):
    """Переданы некорректные данные."""


class DuplicateEntityError(PetSystemError):
    """Объект с таким идентификатором уже существует."""


# =========================
# Базовые классы животных
# =========================

class Animal(ABC):
    """Базовый класс домашнего животного."""

    def __init__(
        self,
        animal_id: int,
        name: str,
        age: int,
        owner_id: int
    ) -> None:
        if animal_id <= 0:
            raise ValidationError("ID животного должен быть положительным.")
        if not name.strip():
            raise ValidationError("Имя животного не может быть пустым.")
        if age < 0:
            raise ValidationError("Возраст не может быть отрицательным.")
        if owner_id <= 0:
            raise ValidationError("ID владельца должен быть положительным.")

        self.animal_id = animal_id
        self.name = name
        self.age = age
        self.owner_id = owner_id

    @property
    @abstractmethod
    def animal_type(self) -> str:
        """Возвращает вид животного."""

    @abstractmethod
    def make_sound(self) -> str:
        """Возвращает звук животного."""

    def to_dict(self) -> dict[str, Any]:
        return {
            "animal_id": self.animal_id,
            "name": self.name,
            "age": self.age,
            "owner_id": self.owner_id,
            "animal_type": self.animal_type,
        }


class Dog(Animal):
    """Собака."""

    @property
    def animal_type(self) -> str:
        return "Собака"
