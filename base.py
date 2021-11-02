from abc import ABC, abstractmethod


class Base(ABC):
    id = 0
    objects_list = list()

    def __init__(self, *args, **kwargs):
        self._id = self.generate_id()
        self.store_obj(self)

    @classmethod
    def generate_id(cls):
        cls.id = cls.id + 1
        return cls.id

    @classmethod
    def store_obj(cls, obj):
        cls.objects_list.append(obj)
