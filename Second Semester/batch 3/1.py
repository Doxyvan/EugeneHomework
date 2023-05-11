class Accepted_Attr:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        return value

    def __set__(self, obj, value):
        if obj == "_name" and not obj in ["_do", "_re","_mi","_fa","_solt","_la","_si"]:
            raise ValueError("недопустимое значение аргумента")
        elif obj == "_name" and not obj in [-1, 0, 1]:
            raise ValueError("недопустимое значение аргумента")
        setattr(obj, self.private_name, value)


class Notes(object):
    __slots__ = ["_do", "_re","_mi","_fa","_solt","_la","_si"]
    def __init__(self) -> None:
        for i in range(len(self.__slots__)):
            self.__setattr__(self.__slots__[i], Note(self.__slots__[i], 0))

    def __getitem__(self, index):
        if index > len(self.__slots__)-1 or index<-len(self.__slots__):
            raise IndexError("недопустимый индекс")
        return getattr(self, self.__slots__[index])
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Notes, cls).__new__(cls)
        return cls.instance

class Note():
    name = Accepted_Attr()
    ton = Accepted_Attr()
    def __init__(self, name, ton) -> None:
        self.name = name
        self.ton = ton
    
    

notes = Notes()

notes2 = Notes()

print(notes[0])
print(notes[1]._name, notes[1]._ton)
print(id(notes), id(notes2))
