from abc import ABC, abstractmethod


class Base(ABC):
    _id = 0
    objects_list = list()

    def __init__(self):
        self._id = self.generate_id()
        self.store_obj(self)

    @classmethod
    def generate_id(cls):
        cls._id = cls._id + 1
        return cls._id

    @classmethod
    def store_obj(cls, obj):
        cls.objects_list.append(obj)
