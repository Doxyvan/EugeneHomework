from abc import ABC, abstractmethod

class Box(ABC):
    @abstractmethod
    def add(self, items):
        ...

    @abstractmethod
    def empty(self):
        ...

    @abstractmethod
    def count(self):
        ...
    
class Item():
    def __init__(self, name="untitled", value="None") -> None:
        self.name = name
        self.value = value

class ListBox(Box):
    def __init__(self) -> None:
        super().__init__()
        self.items = []

    def add(self, *items:Item):
        for i in items:
            self.items.append(i)

    def empty(self):
        x = self.items
        self.items = []
        return list(x)

    def count(self):
        return len(self.items)

class DictBox(Box):
    def __init__(self) -> None:
        super().__init__()
        self.items = dict()

    def add(self, *items:Item):
        for i in range(len(items)):
            self.items[id(items[i])] = items[i]

    def empty(self):
        x = self.items
        self.items = dict()
        return list(x.values())

    def count(self):
        return len(self.items)


def repack_boxes(*boxes:Box):
    temporary_box = []
    for i in range(len(boxes)):
        temporary_box = temporary_box + boxes[i].empty()

    cnt_of_boxes_for_each = (len(temporary_box)//len(boxes))
    
    for i in range(len(temporary_box)):
        boxes[i%len(boxes)].add(temporary_box[i])

lb1 = ListBox()
lb2 = ListBox()
db1 = DictBox()

for i in range(20):
    lb1.add(Item(str(i), i))

for i in range(9):
    lb2.add(Item(str(i), i))

for i in range(5):
    db1.add(Item(str(i), i))

print(lb1.count(), lb2.count(), db1.count())
repack_boxes(lb1, lb2, db1)
print(lb1.count(), lb2.count(), db1.count())